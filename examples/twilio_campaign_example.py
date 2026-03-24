#!/usr/bin/env python
"""
Twilio Messaging Campaign Example

This comprehensive example demonstrates how to:
1. Create messaging services with status callbacks
2. Configure link shortening domains and TLS certificates
3. Send campaign messages with rate limiting and retry logic
4. Review campaign performance with pagination
5. Handle webhooks for delivery status and click tracking

Requirements:
    pip install twilio flask

Environment Variables:
    TWILIO_ACCOUNT_SID - Your Twilio Account SID
    TWILIO_AUTH_TOKEN - Your Twilio Auth Token

Usage:
    # Run the full campaign example
    python examples/twilio_campaign_example.py

    # Run webhook server only
    python examples/twilio_campaign_example.py --webhooks-only
"""

import os
import sys
import time
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from collections import defaultdict

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.request_validator import RequestValidator


# ============================================================================
# Section 1: Configuration & Setup
# ============================================================================

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Twilio credentials from environment
ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
PHONE_NUMBER_SID = os.environ.get('PHONE_NUMBER_SID')

if not ACCOUNT_SID or not AUTH_TOKEN:
    logger.error("Missing TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN environment variables")
    sys.exit(1)

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# ============================================================================
# Section 2: Messaging Service Infrastructure
# ============================================================================

def create_messaging_service(
    friendly_name: str,
    status_callback_url: Optional[str] = None,
    usecase: str = 'marketing',
    sticky_sender: bool = True
) -> Dict:
    """
    Create a Twilio messaging service for campaign messages.

    Args:
        friendly_name: Human-readable name for the service
        status_callback_url: URL for message status updates (delivered, failed, etc.)
        usecase: Service use case ('marketing', '2fa', 'notifications', etc.)
        sticky_sender: Whether to use the same sender for all messages to a recipient

    Returns:
        Dictionary containing service details (sid, friendly_name, etc.)
    """
    logger.info(f"Creating messaging service: {friendly_name}")

    try:
        service = client.messaging.v1.services.create(
            friendly_name=friendly_name,
            status_callback=status_callback_url,
            usecase=usecase,
            sticky_sender=sticky_sender
        )

        logger.info(f"✓ Messaging service created: {service.sid}")
        return {
            'sid': service.sid,
            'friendly_name': service.friendly_name,
            'status_callback': service.status_callback,
            'usecase': service.usecase
        }
    except TwilioRestException as e:
        logger.error(f"Failed to create messaging service: {e.msg} (Code: {e.code})")
        raise


def add_phone_number_to_service(service_sid: str, phone_number_sid: str) -> bool:
    """
    Add a phone number to a messaging service.

    Args:
        service_sid: The messaging service SID
        phone_number_sid: The phone number SID to add

    Returns:
        True if successful
    """
    logger.info(f"Adding phone number {phone_number_sid} to service {service_sid}")

    try:
        client.messaging.v1.services(service_sid).phone_numbers.create(
            phone_number_sid=phone_number_sid
        )
        logger.info("✓ Phone number added to service")
        return True
    except TwilioRestException as e:
        logger.error(f"Failed to add phone number: {e.msg} (Code: {e.code})")
        raise


# ============================================================================
# Section 3: Link Shortening Domain Setup
# ============================================================================

def upload_tls_certificate(domain_sid: str, tls_cert_pem: str) -> Dict:
    """
    Upload a TLS certificate for link shortening domain.

    Args:
        domain_sid: The domain SID
        tls_cert_pem: PEM-encoded TLS certificate content

    Returns:
        Dictionary containing certificate details
    """
    logger.info(f"Uploading TLS certificate for domain: {domain_sid}")

    try:
        cert = client.messaging.v1.domain_certs.get(domain_sid).update(
            tls_cert=tls_cert_pem
        )

        logger.info("✓ TLS certificate uploaded successfully")
        return {
            'domain_sid': cert.domain_sid,
            'date_updated': cert.date_updated
        }
    except TwilioRestException as e:
        logger.error(f"Failed to upload certificate: {e.msg} (Code: {e.code})")
        raise


