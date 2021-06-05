import discord
from discord.ext import commands
import random, asyncio

class Fun(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command(aliases=['roll'])
  async def dice(self, ctx):
    dice6=["1","2","3","4","5","6"]
    await ctx.send("Rolling the dice~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"<:wpublack:723675025894539294> Rolled a dice! 🎲", description=f"It landed on {random.choice(dice6)}!",colour=discord.Color.orange())
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['flip'])
  async def coin(self, ctx):
    coin2=["head","tail"]
    childe=[
      "Well, I'd choose head though...",
      "Well, I'd choose tail though...",
      "Do you believe on that?",
      "",
      "",
      "",
      "And you landed on my heart ;)"]
    await ctx.send("Flipping the coin~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"<:wpublack:723675025894539294> Flipped a coin! 🪙", description=f"It landed on {random.choice(coin2)}. {random.choice(childe)}",colour=discord.Color.orange())
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def rps(self, ctx):
    rps = ['rock', 'paper', 'scissors']
    await ctx.send(f"Let's play rock, paper, scissors with me \nSo rock, paper, or scissors? Choose wisely...")
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rps
    user_choice = (await self.bot.wait_for('message', check=check)).content.lower()
    comp_choice = random.choice(rps)
    if user_choice == 'rock':
      if comp_choice == 'rock':
        await ctx.send(f'Well, that was weird. We tied...\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Nice try\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Aw, you beat me. It won't happen again!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    elif user_choice == 'paper':
      if comp_choice == 'rock':
        await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Aw man, you actually managed to beat me.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    elif user_choice == 'scissors':
      if comp_choice == 'rock':
        await ctx.send(f'HAHA!! I JUST CRUSHED YOU!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Hmph, nice one.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Oh well, we tied.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    else:
      await ctx.send(f"Uh, I told you to choose rock, paper, or scissors...")

def setup(bot):
  bot.add_cog(Fun(bot))