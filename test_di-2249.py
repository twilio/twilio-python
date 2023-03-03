# Remove this file before completing this PR
"""
To run script:
python test_di-2249.py <int_id>
"""
import sys
import asyncio
import json
import time

from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.http.http_client import TwilioHttpClient


def get_test_request_kwargs(id):
    return {
        'url': 'https://pokeapi.co/api/v2/pokemon/{id}'.format(id=id),
        'method': 'GET'
    }


def print_twilio_response(response):
    print('================')
    print('Status Code: ', response.status_code)
    print('Content Type: ', response.headers['content-type'])
    print('Raw Content: ', response.text[:60], '...')
    if response.text:
        content_dict = json.loads(response.text)
        print('ID: {id}, Name: {name}'.format(id=content_dict['id'], name=content_dict['name']))
    print('================')


async def test_async_http_client_with_ctx_manager(kwargs):
    async with AsyncTwilioHttpClient() as client:
        response = await client.request(**kwargs)
        print_twilio_response(response)


async def test_async_http_client(kwargs):
    client = AsyncTwilioHttpClient()
    response = await client.request(**kwargs)
    print_twilio_response(response)
    await client.session.close()


async def test_async_request_with_client(kwargs, async_client=None, print_response=False):
    if async_client is None:
        raise RuntimeError('An asynchronous HTTP client is required.')
    response = await async_client.request(**kwargs)
    if print_response:
        print_twilio_response(response)


def test_request_with_client(kwargs, client=None, print_response=False):
    if client is None:
        raise RuntimeError('A synchronous HTTP client is required.')
    response = client.request(**kwargs)
    if print_response:
        print_twilio_response(response)


def test_sync_http_client(kwargs):
    client = TwilioHttpClient()
    response = client.request(**kwargs)
    print_twilio_response(response)


async def test_performance():
    # Performance tests
    print('===== Performance tests =====')
    sync_client = TwilioHttpClient()
    async_client = AsyncTwilioHttpClient()
    # --- Async requests
    print('Executing 100 async requests')
    start = time.time()
    for i in range(1, 101):
        kwargs = get_test_request_kwargs(i)
        await test_async_request_with_client(kwargs, async_client=async_client)
    print('Finished in {duration}s...'.format(duration=(time.time() - start)))
    # --- Sync requests
    print('Executing 100 sync requests')
    start = time.time()
    for i in range(1, 101):
        kwargs = get_test_request_kwargs(i)
        test_request_with_client(kwargs, client=sync_client)
    print('Finished in {duration}s...'.format(duration=(time.time() - start)))

    # Cleanup
    await async_client.session.close()


async def main():
    """
    Tests the AsyncTwilioHttpClient request method
    """
    id = sys.argv[1]
    kwargs = get_test_request_kwargs(id)

    # Simple test cases
    await test_async_http_client_with_ctx_manager(kwargs)
    await test_async_http_client(kwargs)
    test_sync_http_client(kwargs)

    # Performance tests
    await test_performance()


asyncio.run(main())
