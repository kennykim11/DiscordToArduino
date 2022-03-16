import os
import discord
import requests

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
DISCORD_CHANNELS = ['test', 'help']
PUSH_URL = 'http://kennykim11-receipt-printer.herokuapp.com/push'
COMMAND = '!alert '

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.channel.name in DISCORD_CHANNELS:
            if message.content.startswith(COMMAND):
                text = message.content[len(COMMAND):]
                requests.post(PUSH_URL, data=text)
                print(text)

if __name__ == '__main__':
    client = DiscordClient()
    client.run(DISCORD_TOKEN)