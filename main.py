import asyncio
import websockets

import json

from helper import math_functions


async def handler():
    async with websockets.connect('ws://127.0.0.1:8001') as websocket:
        cont_estuct = 0
        cont_min = 0
        b_list = []
        while True:
            response = await websocket.recv()
            dict_response = json.loads(response)
            b_list.append(dict_response['b'])
            cont_estuct += 1
            if cont_estuct == 6:
                print({'max_number': max(b_list),
                       'min_number': min(b_list),
                       'first_number': b_list[0],
                       'last_number': b_list[-1],
                       'number_of_prime_numbers': math_functions.count_prime_list(b_list),
                       'number_of_even_numbers': math_functions.count_even_list(b_list),
                       'number_of_odd_numbers': math_functions.count_odd_list(b_list)
                       })
                print(b_list)
                b_list = []


asyncio.get_event_loop().run_until_complete(handler())
