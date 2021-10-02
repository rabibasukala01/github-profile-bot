from discord.ext import commands
import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")
token = os.getenv('TOKEN')


# # print(dic["created_at"])
# print(dic["bio"])4
# # print(dic["avatar_url"])
# print(dic["login"])
# print(dic["followers"])
# print(dic["following"])
# print(dic["public_repos"])  # number
# number = (dic["public_repos"])  # number
# url = (dic["repos_url"])
# repos_url = requests.get(url)
# for i in range(0, number):
#     print(repos_url.json()[i]["html_url"])

#

# except KeyError:
#     print("Told you to enter valid username wtf")
# image = result.json()["avatar_url"]
# print(image)


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
