import os
import random
import requests
import json
import discord
from discord.ext import commands
import keep_alive
from discord import Intents
from discord.ext import commands

intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix ="%", intents=intents)

#logged
@client.event
async def on_ready():
  print('WE HAVE LOGGED IN')

#welcome IN Server
@client.event
async def on_member_join(member):
  guild = client.get_guild(930722774513754112)
  channel = guild.get_channel(930722774513754114)
  await channel.send(f"Welcome to the server my friend {member. mention}! How are you? You can do your <#936819091992354826>, if you want us to know you better. Enjoy your stay...")
  await member.send(f"We are so excited you have joined our community! {member. mention}, with your great personality, you are going to be a great addition. Welcome! https://discord.gg/Un7hEt7NC9")
   
#hello  
@client.command()
async def hello(ctx):
   await ctx.reply(f'Just a friendly little hello from me to you! ({round(client.latency*1000)}ms)')

#who?
@client.command()
async def introduce(ctx):
   await ctx.reply(f'Hi, I am the first personalized bot of this server. Lovely to virtually meet you!  ({round(client.latency*1000)}ms)')
  
#bye
@client.command()
async def bye(ctx):
   await ctx.reply(f'If you are brave enough to say goodbye, life will reward you with a new hello. ({round(client.latency*1000)}ms)')
  
#help
@client.command()
async def h(ctx):
   await ctx.reply(f'How may I help you DEAR!! ({round(client.latency*1000)}ms)')
   
#question - smart?
@client.command(aliases = ['friend','test'])
async def _friend(ctx,*,question):
   responses = ['It is certain.',' Without a doubt.',' Yes definitely.',' You may rely on it.','As I see it, yes.',' Most likely.',' Yes.',' Signs point to yes.', ' Better not tell you now.',' Cannot predict now.',' Concentrate and ask again.','I do not think so', 'Sorry, no. I am really busy with my own tasks right now.','Agreeing to this would go against what I believe in','That is right','You got it.']
   await ctx.reply(f'Question: {question}\nAnswer: {random.choice(responses)}  ({round(client.latency*1000)}ms)') 

#delete msges
@client.command()
async def cl(ctx, amount = 0):
  await ctx.channel.purge(limit=amount)

def get_quote():
  response = requests.get("http://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return (quote)
    
#inspire
@client.command()
async def inspire(ctx):
    await ctx.reply(get_quote())
  
keep_alive.keep_alive()
client.run('OTUwNjcwMDcyOTk1Nzc4NjAw.GgF7N5.Sg1T90w9SE-WvQlBT_vO6DlnzWIiw4NAhwn3H0')