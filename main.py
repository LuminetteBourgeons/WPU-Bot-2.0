import discord
from discord.ext import commands, tasks
from discord.utils import get
import os, asyncio

#prefix titik koma :)
PREFIX = [
  "wpu; ",
  "wpu;",
  "; ",
  ";"
]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
  embed=discord.Embed(title="__*WPU bot's commands:*__", description="Prefix: `;`\n<:wpublack:723675025894539294> Develop by: \n<:discordpy:850714601527050251> Using discord.py <:python:778794123544887348>\n‎ ‎ ", colour=discord.Color.blurple())
  embed.set_thumbnail(url='https://www.webprogrammingunpas.com/assets/images/logo-wpu/logo-putih-polos.png')
  embed.add_field(name="__Github:__", value="https://github.com/LuminetteBourgeons/wpu-bot-2.0\n\n***List of Commands:***", inline=False)
  embed.add_field(name='<:wpublack:723675025894539294>__Fun:__', value="‎ ‎ ‎ ‎ ・*Rolling a dice:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ roll` / `+ dice`\n‎ ‎ ‎ ‎ ・*Flipping a coin:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ flip` / `+ coin`\n‎ ‎ ‎ ‎ ・*Rock, Paper, Scissors:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ rps`‎", inline=False)
  embed.add_field(name='<:wpublack:723675025894539294> __Informations:__', value="‎ ‎ ‎ ‎ ・*Userinfo:* shows you informations about a user\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ userinfo @user` / `+ userinfo`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Avatar:* shows you informations about a user's avatar\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ avatar @user` / `+ avatar`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Serverinfo:* shows you informations about the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ serverinfo`\n‎ ‎ ‎ ‎ ・*Servericon:* shows you the server icon\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ servericon`", inline=False)
  embed.add_field(name='<:wpublack:723675025894539294> __Miscellaneous:__', value="‎ ‎ ‎ ‎ ・*Help:* shows you this message\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ help`\n‎ ‎ ‎ ‎ ・*Calculate:* I'll count for you :3\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ calc <operation>` / `+ calculate <operation>`\n‎ ‎ ‎ ‎ ・*Picking out some choice:* I'll choose for you :3\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ choose <opt. 1>|<opt.2>|<opt.3>|<...>` /\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ pick <opt. 1>|<opt.2>|<opt.3>|<...>`\n‎ ‎ ‎ ‎ ・*Making regional texts:* simply turn `this` to 🇹 🇭 🇮 🇸\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ regional <text>`\n‎ ‎ ‎ ‎ ・*Reminder:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ reminder <time> <text>`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example:`+ reminder 50m Cookies are ready!`\n‎ ‎ ‎ ‎ ・*Ping:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ ping`", inline=False)
  embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
    channel = bot.get_channel(848750771323404318)
    await channel.send('Rebooting')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
    await asyncio.sleep(5)
    print('WPU is online.')
@bot.event
async def on_member_join(member):
    if member.guild.id == 786492151058923520:
        channel = bot.get_channel(848812370334711848)
        await channel.send("Halo, {}! Selamat datang di server discord **Web Programming Unpas**. Sebelumnya, silakan kunjungi <#850305113554026497> untuk membaca __Peraturan__, dan mengikuti instruksi selanjutnya. ".format (member.mention))
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    #ngasi prefix kalo ditag
    if bot.user.mentioned_in(message):
        await message.channel.send(f'My Prefix is `{bot.command_prefix}`')
        await bot.process_commands(message)
    #buat di channel 'selamat-datang'
    if message.channel.id == 745872171825627157: #id channel selamat-datang
        channel = bot.get_channel(745872171825627157)
        if message.content.lower() == 'Web Programming UNPAS':
          user = message.author
          role = get(user.guild.roles, name="Mahasiswa Baru")
          await user.add_roles(role)
          await message.delete()
          await channel.send(f"Terimakasih {message.author.mention}, sudah membaca peraturan. Silakan, dilanjutkan ke <#722024507707228160>!", delete_after=3)
          await bot.process_commands(message)
        else:
          await message.delete()
          await bot.process_commands(message)
    #verifikasi form
    if message.channel.id == 722024507707228160: #id channel perkenalan
        channel = bot.get_channel(722024507707228160)
        raw = message.content.split('\n')
        nama = ''
        asal = ''
        sekolah = ''
        kerja = ''
        tau = ''
        bahasa = ''
        hobby = ''
        for data in raw:
                    data = data.split('?')
                    if (data[0]).lower() == 'siapa nama kamu':
                        nama = data[1]
                    elif (data[0]).lower() == 'asal dari mana':
                        asal = data[1]
                    elif (data[0]).lower() == 'sekolah / kuliah di mana':
                        sekolah = data[1]
                    elif (data[0]).lower() == 'bekerja di mana':
                        kerja = data[1]
                    elif (data[0]).lower() == 'dari mana tau wpu':
                        tau = data[1]
                    elif (data[0]).lower() == 'bahasa pemrograman favorit':
                        bahasa = data[1]
                    elif (data[0]).lower() == 'hobby / interest':
                        hobby = data[1]
        if nama == '' or asal == '' or sekolah == '' or kerja == '' or tau == '' or bahasa == '' or hobby == '' :
            await message.add_reaction('\U0000274c')
            salah = await channel.send(f"{message.author.mention}, tolong masukkan data sesuai format!")
            await asyncio.sleep(5)
            await message.delete()
            await salah.delete()
            await bot.process_commands(message)
        else:
            await message.add_reaction('\U00002705')
            user = message.author
            role = get(user.guild.roles, name="Mahasiswa")
            await user.add_roles(role)
            await channel.send(f"Terimakasih {message.author.mention}, sudah perkenalan sesuai format. Salam kenal!")
            await bot.process_commands(message)

#ini buat ngeremind format formnya
@tasks.loop(minutes=20)
async def perkenalan():
    channel = bot.get_channel(722024507707228160) #id channel perkenalan
    embed=discord.Embed(title="Halo! Untuk perkenalan, bisa copy format dibawah ini ya!", description="```Siapa nama kamu?\nAsal dari mana?\nSekolah / Kuliah di mana?\nBekerja di mana?\nDari mana tau WPU?\nBahasa pemrograman favorit?\nHobby / Interest?```", colour=discord.Color.orange())
    await channel.send(embed=embed)
@perkenalan.before_loop
async def perkenalan_before():
  await bot.wait_until_ready()
@bot.command()
async def introstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    perkenalan.start()
    await ctx.send("Auto introduction reminder has started.")
  else:
    await ctx.send("You are not allowed to use this command!")
@bot.command()
async def introstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    perkenalan.cancel()
    await ctx.send("Auto introduction reminder has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")

extensions = [ 
  'cogs.miscellaneous', 
  'cogs.mod', 
  'cogs.reminder',  
  'cogs.info', 
  'cogs.fun'     
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
bot.run(os.getenv('TOKEN'))