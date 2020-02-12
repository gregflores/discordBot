import discord
import random
import time
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", 'https://www.googleapis.com/auth/spreadsheets', "https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets.readonly']

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)


mcoc = client.open_by_url('https://docs.google.com/spreadsheets/d/1beR2CAlBQ2XBA3M1jJ1aPEfwE46eQt6LU-lzA0babxQ/edit#gid=0').sheet1


def read_token():
    with open('.token', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

# global ryanspam, willspam
ryanspam = 2
willspam = 10
messages = 0


async def update_stats():
    await client.wait_until_ready()
    global messages

    while not client.is_closed():
        try:
            with open('stats.txt', 'a') as f:
                f.write(f'Time: {int(time.time())}, Messages: {messages}\n')

                messages = 0

                await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='with cum'))
    # print(client.guilds)
    print(client.guilds[0])
    # id = client.guilds[0]
    # print(id.emojis)


@client.event
async def on_message(message):
    global messages
    global ryanspam
    global willspam
    messages += 1
    id = client.guilds[0]
    # print(id)
    # print(message.author.name)
    if message.author.name == 'OnlyJust':
        willspam -= 1
        if willspam == 0:
            await message.author.send('OwO')
            willspam = 100
    if message.author.name == 'Userface':
        ryanspam -= 1
        if ryanspam == 0:
            await message.author.send('Ryan and Greg 100 years!')
            ryanspam = 100
    if message.author == client.user:
        return
    if message.content == "$help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="$hello", value="Greets the user")
        embed.add_field(name="$users", value="Prints number of users")
        embed.add_field(name="(╯°□°）╯︵ ┻━┻", value="No")
        embed.add_field(name="$sobble", value=discord.utils.get(id.emojis, name='sobble_o'))
        await message.channel.send(content=None, embed=embed)
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith("$users"):
        await message.channel.send(f"""# of members {id.member_count}""")
    elif message.content.startswith("(╯°□°）╯︵ ┻━┻"):
        await message.channel.send('┬─┬ ノ( ゜-゜ノ)')
    elif message.content.startswith('$sobble'):
        emoji = discord.utils.get(id.emojis, name='sobble_o')
        if emoji:
            await message.channel.send(emoji)
    elif message.content.startswith('$beyondgod'):
        col = mcoc.col_values(1)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$godtier'):
        col = mcoc.col_values(2)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$highdemi'):
        col = mcoc.col_values(3)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$lowdemi'):
        col = mcoc.col_values(4)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$prettyuseful'):
        col = mcoc.col_values(5)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$occasionally'):
        col = mcoc.col_values(6)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content.startswith('$memetier'):
        col = mcoc.col_values(7)
        msg = ''
        for champ in col[2:]:
            msg += champ + '\n'
        await message.channel.send(msg)
    elif message.content == "$tierlist":
        embed = discord.Embed(title="MCOC Tier List", description="Champs you play")
        embed.add_field(name='$beyondgod', value="Beyond God", inline=False)
        embed.add_field(name="$godtier", value="God Tier", inline=False)
        embed.add_field(name="$highdemi", value="High Demi God", inline=False)
        embed.add_field(name="$lowdemi", value='Low Demi God', inline=False)
        embed.add_field(name="$prettyuseful", value='Pretty Useful', inline=False)
        embed.add_field(name="$occasionally", value='Occasionally Useful', inline=False)
        embed.add_field(name="$memetier", value='Meme Tier', inline=False)
        await message.channel.send(content=None, embed=embed)
    elif message.content.startswith('$buddiestier'):
        buddies = discord.utils.get(id.roles, name='buddies').members
        # print(buddies)
        buddies = [buddy.nick for buddy in buddies]
        # print(buddies)
        random.shuffle(buddies)
        msg = ''
        for rank, buddy in enumerate(buddies):
            msg += '{}. {}\n'.format(rank + 1, buddy)
        await message.channel.send(msg)
    elif message.content.startswith('$truebuddiestier'):
        buddies = discord.utils.get(id.roles, name='buddies').members
        # print(buddies)
        buddies = [buddy.nick for buddy in buddies]
        buddies.remove('Will')
        # print(buddies)
        random.shuffle(buddies)
        msg = ''
        for rank, buddy in enumerate(buddies):
            msg += '{}. {}\n'.format(rank + 1, buddy)
        msg += '{}. {}\n'.format(8, 'Will')
        await message.channel.send(msg)
    if 'OwO' in message.content:
        emoji = discord.utils.get(id.emojis, name='furhot')
        if emoji:
            await message.add_reaction(emoji)
client.loop.create_task(update_stats())
client.run(token)
