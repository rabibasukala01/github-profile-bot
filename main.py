from discord.ext import commands
import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")
token = os.getenv('TOKEN')


client = commands.Bot(command_prefix="?", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ok")


@client.command()
async def github(context, *, message):

    githubAPI = f"https://api.github.com/users/{message}"
    result = requests.get(githubAPI)
    dic = result.json()
    try:
        myembed = discord.Embed(title="GITHUB", color=0x000000)
        myembed.add_field(name="username: ", value=dic["login"], inline=False)
        myembed.add_field(name="bio:", value=dic["bio"], inline=False)
        myembed.add_field(name="Followers: ",
                          value=dic["followers"], inline=True)
        myembed.add_field(name="Following:",
                          value=dic["following"], inline=True)
        myembed.add_field(name="Public Repos: ",
                          value=dic["public_repos"], inline=True)
        myembed.add_field(
            name="url:", value=f"https://github.com/{dic['login']}", inline=False)

        myembed.set_footer(
            text="created at" + ":"+dic["created_at"],
            icon_url=f"https://e7.pngegg.com/pngimages/914/758/png-clipart-computer-icons-logo-github-github-logo-logo-computer-program-thumbnail.png")
        myembed.set_author(name=f'Requested by: {context.author.name}')
        myembed.set_thumbnail(
            url=dic["avatar_url"]
        )
        await context.send(embed=myembed)
    except:
        await context.send(f"Error! No user found for {message}\nPlease Enter The Valid Username.")


client.run(token)
