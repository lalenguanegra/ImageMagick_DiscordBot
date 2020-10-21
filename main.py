import requests 
import shutil 
import discord
import sys
import subprocess 
from subprocess import call
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.command()
async def im(ctx, args):
    await ctx.send("Photo Added!")
    userInput = ' '.join(args)
    image_url = args
    filename = "1.jpg"

    r = requests.get(image_url, stream = True)


    if r.status_code == 200:
        r.raw.decode_content = True
    
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        


@bot.command()
async def cap(ctx, *args):
  await ctx.send("Caption Added")
  shutil.copyfile('default.txt', 'file.bat')
  userInput = ' '.join(args)
  with open("file.bat") as f:
      string = str(userInput)
      newText=f.read().replace("ayylmao", string)
  with open("file.bat", "w") as f:
      f.write(newText)

@bot.command()
async def go(ctx):
      await ctx.send("Please Wait...")
      subprocess.call(['file.bat'], shell=False)
      await ctx.message.channel.send(file=discord.File('photo.jpg'))
    


bot.run('token')
