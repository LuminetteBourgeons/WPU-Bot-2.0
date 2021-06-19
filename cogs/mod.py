import discord
from discord.ext import commands
import json, asyncio

orange=discord.Colour.blurple()

#ubah nama bot jgn lupa

class Mod(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def embed(self, ctx):
    await ctx.message.delete()
    await ctx.send('Waiting for your JSON embed... `timeout in 60 seconds.`', delete_after=5)
    message = await self.bot.wait_for('message', timeout=60)
    try:
      f = json.loads(str(message.content))
      embed = discord.Embed.from_dict(f)
      await asyncio.sleep(2)
      await message.delete()
      await ctx.send(embed=embed)
    except json.JSONDecodeError:
      await message.delete()
      await ctx.send('JSON ERROR', delete_after=1)
      return

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setonline(self, ctx):
    await ctx.bot.change_presence(status=discord.Status.online)
    embed = discord.Embed(color=orange, title="Set WPU's status to",description='`Online`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setidle(self, ctx):
    await ctx.bot.change_presence(status=discord.Status.idle)
    embed = discord.Embed(color=orange, title="Set WPU's status to",description='`Idle`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setdnd(self, ctx):
    await ctx.bot.change_presence(status=discord.Status.dnd)
    embed = discord.Embed(color=orange, title="Set WPU's status to",description='`Do not disturb`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setinv(self, ctx):
    await ctx.bot.change_presence(status=discord.Status.invisible)
    embed = discord.Embed(color=orange, title="Set WPU's status to",description='`Invisible`')
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def actplaying(self, ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=name))
    embed = discord.Embed(color=orange,title="Set WPU's activity to",description=f'`playing {name}`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def actlistening(self, ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
    embed = discord.Embed(color=orange, title="Set WPU's activity to",description=f'`listening {name}`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def actwatching(self, ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    embed = discord.Embed(color=orange,title="Set WPU's activity to",description=f'`watching {name}`')
    await ctx.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def actcompeting(self, ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=name))
    embed = discord.Embed(color=orange, title="Set WPU's activity to",description=f'`competing in {name}`')
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def delete(self, ctx, limit=500, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
      limit = int(limit)
    except:
      return await ctx.send("Please pass in an integer as limit")
    if limit == 0:
      ctx.send("Please specify how much messages you want to purge!", delete_after=4)
      return
    if not member:
      await ctx.channel.purge(limit=limit)
      return await ctx.send(f"Deleted {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
      if len(msg) == limit:
          break
      if m.author == member:
          msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Deleted {limit} messages of {member.mention}", delete_after=3)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def dm(self,ctx, user: discord.User, *, value):
    await user.send(f"**{value}**")
    await user.send(f"||Sent by {ctx.author.name}||")
    await ctx.send("DM sent!")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def warn(self, ctx, member: discord.member, *, reason="Not specified"):
    if member is None:
      embed = discord.Embed(color=orange, title=f'{ctx.author.name}',description='Please specify the user you want to warn\n Use:`+warn @user`')
      await ctx.send(embed=embed)
    embed1 = discord.Embed(color=orange, title=f'{member}, you have been warned!', description=f'by {ctx.author.name}')
    embed1.add_field(name="Reason:", value=reason)
    await ctx.send(embed=embed1)
    channel = ctx.bot.get_channel(854589548864340009)
    embed2 = discord.Embed(color=orange, title=f'{member}, have been warned!', description=f'by {ctx.author.name}')
    embed2.add_field(name="Reason:", value=reason)
    embed2.add_field(name="Server:", value=f'{ctx.guild.name}')
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed2)
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="Not specified"):
    if member.guild_permissions.administrator:
      embed = discord.Embed(title="Error!",description="User is an Admin", color=discord.Colour.red())
      await ctx.send(embed=embed)
    else:
      try:
        await member.kick(reason=reason)
        embed = discord.Embed(title="User Kicked!",description=f"**{member}** was kicked by **{ctx.message.author}**!",color=orange)
        embed.add_field(name="Reason:", value=reason)
        await ctx.send(embed=embed)
        try:
          await member.send(f"You were kicked by **{ctx.message.author}**!\nReason: {reason}")
        except:
          pass
      except:
        embed = discord.Embed(title="Error!", description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",color=discord.Colour.red())
        await ctx.message.channel.send(embed=embed)
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="Not specified"):
    if member.guild_permissions.administrator:
      embed = discord.Embed(title="Error!",description="User is an Admin", color=discord.Colour.red())
      await ctx.send(embed=embed)
    else:
      try:
        await member.ban(reason=reason)
        embed = discord.Embed(title="User Banned!",description=f"**{member}** was banned by **{ctx.message.author}**!",color=orange)
        embed.add_field(name="Reason:", value=reason)
        await ctx.send(embed=embed)
        try:
          await member.send(f"You were banned by **{ctx.message.author}**!\nReason: {reason}")
        except:
          pass
      except:
        embed = discord.Embed(title="Error!", description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to kick.",color=discord.Colour.red())
        await ctx.message.channel.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member: discord.Member):
    if member.guild.id == 775568951101882398:
      role = discord.utils.get(ctx.guild.roles, name="🤫 Shh, MUTED!")
      await member.add_roles(role)
      await ctx.send(f"Muted {member} >:D")
    else:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"Muted {member} >:D")
      else:
        await member.add_roles(role) 
        await ctx.send(f"Muted {member} >:D")
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unmute(self, ctx, member: discord.Member):
    if member.guild.id == 775568951101882398:
      role = discord.utils.get(ctx.guild.roles, name="🤫 Shh, MUTED!")
      await member.remove_roles(role)
      await ctx.send(f"Unmuted {member}")
    else:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.remove_roles(role)
        await ctx.send(f"Unmuted {member}")
      else:
        await member.remove_roles(role) 
        await ctx.send(f"Unmuted {member}")

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  async def nick(self, ctx, member: discord.Member, *, nickname=None):
    try:
      await member.edit(nick=nickname)
      embed = discord.Embed(title="Changed Nickname!", description=f"**{member}'s** new nickname is **{nickname}**!", color=orange)
      await ctx.send(embed=embed)
    except:
      embed = discord.Embed(title="Error!", description="An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.", color=orange)
      await ctx.message.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Mod(bot))
