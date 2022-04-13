import asyncio
import json
from random import randint

import websockets


async def handler(websocket):
    while True:
        try:
            data = {
                'a': randint(1, 100),
                'b': randint(0, pow(2, 32))
            }
            await websocket.send(json.dumps(data))
            await asyncio.sleep(0.001)
        except websockets.ConnectionClosedOK:
            break


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
