from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import redis
import json
import asyncio

app = FastAPI()

# Configuração do Redis
redis_client = redis.StrictRedis(host='fastapi_chat_redis_1', port=6379, db=0, password='Redis')

@app.get("/")
async def get():
    with open("templates/chat.html") as f:
        content = f.read()
    return HTMLResponse(content=content)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            redis_client.publish('chat', json.dumps(message))
            await manager.broadcast(message['content'])
    except WebSocketDisconnect:
        manager.disconnect(websocket)

async def redis_listener():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('chat')
    async for message in pubsub.listen():
        if message['type'] == 'message':
            await manager.broadcast(message['data'].decode('utf-8'))

@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(redis_listener())