def configure_link_shortening_domain(
    domain_sid: str,
    callback_url: str,
    fallback_url: Optional[str] = None
) -> Dict:
    """
    Configure link shortening domain with click tracking callbacks.

    Args:
        domain_sid: The domain SID
        callback_url: URL to receive click tracking events
        fallback_url: Fallback URL if callback fails

    Returns:
        Dictionary containing domain configuration
    """
    logger.info(f"Configuring link shortening domain: {domain_sid}")

    try:
        config = client.messaging.v1.domain_config.get(domain_sid).update(
            callback_url=callback_url,
            fallback_url=fallback_url
        )

        logger.info("✓ Domain configuration updated")
        return {
            'domain_sid': config.domain_sid,
            'callback_url': config.callback_url,
            'fallback_url': config.fallback_url
        }
    except TwilioRestException as e:
        logger.error(f"Failed to configure domain: {e.msg} (Code: {e.code})")
        raise


# ============================================================================
# Section 4: Campaign Message Sending
# ============================================================================

class RateLimitHandler:
    """
    Handle rate limiting (HTTP 429) with exponential backoff retry logic.
    """

    def __init__(self, max_retries: int = 5, initial_delay: float = 1.0):
        self.max_retries = max_retries
        self.initial_delay = initial_delay

    def send_with_retry(self, send_func, *args, **kwargs):
        """
        Execute a send function with exponential backoff on rate limit errors.

        Args:
            send_func: Function to call for sending message
            *args, **kwargs: Arguments to pass to send_func

        Returns:
            Message object if successful

        Raises:
            TwilioRestException: If all retries fail or non-retryable error occurs
        """
        delay = self.initial_delay

        for attempt in range(self.max_retries):
            try:
                return send_func(*args, **kwargs)

            except TwilioRestException as e:
                # Handle rate limiting (429)
                if e.status == 429:
                    if attempt < self.max_retries - 1:
                        logger.warning(
                            f"Rate limited (429). Retrying in {delay}s "
                            f"(attempt {attempt + 1}/{self.max_retries})"
                        )
                        time.sleep(delay)
                        delay *= 2  # Exponential backoff
                        continue
                    else:
                        logger.error("Max retries reached for rate limiting")
                        raise

                # Handle unreachable destination (30003)
                elif e.code == 30003:
                    logger.error(f"Unreachable destination: {e.msg}")
                    raise

                # Handle landline/unreachable carrier (30006)
                elif e.code == 30006:
                    logger.error(f"Landline or unreachable carrier: {e.msg}")
                    raise

                # Other errors - don't retry
                else:
                    logger.error(f"Message send failed: {e.msg} (Code: {e.code})")
                    raise

        raise TwilioRestException(
            status=429,
            uri="",
            msg="Max retries exceeded for rate limiting"
        )


def send_campaign_message(
    to: str,
    body: str,
    messaging_service_sid: str,
    status_callback: Optional[str] = None,
    shorten_urls: bool = True,
    rate_limit_handler: Optional[RateLimitHandler] = None
) -> Dict:
    """
    Send a campaign message with rate limiting support.

    Args:
        to: Recipient phone number (E.164 format)
        body: Message text content
        messaging_service_sid: SID of the messaging service to use
        status_callback: URL for delivery status updates
        shorten_urls: Whether to shorten URLs in message
        rate_limit_handler: RateLimitHandler instance for retry logic

    Returns:
        Dictionary containing message details (sid, status, etc.)
    """
    if rate_limit_handler is None:
        rate_limit_handler = RateLimitHandler()

    def _send():
        return client.messages.create(
            messaging_service_sid=messaging_service_sid,
            to=to,
            body=body,
            status_callback=status_callback,
            shorten_urls=shorten_urls
        )

    try:
        message = rate_limit_handler.send_with_retry(_send)

        logger.info(f"✓ Message sent to {to}: {message.sid} (Status: {message.status})")
        return {
            'sid': message.sid,
            'to': message.to,
            'status': message.status,
            'date_created': message.date_created
        }
    except TwilioRestException as e:
        logger.error(f"Failed to send message to {to}: {e.msg}")
        return {
            'sid': None,
            'to': to,
            'status': 'failed',
            'error_code': e.code,
            'error_message': e.msg
        }


