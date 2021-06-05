import discord
from discord.ext import commands

class Info(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def avatar(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    embed = discord.Embed(title=f'{user.name}\'s avatar.',url=f"{user.avatar_url}",colour=discord.Colour.orange())
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def userinfo(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    name = f'{user.name}'
    nick = f'{user.nick}'
    if nick is None:
      nick = name
    id = f'`{user.id}`'
    status = f'`{user.status}`' 
    voice_state = None if not user.voice else user.voice.channel
    voice = f'`{voice_state}`'
    activity = f'`{user.activity}`'
    role = f'{user.top_role.name}'
    if role == "@everyone":
      role = "None"
    icon = f'{user.avatar_url}'
    embed = discord.Embed(title=name + "'s Information", color = discord.Color.orange())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="User Nickname", value=nick, inline=True)
    embed.add_field(name="User ID", value=id, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="In Voice", value=voice, inline=True)
    embed.add_field(name="In Activity", value=activity, inline=True)
    embed.add_field(name="Highest Role", value=role, inline=True)
    embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    await ctx.send(embed=embed)

  @commands.command()
  async def servericon(self, ctx):
    embed = discord.Embed(title=f'{ctx.guild.name} server icon.',url=f"{ctx.guild.icon_url}",colour=discord.Colour.orange())
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def serverinfo(self, ctx):
    name = f'{ctx.guild.name}'
    owner = f'<@{ctx.guild.owner_id}>'
    id = f'`{ctx.guild.id}`'
    region = f'`{ctx.guild.region}`'
    memberCount = f'`{ctx.guild.member_count}`'
    icon = f'{ctx.guild.icon_url}'
    embed = discord.Embed(title=name + " Server Information", color = discord.Color.orange())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Server Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Info(bot))