import json
from concurrent.futures import CancelledError, ProcessPoolExecutor
import asyncio

from chat_fetcher import ChatFetcher


async def main(config_data):
    port = config_data['port']
    host = config_data['host']
    post_url = f'{host}:{port}/message' if port else f'{host}/message'

    fetchers = []
    videos = config_data['videos']
    for v in videos:
        fetchers.append(ChatFetcher(v, post_url).run())
    await asyncio.gather(*fetchers)


if __name__ == '__main__':
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)
            print(config)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(config))
    except CancelledError:
        pass
