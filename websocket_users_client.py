import asyncio
import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        message = 'Привет, сервер!'
        print(f'Отправка: {message}')
        await websocket.send(message)

        for i in range(1, 6):
            response = await websocket.recv()
            print(i, response)


asyncio.run(client())