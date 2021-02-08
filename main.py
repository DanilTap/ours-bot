# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands

bot = discord.ext.commands.Bot(command_prefix = "!")

# START

# Power
@bot.event
async def on_ready():
    activity = discord.Game(name="!help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

# INFORMATION

# Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')

# Help
bot.remove_command('help')
@bot.command()
async def help(ctx):
	embed = discord.Embed(color = 0x537cda, description = f"\n**Информация**\n`!help` - Список моих команд.\n`!bot_info` - Информация обо мне.\n\n**Полезное**\n`!installer <Язык или файл> <Версия>` - Отправит указанный\nфайл или даст ссылку на инсталлятор указанного языка программирования.\nСейчас доступны инсталляторы языка Python\nверсий 2.0.1, 3.4.0, 3.5.0, 3.6.0, 3.7.0, 3.8.0, 3.9.1.\n\n**Модерация**\n`!ban <Участник | @Участник | ID> <Причина>` - Забанит участника на сервере.\n`!kick <Участник | @Участник | ID> <Причина>` - Выгонит\nучастника с сервера.\n`!warn <Участник | @Участник | ID> <Причина>` - Отправит в канал сообщение с предупреждением участнику.\n\n**Прочие**\n`!hello` - Сообщение с приветствием :)\n`!print <Текст>` - Команда отправит указаный текст\nи удалит сообщение с командой.", title = 'Команды')
	await ctx.send(embed = embed)

# Bot info
@bot.command()
async def bot_info(ctx):
	embed = discord.Embed(color = 0x537cda, description = f"Мой создатель - <@677453905227022349>.\nВы можете предложить имя для меня написав моему создателю или в канале <#782893317226233857>.\n\nУ меня открытый исходный код, вот мой репозиторий на Git Hub:\n`https://github.com/Innokentie/ours-bot`.", title = 'Обо мне')
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/774646187440865290/643380e6d2dd7bbbe0aaae4c2815382c.png?size=256")
	await ctx.send(embed = embed)

# MODERATION

# Ban
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def ban(ctx, member: discord.Member, *, about: str):
	if member:
		await member.ban()
		embed = discord.Embed(color = 0x537cda, description = f'Участник **{member.name}** был забанен **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)


# Kick
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def kick(ctx, member: discord.Member, *, about: str):
	if member:
		await member.kick()
		embed = discord.Embed(color = 0x537cda, description = f'Участник **{member.name}** был кикнут **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
		await ctx.send(embed = embed)

# Warn
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def warn(ctx, member: discord.Member, *, about: str):
		if member:
			embed = discord.Embed(color = 0x537cda, description = f'Участник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
			await ctx.send(embed = embed)
		else:
			embed = discord.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
			await ctx.send(embed = embed)

# USEFUL

# Installers
@bot.command()
async def installer(ctx, name, version):
	if name == 'python' and version == '2.1.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 2.1.0** Windows Installer - https://www.python.org/ftp/python/2.0.1/Python-2.0.1.exe')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.4.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.4.0** Windows Installer - https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.5.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.5.0** Windows Installer - https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.6.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.6.0** Windows Installer - https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.7.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.7.0** Windows Installer - https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.8.0':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.8.0** Windows Installer - https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi')
		await ctx.send(embed = embed)

	elif name == 'python' and version == '3.9.1':
		embed = discord.Embed(color = 0x537cda, description = f'**Python 3.8.0** Windows Installer - https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe')
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(color = 0x537cda, description = f'Ошибка в аргументах команды\nили в моей БД нет данных файлов.', title = 'Ошибка!')
		await ctx.send(embed = embed)

# Vote
@bot.command()
async def vote(ctx):
	
	embed = discord.Embed(color = 0x537cda, description = f'**{question}**\n\n{varone}\n{vartwo}\n{varthree}\n{varfour}', title = '')
	await ctx.send(embed = embed)

# ALSO

# Print
@bot.command()
async def print(ctx, *, text):
	await ctx.channel.purge(limit=1)
	await ctx.send(f'{text}')

# SECRET

# Hehe, hacker

bot.run('token')
