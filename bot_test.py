import discord
import time
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身份:', client.user)
    activity = discord.Game('Code a Discord Bot')
    await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.event
async def on_message(message):
    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel
        await channel.send('那你先跟我說你好')
        def checkmessage(m):
            return m.content == '你好' and m.channel == channel
        msg = await client.wait_for('message', check=checkmessage)
        await channel.send('嗨, {.author}!'.format(msg))

    if message.content == '我好帥喔':
        tmpmsg = await message.channel.send('你確定你帥嗎？')
        await asyncio.sleep(3)
        await tmpmsg.delete()

    if message.content == '我真帥':
        await message.delete()
        await message.channel.send('你這根本就是詐欺')
    
    if message.content == '群組':
        guilds = await client.fetch_guilds(limit=150).flatten()
        for i in guilds:
            await message.channel.send(i.name)

    print(message.content)
    
    if message.author == client.user:
        return
    if message.content.startswith('?say'):
        tmp = message.content.split(" ",1)
        print(tmp)
        if len(tmp) == 1:
            await message.channel.send(f"{message.author.mention} 你要我說什麼啦..")
        else:
            await message.channel.send(f"{message.author.mention} 逼我說「{tmp[1]}」")

client.run('')