def send_bulk_campaign(
    recipients: List[str],
    message_body: str,
    messaging_service_sid: str,
    batch_delay: float = 0.1
) -> Dict:
    """
    Send messages to multiple recipients with rate limiting.

    Args:
        recipients: List of recipient phone numbers
        message_body: Message text to send
        messaging_service_sid: SID of the messaging service
        batch_delay: Delay between messages (seconds)

    Returns:
        Dictionary with campaign statistics
    """
    logger.info(f"Starting bulk campaign to {len(recipients)} recipients")

    rate_handler = RateLimitHandler(max_retries=5, initial_delay=1.0)
    results = {
        'total': len(recipients),
        'sent': 0,
        'failed': 0,
        'messages': []
    }

    for i, recipient in enumerate(recipients, 1):
        logger.info(f"Sending message {i}/{len(recipients)} to {recipient}")

        result = send_campaign_message(
            to=recipient,
            body=message_body,
            messaging_service_sid=messaging_service_sid,
            rate_limit_handler=rate_handler
        )

        results['messages'].append(result)

        if result['status'] != 'failed':
            results['sent'] += 1
        else:
            results['failed'] += 1

        # Small delay between messages
        if i < len(recipients):
            time.sleep(batch_delay)

    logger.info(
        f"✓ Campaign complete: {results['sent']} sent, {results['failed']} failed"
    )
    return results


# ============================================================================
# Section 5: Campaign Performance Review
# ============================================================================

def get_campaign_messages(
    from_number: Optional[str] = None,
    to_number: Optional[str] = None,
    date_sent_after: Optional[datetime] = None,
    date_sent_before: Optional[datetime] = None,
    messaging_service_sid: Optional[str] = None,
    limit: int = 1000
) -> List[Dict]:
    """
    Retrieve campaign messages with pagination support.

    Note: The Twilio Messages API stream() method does NOT support filtering by
    messaging_service_sid directly. It only supports: to, from_, date_sent filters.

    If you need to filter by messaging service, you have two options:
    1. Use from_number to filter by a specific sender from your messaging service
    2. Fetch all messages and filter in-memory by messaging_service_sid (less efficient)

    Args:
        from_number: Filter by sender phone number (E.164 format, e.g., "+15551234567")
        to_number: Filter by recipient phone number (E.164 format)
        date_sent_after: Only include messages sent after this date
        date_sent_before: Only include messages sent before this date
        messaging_service_sid: If provided, filter results in-memory by this messaging service SID
        limit: Maximum number of messages to retrieve from API (before in-memory filtering)

    Returns:
        List of message dictionaries

    Example:
        # Get messages from a specific phone number in your messaging service
        messages = get_campaign_messages(
            from_number="+15551234567",
            date_sent_after=datetime(2024, 1, 1)
        )

        # Get all account messages and filter by messaging service (slower)
        messages = get_campaign_messages(
            messaging_service_sid="MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            date_sent_after=datetime(2024, 1, 1)
        )
    """
    logger.info("Fetching campaign messages...")

    messages = []

    try:
        # Use stream() for automatic pagination
        # WARNING: stream() does NOT support messaging_service_sid parameter
        for message in client.messages.stream(
            to=to_number,
            from_=from_number,
            date_sent_after=date_sent_after,
            date_sent_before=date_sent_before,
            page_size=100,
            limit=limit
        ):
            # Filter by messaging_service_sid in memory if provided
            if messaging_service_sid and message.messaging_service_sid != messaging_service_sid:
                continue

            messages.append({
                'sid': message.sid,
                'to': message.to,
                'from': message.from_,
                'body': message.body,
                'status': message.status,
                'date_sent': message.date_sent,
                'date_created': message.date_created,
                'error_code': message.error_code,
                'error_message': message.error_message,
                'num_segments': message.num_segments,
                'price': message.price,
                'price_unit': message.price_unit,
                'messaging_service_sid': message.messaging_service_sid
            })

        logger.info(f"✓ Retrieved {len(messages)} messages")
        return messages

    except TwilioRestException as e:
        logger.error(f"Failed to fetch messages: {e.msg} (Code: {e.code})")
        raise


def calculate_campaign_statistics(messages: List[Dict]) -> Dict:
    """
    Calculate performance statistics from campaign messages.

    Args:
        messages: List of message dictionaries from get_campaign_messages()

    Returns:
        Dictionary with campaign statistics
    """
    stats = {
        'total_messages': len(messages),
        'by_status': defaultdict(int),
        'total_segments': 0,
        'total_cost': 0.0,
        'error_breakdown': defaultdict(int),
        'delivery_rate': 0.0
    }

    for msg in messages:
        # Count by status
        stats['by_status'][msg['status']] += 1

        # Sum segments
        if msg['num_segments']:
            stats['total_segments'] += int(msg['num_segments'])

        # Sum costs
        if msg['price']:
            stats['total_cost'] += abs(float(msg['price']))

        # Error breakdown
        if msg['error_code']:
            stats['error_breakdown'][msg['error_code']] += 1

    # Calculate delivery rate
    delivered = stats['by_status'].get('delivered', 0)
    if stats['total_messages'] > 0:
        stats['delivery_rate'] = (delivered / stats['total_messages']) * 100

    return dict(stats)


