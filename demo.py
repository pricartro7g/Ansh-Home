import asyncio
import json
import openai
import re
import websockets

async def keepalive(websocket):
    keepalive_request = {"_type": "KeepaliveRequest"}
    while True:
        await websocket.send(json.dumps(keepalive_request))
        await asyncio.sleep(15)

async def generate_response(prompt):
    openai.api_key = ""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
        language="en"
    )
    return response.choices[0].text.strip()

async def highrise_bot():
    websocket_endpoint = "wss://production.highrise.game/web/webapi"
    API_TOKEN = "98b2a2bf950cfc7fd4e6261203bc8279b3ed8b877c1bb7e73b404f9c4d459f7a"
    room_id = "641594f85b41ee085ed62db0"
    BOT_NAME = "IronManBot"

    async with websockets.connect(
        websocket_endpoint, extra_headers={"api-token": API_TOKEN, "room-id": room_id}
    ) as websocket:
        auth_response = json.loads(await websocket.recv())
        if auth_response["_type"] == "Error":
            print(f"Error authenticating: {auth_response['message']}")
            return

        # Start the keepalive task
        keepalive_task = asyncio.create_task(keepalive(websocket))

        # Listen for incoming messages
        while True:
            message = await websocket.recv()
            message_data = json.loads(message)
            print(message_data)

            if message_data["_type"] == "UserJoinedEvent":
                user = message_data["user"]
                user_id = user["id"]
                username = user["username"]

                # Send a welcome message to the user
                welcome_message = {
                    "_type": "ChatRequest",
                    "message": f"Welcome to The Night Court, {username}!",
                    "whisper_target_id": user_id,
                }
                await websocket.send(json.dumps(welcome_message))

            if message_data["_type"] == "ChatRequest" and "text" in message_data and f"@IronManBot" in message_data["text"] and message_data["text"].index(f"@MelroseBot") == len(message_data["text"]) - len(BOT_NAME) - 1:
                user_id = message_data["user_id"]
                message_text = message_data["text"][:len(message_data["text"]) - len(BOT_NAME) - 2]

                # Generate response using OpenAI API
                response_text = await generate_response(message_text)

                # Send response back to user
                response_message = {
                    "_type": "ChatRequest",
                    "message": response_text,
                    "whisper_target_id": user_id,
                }
                await websocket.send(json.dumps(response_message))

            # Send KeepaliveRequest every 15 seconds
            if message_data["_type"] == "KeepaliveRequest":
                keepalive_request = {"_type": "KeepaliveRequest"}
                await websocket.send(json.dumps(keepalive_request))

        # Cancel the keepalive task when the bot is disconnected
        keepalive_task.cancel()


asyncio.run(highrise_bot())
