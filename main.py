import copy
from typing import Annotated

from fastapi import FastAPI, Body, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware

from interpret import interpret
from machine import Machine

def create_app():
    app = FastAPI()
    machine = Machine()

    @app.post("/interpret_machine")
    async def interpret_machine(request: Request):
        definition = (await request.json())['definition']
        machine.update(*interpret(definition))
        return {
            "message": "Machine interpreter done!",
            "state": machine.initial_state
        }

    @app.post("/run")
    async def run(request: Request):
        local_machine = copy.copy(machine)
        request_json = (await request.json())
        return {"message": await machine.run(request_json['input_string'], request_json['run'])}

    @app.websocket("/ws")
    async def websocket(websocket: WebSocket):
        await websocket.accept()
        machine.add_websocket(websocket)
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f'Message: {data}')

    return app

app = create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)