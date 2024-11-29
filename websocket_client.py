import asyncio
import websockets
import json

async def connect_websocket():
    uri = "ws://alnoor-hajj.com/ws/manager-chat/7/2"
    
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to {uri}")
            
            # Keep the connection alive and handle messages
            while True:
                try:
                    # Receive message
                    message = await websocket.recv()
                    print(f"Received message: {message}")
                    
                    # Here you can add your message handling logic
                    
                except websockets.exceptions.ConnectionClosed:
                    print("Connection closed")
                    break
                
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Run the async function
    asyncio.get_event_loop().run_until_complete(connect_websocket())
