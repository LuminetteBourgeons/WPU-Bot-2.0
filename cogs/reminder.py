import discord
from discord.ext import commands
import asyncio

class Reminder(commands.Cog):
    def __init__(self,bot):
      self.bot=bot
    
    @commands.command()
    async def reminder(self, ctx, time, *, reminder):
        embed = discord.Embed(color=discord.Colour.orange())
        seconds = 0
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} day(s)"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hour(s)"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minute(s)"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} second(s)"
        if seconds == 0:
            embed.add_field(name='Warning',
                            value='Please specify a proper duration :(')
        elif seconds > 7776000:
            embed.add_field(
                name='Warning',
                value=
                'You have specified a too long duration!\nMaximum duration is 90 days.'
            )
        else:
            await ctx.send(
                f"Alright, I will remind you about {reminder} in {counter}.")
            await asyncio.sleep(seconds)
            await ctx.author.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
            return
        await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Reminder(bot))

