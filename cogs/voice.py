import asyncio

import discord
import nacl
from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.send("Connected!", delete_after=3)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await asyncio.sleep(1)
        await ctx.message.delete()
        await ctx.send("Disconnected!", delete_after=3)

    @commands.command()
    async def voicemute(self, ctx):  # ???
        voice_client = ctx.guild.voice_client
        if not voice_client:
            return
        channel = voice_client.channel
        await voice_client.main_ws.voice_state(ctx.guild.id, channel.id, self_mute=True)
        await ctx.send("Muted!", delete_after=3)


def setup(bot):
    bot.add_cog(Voice(bot))
