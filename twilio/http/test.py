import sys
import asyncio

from async_http_client import AsyncTwilioHttpClient

async def main():
    """
    Tests the AsyncTwilioHttpClient request method
    """
    id = sys.argv[1]
    url = 'https://pokeapi.co/api/v2/pokemon/{id}'.format(id=id)
    method = 'GET'

    client = AsyncTwilioHttpClient()
    response = await client.request(method, url)
    print('Status Code: ', response.status_code)
    print('Content Type: ', response.headers['content-type'])
    print('Raw Content: ', response.text[:60], '...')

asyncio.run(main())
