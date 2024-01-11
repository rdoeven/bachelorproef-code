import asyncio
import random
import websockets
import json
import datetime

async def send_random_int(websocket, path):
    while True:
        random_int = random.randint(50, 200)
        try:
            await websocket.send(str(random_int))
            print(f"[{datetime.datetime.now().time()}] {websocket.port} sent: {random_int}")
            await asyncio.sleep(5)
        except Exception as e:
            print("error recieved: " + str(e))

async def send_random_int_packed(websocket, path):
    while True:
        random_int = random.randint(50, 200)
        try:
            await websocket.send(json.dumps({
                "value" : random_int,
                "quality" : "good enough"
            }))
            print(f"[{datetime.datetime.now().time()}] sent: {random_int}")
            await asyncio.sleep(5)
        except Exception as e:
            print("error recieved: " + str(e))
            
    


start_oven = websockets.serve(send_random_int, 'localhost', 8765)
start_mixer = websockets.serve(send_random_int, 'localhost', 8764)

asyncio.get_event_loop().run_until_complete(start_oven)
asyncio.get_event_loop().run_until_complete(start_mixer)
asyncio.get_event_loop().run_forever()