def print_campaign_report(stats: Dict):
    """
    Print a formatted campaign performance report.

    Args:
        stats: Statistics dictionary from calculate_campaign_statistics()
    """
    print("\n" + "=" * 60)
    print("CAMPAIGN PERFORMANCE REPORT")
    print("=" * 60)

    print(f"\nTotal Messages: {stats['total_messages']}")
    print(f"Total Segments: {stats['total_segments']}")
    print(f"Total Cost: ${stats['total_cost']:.4f} {list(stats.get('messages', [{}]))[0].get('price_unit', 'USD') if stats.get('messages') else 'USD'}")
    print(f"Delivery Rate: {stats['delivery_rate']:.2f}%")

    print("\nStatus Breakdown:")
    for status, count in sorted(stats['by_status'].items()):
        percentage = (count / stats['total_messages']) * 100
        print(f"  {status.capitalize():.<20} {count:>5} ({percentage:>5.1f}%)")

    if stats['error_breakdown']:
        print("\nError Code Breakdown:")
        for error_code, count in sorted(stats['error_breakdown'].items()):
            print(f"  Error {error_code}{'.'*10} {count:>5}")

    print("\n" + "=" * 60 + "\n")


# ============================================================================
# Section 6: Webhook Handlers
# ============================================================================

def validate_twilio_request(url: str, params: Dict, signature: str) -> bool:
    """
    Validate that a webhook request came from Twilio.

    Args:
        url: Full URL of the webhook endpoint
        params: Request parameters (POST body or query string)
        signature: X-Twilio-Signature header value

    Returns:
        True if request is valid, False otherwise
    """
    validator = RequestValidator(AUTH_TOKEN)
    return validator.validate(url, params, signature)


def create_webhook_app():
    """
    Create a Flask app with webhook handlers for status callbacks and click tracking.

    Returns:
        Flask application instance
    """
    try:
        from flask import Flask, request, jsonify
    except ImportError:
        logger.error("Flask is not installed. Run: pip install flask")
        return None

    app = Flask(__name__)

    @app.route('/webhooks/status', methods=['POST'])
    def status_callback():
        """
        Handle message status updates (queued, sent, delivered, failed, etc.).
        """
        # Validate request signature
        signature = request.headers.get('X-Twilio-Signature', '')
        url = request.url

        if not validate_twilio_request(url, request.form.to_dict(), signature):
            logger.warning(f"Invalid webhook signature from {request.remote_addr}")
            return jsonify({'error': 'Invalid signature'}), 403

        # Extract status update data
        message_sid = request.form.get('MessageSid')
        message_status = request.form.get('MessageStatus')
        to = request.form.get('To')
        error_code = request.form.get('ErrorCode')
        error_message = request.form.get('ErrorMessage')

        logger.info(
            f"Status update: {message_sid} to {to} - "
            f"Status: {message_status}"
        )

        if error_code:
            logger.error(
                f"Message {message_sid} error: {error_message} "
                f"(Code: {error_code})"
            )

        # Here you would typically:
        # - Update database with message status
        # - Trigger alerts for failed messages
        # - Update campaign analytics

        return jsonify({'status': 'received'}), 200

    @app.route('/webhooks/click-tracking', methods=['POST'])
    def click_tracking():
        """
        Handle link click tracking events.
        """
        # Validate request signature
        signature = request.headers.get('X-Twilio-Signature', '')
        url = request.url

        if not validate_twilio_request(url, request.form.to_dict(), signature):
            logger.warning(f"Invalid webhook signature from {request.remote_addr}")
            return jsonify({'error': 'Invalid signature'}), 403

        # Extract click tracking data
        message_sid = request.form.get('MessageSid')
        link_clicked = request.form.get('LinkUrl')
        recipient = request.form.get('To')
        click_time = request.form.get('Timestamp')

        logger.info(
            f"Link clicked: {link_clicked} in message {message_sid} "
            f"by {recipient} at {click_time}"
        )

        # Here you would typically:
        # - Store click event in analytics database
        # - Update campaign engagement metrics
        # - Trigger follow-up actions

        return jsonify({'status': 'received'}), 200

    @app.route('/health', methods=['GET'])
    def health():
        """Health check endpoint."""
        return jsonify({'status': 'healthy'}), 200

    return app


