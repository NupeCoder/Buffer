import discord
from discord.ext import commands
import config


class Buffer(discord.Client):
    async def on_run(self):
        print(f'hello {self.user}')
        
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        print(f'Message from {message.author}: {message.content}')
        await message.channel.send('hello')
            

intents = discord.Intents.all()
intents.message_content = True

client  = Buffer(intents=intents)

client.run(config.TOKEN)
