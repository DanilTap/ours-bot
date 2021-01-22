# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands

bot = discord.ext.commands.Bot(command_prefix = "!")

# START

# Power
@bot.event
async def on_ready():
    print('I am power')# Допилить

# INFORMATION

# Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')

# Help
bot.remove_command('help')
@bot.command()
async def help(ctx):
	embed = discord.Embed(color = 0x537cda, description = f"\n**Информация**\n`!hello` - Приветствие.\n\n`!help` - Список моих команд.\n\n`!bot_info` - Информация обо мне.\n\n**Полезное**\n`!installer <Язык или файл> <Версия>` - Отправит указанный файл или даст ссылку на инсталлятор указанного языка программирования.\nНа данный момент доступны инсталляторы языка Python версий **2.0.1, 3.4.0, 3.5.0, 3.6.0, 3.7.0, 3.8.0, 3.9.1**.\n\n**Модерация**\n`!warn <Ник участника | @Упоминание | ID> <Причина>` - Выдаст предупреждение участнику без пинга, ни на что не влияет.\nКоманда доступна только модераторам.\n\n**Прочие**\n`!print <Текст>` - Команда выведет текст.\n\n`!ping <Ник участника | @Упоминание | ID> <std>` - Пинг указанного участника, не злоупотреблять коммандой!\n\nПредлагайте свои команды для меня в <#782893317226233857>.", title = 'Команды')
	await ctx.send(embed = embed)

# Bot info
@bot.command()
async def bot_info(ctx):
	embed = discord.Embed(color = 0x537cda, description = f"Меня разрабатывает <@677453905227022349>. У меня нет имени, но Вы пожете предложить его написав моему создателю или в канале <#782893317226233857>.\nЯ выполняю некоторые полезные команды, например я могу дать прямую ссылку на инсталлятор некоторых языков программирования или отправить файл, подробнее - `!help`.\nВы также можете вынести предложение о моем улучшении всё в том же канале <#782893317226233857>.", title = 'Обо мне')
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/774646187440865290/9201269a8a69a50df77376ccd376fc53.png?size=256")
	await ctx.send(embed = embed)

# MODERATION

# Warn
@bot.command()
async def warn(ctx, member: discord.Member, *, about: str):
		if member:
			embed = discord.Embed(color = 0x537cda, description = f'Учасмрапаретник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
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

# ALSO

# Print    Сделать чтобы выдавался текст в ()
@bot.command()
async def print(ctx, *, text):
    await ctx.send(f'{text}')

# Ping member
@bot.command()
async def ping(ctx, member: discord.Member, loop: str):
	if loop == "std":
		await ctx.channel.purge(limit=1)
		await ctx.send(f'{member.mention}')

	elif loop == "whileTrue":
		while True:
			await ctx.send(f'{member.mention}')

	else:
			await ctx.send('Ошибка в аргументе цикла!')

# SECRET

# Sc 0000001
@bot.command()
async def sc0000001(ctx):
	embed = discord.Embed(color = 0x537cda, description = f"Секретная команда", title = 'Секретная команда')
	await ctx.send(embed = embed)

bot.run('Nzc0NjQ2MTg3NDQwODY1Mjkw.X6azew.bFWlgkQ68W7sTFfT8PA-InZkG0I')