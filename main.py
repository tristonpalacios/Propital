from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Embed
from responses._init_ import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        return
    if is_private := user_message.startswith('?'):
        user_message = user_message[1:]

    try:
        response = await get_response(user_message)
        if isinstance(response, tuple):
            embed, views = response
            sent_message = await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
            for view in views:
                await sent_message.channel.send(view=view)
        elif isinstance(response, list):
            for embed in response:
                await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        elif isinstance(response, Embed):
            await message.author.send(embed=response) if is_private else await message.channel.send(embed=response)
        elif isinstance(response, str):
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        await message.channel.send('An error occurred while processing your request.')



@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')

    await send_message(message, user_message)


# Entry Point
def main() -> None:
    client.run(TOKEN)


if __name__ == '__main__':
    main()
