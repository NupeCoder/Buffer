import discord
from discord.ext import commands
import config


class Buffer(discord.Client):
    async def on_run(self):
        print(f'hello {self.user}')
        
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content == ("!mma"):
            await message.channel.send('Search a fighter?')
        
    


intents = discord.Intents.all()
intents.message_content = True

client  = Buffer(intents=intents)

client.run(config.TOKEN)