def run_webhook_server(host: str = '0.0.0.0', port: int = 5000):
    """
    Start the webhook server.

    Args:
        host: Host to bind to
        port: Port to listen on

    Note:
        For production, use ngrok or similar to expose webhooks:
            ngrok http 5000
        Then configure Twilio with your ngrok URL.
    """
    app = create_webhook_app()

    if app is None:
        return

    logger.info(f"Starting webhook server on {host}:{port}")
    logger.info(
        "For local development, expose this with ngrok:\n"
        f"  ngrok http {port}\n"
        "Then configure Twilio webhooks with your ngrok URL"
    )

    app.run(host=host, port=port, debug=False)


# ============================================================================
# Section 7: Main Execution - Complete Workflow
# ============================================================================

def main():
    """
    Run a complete messaging campaign demonstration.
    """
    print("\n" + "=" * 60)
    print("TWILIO MESSAGING CAMPAIGN EXAMPLE")
    print("=" * 60 + "\n")

    try:
        # Step 1: Create messaging service
        print("Step 1: Creating messaging service...")
        service = create_messaging_service(
            friendly_name="Marketing Campaign Service",
            status_callback_url="https://shaggy-heads-join.loca.lt/webhooks/status",
            usecase='marketing',
            sticky_sender=True
        )
        service_sid = service['sid']
        print(f"✓ Service created: {service_sid}\n")

        # Optional: Add phone numbers to the service
        # phone_number_sid = "PN..."  # Your Twilio phone number SID
        add_phone_number_to_service(service_sid, PHONE_NUMBER_SID)

        # Step 2: Configure link shortening (optional - requires domain)
        print("Step 2: Link shortening configuration (skipped - requires domain)")
        print("  To enable link shortening:")
        print("  1. Configure a domain in Twilio Console")
        print("  2. Upload TLS certificate using upload_tls_certificate()")
        print("  3. Configure callbacks using configure_link_shortening_domain()\n")

        # Step 3: Send campaign messages
        print("Step 3: Sending campaign messages...")

        # Example recipients (replace with real phone numbers for testing)
        recipients = [
            "+1234567890",  # Replace with real numbers
            "+1234567891",
            "+1234567892"
        ]

        message_body = (
            "Hello! Check out our new product launch: "
            "https://example.com/campaign"
        )

        # Uncomment to actually send messages
        # campaign_results = send_bulk_campaign(
        #     recipients=recipients,
        #     message_body=message_body,
        #     messaging_service_sid=service_sid,
        #     batch_delay=0.1
        # )

        print("  (Skipped - update recipients list with real numbers to test)\n")

        # Step 4: Review campaign performance
        print("Step 4: Reviewing campaign performance...")

        # Fetch messages from last 24 hours
        # Note: For better performance, use from_number instead of messaging_service_sid
        date_after = datetime.now() - timedelta(days=1)

        # Option A: Filter by messaging service (in-memory filtering - slower)
        messages = get_campaign_messages(
            messaging_service_sid=service_sid,
            date_sent_after=date_after,
            limit=1000
        )

        # Option B: Filter by specific sender number (API filtering - faster)
        # Uncomment and replace with your Twilio phone number:
        # messages = get_campaign_messages(
        #     from_number=TWILIO_PHONE_NUMBER,
        #     date_sent_after=date_after,
        #     limit=1000
        # )

        if messages:
            stats = calculate_campaign_statistics(messages)
            print_campaign_report(stats)
        else:
            print("  No messages found in the last 24 hours\n")

        # Step 5: Webhook information
        print("Step 5: Webhook setup")
        print("  To handle status callbacks and click tracking:")
        print("  1. Run webhook server: python examples/twilio_campaign_example.py --webhooks-only")
        print("  2. Expose with ngrok: ngrok http 5000")
        print("  3. Configure Twilio webhooks with your ngrok URL")
        print("     - Status callback: https://your-ngrok-url.ngrok.io/webhooks/status")
        print("     - Click tracking: https://your-ngrok-url.ngrok.io/webhooks/click-tracking\n")

        print("=" * 60)
        print("Campaign demonstration complete!")
        print("=" * 60 + "\n")

    except TwilioRestException as e:
        logger.error(f"Campaign failed: {e.msg} (Code: {e.code})")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Twilio Messaging Campaign Example'
    )
    parser.add_argument(
        '--webhooks-only',
        action='store_true',
        help='Run webhook server only (no campaign execution)'
    )

    args = parser.parse_args()

    if args.webhooks_only:
        run_webhook_server(host='0.0.0.0', port=5000)
    else:
        main()
