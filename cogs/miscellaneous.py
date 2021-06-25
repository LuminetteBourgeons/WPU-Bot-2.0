import discord
from discord.ext import commands
import random, time
import aiohttp
import json

#dibawah ada ubah warna embed

class Misc(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.regionals = {
      'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 
      'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
      'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
      'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 
      'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
      'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
      'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 
      'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
      'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
      'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 
      'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
      'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
      'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 
      'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
      'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
      'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 
      'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
      'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
      's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 
      't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
      'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
      'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 
      'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
      'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
      'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 
      'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
      '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
      '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', 
      '8': '8⃣', '9': '9⃣', '!': '\u2757', '?': '\u2753'
      }
    
  @commands.command(aliases=['calc'])
  async def calculate(self, ctx, *, q):
    await ctx.send(f"{q}={eval(q)}")

  @commands.command(aliases=['pick'])
  async def choose(self, ctx, *, choices: str):
    await ctx.send('I choose: {}'.format(random.choice(choices.split("|"))))
  
  @commands.command()
  async def regional(self,ctx, *, msg):
    await ctx.message.delete()
    msg = list(msg)
    regional_list = [self.regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
    regional_output = '\u200b'.join(regional_list)
    await ctx.send(regional_output)
    
  @commands.command()
  async def ping(self, ctx):
    before = time.monotonic()
    message = await ctx.send("🏓 Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 Pong!  `{int(ping)}ms`")

  @commands.command()
  async def poll(self, ctx, *, title):
    embed = discord.Embed(title="A new poll has been created!", description=f"{title}", color=discord.Colour.blurple())
    embed.set_footer(text=f"Poll created by: {ctx.message.author} • React to vote!")
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

    #ga penting tp yauda la ya wkwk
  @commands.command(name="bitcoin")
  async def bitcoin(self, ctx):
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    async with aiohttp.ClientSession() as session:
      raw_response = await session.get(url)
      response = await raw_response.text()
      response = json.loads(response)
      embed = discord.Embed(title=":information_source: Info",description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}", color=discord.Colour.blurple())
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Misc(bot))
