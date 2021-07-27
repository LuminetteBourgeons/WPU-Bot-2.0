import discord
from discord.ext import commands

orange = discord.Colour.blurple()


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(
            title=f"{user.name}'s avatar.", url=f"{user.avatar_url}", colour=orange
        )
        embed.set_image(url=user.avatar_url)
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        name = f"{user.name}"
        nick = f"{user.nick}"
        if nick is None:
            nick = name
        id = f"`{user.id}`"
        status = f"`{user.status}`"
        voice_state = None if not user.voice else user.voice.channel
        voice = f"`{voice_state}`"
        activity = f"{user.activity}"
        toprole = f"{user.top_role.name}"
        if toprole == "@everyone":
            toprole = "None"
        roles = " ".join([r.mention for r in user.roles][1:])
        avatar = f"{user.avatar_url}"
        embed = discord.Embed(title=name + "'s Informations", color=orange)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User Nickname", value=nick, inline=True)
        embed.add_field(name="User ID", value=id, inline=True)
        embed.add_field(name="Status", value=status, inline=True)
        embed.add_field(name="In Voice", value=voice, inline=False)
        embed.add_field(name="Custom Status", value=activity, inline=False)
        embed.add_field(name=f"Roles ({len(user.roles)-1})", value=roles, inline=False)
        embed.add_field(name="Highest Role", value=toprole, inline=False)
        embed.add_field(
            name="Account Created",
            value=user.created_at.__format__("%A, %d. %B %Y @ %H:%M:%S"),
            inline=True,
        )
        embed.add_field(
            name="Join Date",
            value=user.joined_at.__format__("%A, %d. %B %Y @ %H:%M:%S"),
            inline=True,
        )
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["perms"])
    async def permissions(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        avatar = f"{user.avatar_url}"
        perms = "`,\n `".join(
            [
                str(p[0]).replace("_", " ").title()
                for p in user.guild_permissions
                if p[1]
            ]
        )
        embed = discord.Embed(
            title=f"{user.name}" + "'s Permissions",
            description=f"`{perms}`",
            color=orange,
        )
        embed.set_thumbnail(url=avatar)
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(
            title=f"{ctx.guild.name} server icon.",
            url=f"{ctx.guild.icon_url}",
            colour=orange,
        )
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        name = f"{ctx.guild.name}"
        owner = f"<@{ctx.guild.owner_id}>"
        id = f"`{ctx.guild.id}`"
        icon = f"{ctx.guild.icon_url}"
        categories = f"{len(ctx.guild.categories)}"
        channels = f"{len(ctx.guild.channels)}"
        text_channels = f"{len(ctx.guild.text_channels)}"
        voice_channels = f"{len(ctx.guild.voice_channels)}"
        total_member = f"`{ctx.guild.member_count}`"
        online_members = f"{sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)}"
        offline_members = f"{sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)}"
        humans = f"{sum(not member.bot for member in ctx.guild.members)}"
        bots = f"{sum(member.bot for member in ctx.guild.members)}"
        roles = f"`{len(ctx.guild.roles)}`"
        boost_level = f"{ctx.guild.premium_tier}"
        total_boosts = f"{ctx.guild.premium_subscription_count}"
        time = str(ctx.guild.created_at)
        time = time.split(" ")
        time = time[0]
        embed = discord.Embed(title=name + " Server Informations", color=orange)
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Server Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="‎", value="‎", inline=True)
        embed.add_field(
            name="Members Informations:",
            value=f"All members: `{total_member}`\nMembers: `{humans}`\nBots: `{bots}`\nOnline members: `{online_members}`\nOffline members: `{offline_members}`",
            inline=True,
        )
        embed.add_field(
            name="Server Informations:",
            value=f"Total roles: `{roles}`\nCategories: `{categories}`\nTotal channels: `{channels}`\nText channels: `{text_channels}`\nVoice channels: `{voice_channels}`\nBoost level: `{boost_level}`\nTotal boost: `{total_boosts}`\nServer created at: {time}",
            inline=True,
        )
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["role"])
    async def roleinfo(self, ctx, *, role: discord.Role):
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(role_created, since_created)
        members = ""
        i = 0
        for user in role.members:
            members += f"{user.name}, "
            i += 1
            if i > 30:
                break
        embed = discord.Embed(colour=orange)
        embed.set_author(name=role.name)
        embed.add_field(name="Users", value=len(role.members))
        embed.add_field(name="Mentionable", value=role.mentionable)
        embed.add_field(name="Hoist", value=role.hoist)
        embed.add_field(name="Position", value=role.position)
        embed.add_field(name="Managed", value=role.managed)
        embed.add_field(name="Colour", value=role.colour)
        embed.add_field(name="Creation Date", value=created_on)
        embed.add_field(name="Members", value=members[:-2], inline=False)
        embed.add_field(name=f"Role ID", value=f"{role.id}", inline=False)
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["channel"])
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.message.channel
        embed = discord.Embed(color=orange, description=channel.mention)
        embed.add_field(name="Name", value=channel.name)
        embed.add_field(name="Server", value=channel.guild)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Category ID", value=channel.category_id)
        embed.add_field(name="Position", value=channel.position)
        embed.add_field(name="NSFW", value=str(channel.is_nsfw()))
        embed.add_field(name="Members (cached)", value=str(len(channel.members)))
        embed.add_field(name="Category", value=channel.category)
        embed.add_field(
            name="Created", value=channel.created_at.strftime("%d %b %Y %H:%M")
        )
        embed.set_footer(
            text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
