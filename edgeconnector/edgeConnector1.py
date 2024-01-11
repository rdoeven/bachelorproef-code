import asyncio
import websockets
import json
from azure.iot.device.aio import IoTHubDeviceClient
import datetime


async def start_server(wsAddress, tagname, iot_hub_connection_string):
# Start the WebSocket server
    try:
        # Create an instance of the IoT Hub client
        iot_hub_client = IoTHubDeviceClient.create_from_connection_string(iot_hub_connection_string)
        await iot_hub_client.connect()

        async with websockets.connect(wsAddress) as websocket:
            while True:

                data = await websocket.recv()
                print(f"{datetime.datetime.now().time()} Message received from {wsAddress}: {data}")

                message_payload = {"data": data, "tag": tagname}



                # Send data to Azure IoT Hub
                await iot_hub_client.send_message(json.dumps(message_payload))
                print(f"{datetime.datetime.now().time()} Message sent")

    finally:
        await iot_hub_client.disconnect()

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server('ws://localhost:8765', 'oven', 'HostName=TestHub.azure-devices.net;DeviceId=Oven;SharedAccessKey=CznDN9OnpeFdZZBDpEwYIenxIxZKeI/uXAIoTFpyhn4='))
asyncio.get_event_loop().run_until_complete(start_server('ws://localhost:8764', 'mixer', 'HostName=TestHub.azure-devices.net;DeviceId=Mixer;SharedAccessKey=3Zllov6paAYh1T18P63T3udRsNEpESu9YAIoTLZDLc8='))
asyncio.get_event_loop().run_forever()