# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands
import asyncio
import uuid
import random

bot = discord.ext.commands.Bot(command_prefix = "!")

# Power
@bot.event
async def on_ready():
	print("Bot is ready!")
	activity = discord.Game(name="!help", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)


# INFORMATION

# Help
bot.remove_command('help')
@bot.command()
async def help(ctx):
	embed = discord.Embed(title = 'Команды:', color = 0x326cfc, description = f"\n**Информация**\n`!help` `!chelp` `!bot_info`\n\n**Модерация**\n`!ban` `!unban` `!kick` `!mute` `!unmute` `!warn`\n`!sendmember` `!sendchannel`\n\n**Прочие**\n`!randid` `!randnum` `!setstats`\n`!print` `!hello`\n\nСекретные: `1`")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809274410049339452/816321656238768219/Screenshot_4.png")
	embed.set_footer(text="15 команд | Подробнее о командах - !chelp <команда без !>")
	await ctx.send(embed = embed)

# Chelp
@bot.command()
async def chelp(ctx, command):
	if command == 'ban':
		embed = discord.Embed(title = '!ban', color = 0x326cfc, description = f"Синтаксис:\n`!ban <Участник | @Участник | ID> <Причина>`\nЗабанит участника на сервере.")
		await ctx.send(embed = embed)

	if command == 'unban':
		embed = discord.Embed(title = '!unban', color = 0x326cfc, description = f"Синтаксис:\n`!unban <Участник | @Участник | ID>`\nРазбанит участника на сервере.")
		await ctx.send(embed = embed)

	elif command == 'kick':
		embed = discord.Embed(title = '!kick', color = 0x326cfc, description = f"Синтаксис:\n`!kick <Участник | @Участник | ID> <Причина>`\nВыгонит участника с сервера.")
		await ctx.send(embed = embed)

	elif command == 'mute':
		embed = discord.Embed(title = '!mute', color = 0x326cfc, description = f"Синтаксис:\n`!mute <Участник | @Участник | ID> <Время в минутах> <Причина>`\nЗапретит участнику писать в каналах(выдаст роль MUTED).")
		await ctx.send(embed = embed)

	elif command == 'unmute':
		embed = discord.Embed(title = '!unmute', color = 0x326cfc, description = f"Синтаксис:\n`!unmute <Участник | @Участник | ID>`\nРазмьютит участника.")
		await ctx.send(embed = embed)

	elif command == 'warn':
		embed = discord.Embed(title = '!warn', color = 0x326cfc, description = f"Синтаксис:\n`!warn <Участник | @Участник | ID> <Причина>`\nВыдаст предупреждение участнику(Сообщение в чате).")
		await ctx.send(embed = embed)

	elif command == 'sendmember':
		embed = discord.Embed(title = '!sendmember', color = 0x326cfc, description = f"Синтаксис:\n`!sendmember <Участник | @Участник | ID> <Сообщение>`\nОтправит сообщение участнику в личный чат(только для модерации).")
		await ctx.send(embed = embed)

	elif command == 'sendchannel':
		embed = discord.Embed(title = '!sendchannel', color = 0x326cfc, description = f"Синтаксис:\n`!sendchannel <Канал | @Канал | ID> <Сообщение>`\nОтправит сообщение в указаный канал(только для модерации).")
		await ctx.send(embed = embed)

	elif command == 'chelp':
		embed = discord.Embed(title = 'Гениально', color = 0x326cfc)
		await ctx.send(embed = embed)

	elif command == 'randnum':
		embed = discord.Embed(title = '!randnum', color = 0x326cfc, description = f"Синтаксис:\n`!randnum <От> <До>`\nОтправит случайное число от первого и второго указанных.")
		await ctx.send(embed = embed)

	elif command == 'randid':
		embed = discord.Embed(title = '!randid', color = 0x326cfc, description = f"Синтаксис:\n`!randid`\nСгенерирует случайный id в 128 бит.")
		await ctx.send(embed = embed)

	elif command == 'setstats':
		embed = discord.Embed(title = '!setstats', color = 0x326cfc, description = f"Синтаксис:\n`!setstats <Статус>`\nСменит статус бота.")
		await ctx.send(embed = embed)

	elif command == 'hello':
		embed = discord.Embed(title = '!hello', color = 0x326cfc, description = f"Синтаксис:\n`!hello`\n:)")
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0x326cfc, description = f"Такой команды не существует.")
		await ctx.send(embed = embed)

