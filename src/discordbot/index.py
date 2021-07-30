import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv();
TOKEN = os.getenv('DISCORD_TOKEN');

bot = commands.Bot(command_prefix='>')
client = discord.Client()

class DiscordClient(discord.Client):
    @client.event
    async def on_ready(self):
        print('Logado no bot {0}!'.format(self.user))
    
    @client.event
    async def on_message(self, message):
        if message.content == 'criarficha':
            await message.channel.send('Oi, quer criar a sua ficha?');
            resposta = await client.wait_for("ficha", check=on_message)
            if resposta.content.lower() == "sim":
                await message.channel.send('CE RESPONDEU SIM');
            else:
                await message.channel.send("CE RESPONDEU NAO");
        else:
            print('Nao passei no if')

    @client.event    
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.sender(
            f'Oi {member.name} bem vindo ao Servidor'
        )

client = DiscordClient()
client.run(TOKEN)