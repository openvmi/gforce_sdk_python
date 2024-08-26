import asyncio
import websockets

CONNECTIONS = set()

async def handle(websocket):
    if websocket not in CONNECTIONS:
        CONNECTIONS.add(websocket)
    try:
        async for message in websocket:
            print(message)
    finally:
        CONNECTIONS.remove(websocket)

async def broadcast(message):
    for websocket in CONNECTIONS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            pass

async def main():
    async with websockets.serve(handle, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())