import discord
from discord.ext import commands


class Modmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        empty_array = []
        # ketuakelas
        modmail_channel = self.bot.get_channel(760157245173399637)
        if message.author == self.bot.user:
            return
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" + message.author.display_name + "]")
                for file in files:
                    await modmail_channel.send(file.url)
            else:
                await modmail_channel.send(
                    "[" + message.author.display_name + "] " + message.content
                )

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reply(self, ctx, user: discord.User, *, value):
        await user.send(f"{value}")
        await ctx.send("DM sent!")


def setup(bot):
    bot.add_cog(Modmail(bot))