# Bot info
@bot.command()
async def bot_info(ctx):
	embed = discord.Embed(title = 'Обо мне', color = 0x326cfc, description = f"Мой репозиторий на GitHub:\n`https://github.com/Innokentie/ours-bot`.")
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/774646187440865290/643380e6d2dd7bbbe0aaae4c2815382c.png?size=256")
	embed.set_footer(text = "Innokentie12")
	await ctx.send(embed = embed)


# MODERATION

# Ban
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def ban(ctx, member: discord.Member, *, about: str):
	if member:
		await member.ban()
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был забанен **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Unban
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def unban(ctx, member: discord.Member, *, about: str):
	if member:
		await member.unban()
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был разбанен **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Kick
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def kick(ctx, member: discord.Member, *, about: str):
	if member:
		await member.kick()
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был кикнут **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Mute
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def mute(ctx, member: discord.Member, time: int, *, about: str):
	if member:
		getrole = discord.utils.get(ctx.guild.roles, id = 808691502191738891)
		await member.add_roles(getrole)
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был замьючен **{ctx.message.author.name}** на {time} минут по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)
		await asyncio.sleep(time*60)
		await member.remove_roles(getrole)
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был размьючен спустя {time} минут')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Unmute
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def unmute(ctx, member: discord.Member):
	if member:
		getrole = discord.utils.get(ctx.guild.roles, id = 808691502191738891)
		await member.remove_roles(getrole)
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был размьючен **{ctx.message.author.name}**.')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Warn
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def warn(ctx, member: discord.Member, *, about: str):
	if member:
		embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0xed0c0c, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Member send
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def sendmember(ctx, member: discord.Member, *, text):
	embed = discord.Embed(color = 0x326cfc, description = f"{text}")
	await member.send(embed = embed)
	embed = discord.Embed(color = 0x326cfc, description = f"{ctx.message.author.name} Ваше сообщение было доставлено участнику {member.name}.",)
	await ctx.send(embed = embed)

# Channel send
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def sendchannel(ctx, channel: int, *, text):
	channelm = bot.get_channel(channel)
	await channelm.send(f'{text}')
	embed = discord.Embed(color = 0x326cfc, description = f"{ctx.message.author.name} Ваше сообщение было доставлено.",)
	await ctx.send(embed = embed)


# ALSO

# Print
@bot.command()
async def print(ctx, *, text):
	await ctx.channel.purge(limit=1)
	await ctx.send(f'{text}')

# Randid
@bot.command()
async def randid(ctx):
	embed = discord.Embed(color = 0x326cfc, description = f"{uuid.uuid4()}")
	await ctx.send(embed = embed)

# Randnum
@bot.command()
async def randnum(ctx, numone: int, numtwo: int):
	randnumber = random.randrange(numone, numtwo)
	embed = discord.Embed(color = 0x326cfc, description = f"{randnumber}")
	await ctx.send(embed = embed)

# Embedc
@bot.command()
async def embedc(ctx, color: discord.Colour, title, *, des):
	await ctx.send(f'Код:\n```python\nembed = discord.Embed(title = "{title}", color = {color}, description = f"{des}")\nawait ctx.send(embed = embed)\n```')
	embed = discord.Embed(title = f'{title}', color = color, description = f"{des}")
	await ctx.send(embed = embed)


# Set stats
@bot.command()
async def setstats(ctx, *, stats: str):
	activity = discord.Game(name=stats, type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)
	await ctx.message.add_reaction('✅')
	await asyncio.sleep(100)
	activity = discord.Game(name="!help", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)


# Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')


# SECRET

# You hacker

bot.run('token_HaCkEr')
