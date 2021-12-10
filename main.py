# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands
import asyncio
import uuid
import random 
import json

intents = discord.Intents.default()
intents.members = True
bot = discord.ext.commands.Bot(command_prefix = "!", intents = intents)

# EVENTS
# Start
@bot.event
async def on_ready():
	print("Bot is ready!")
	activity = discord.Game(name="!help", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)


# Welcome
@bot.event
async def on_member_join(member):
	channel = bot.get_channel(898104718293884988)
	await channel.send(f'**{member.mention}, Добро пожаловать на сервер Programming | PySider | RU! :wave:**\nРекомендуем ознакомиться с основной информацией о сервере в канале <#898105144372244501>, а также с правилами сервера - <#779376759065411624>.\n\n<@677453905227022349>')

# Buy
@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(898104747322642472)
	await channel.send(f'Наш сервер покидает `{member}`.\n\n<@677453905227022349>')

# Get roles
@bot.event
async def on_raw_reaction_add(payload):
	guild = bot.get_guild(payload.guild_id)
	member_id = payload.user_id
	member = guild.get_member(member_id)
	message_id = payload.message_id

	if payload.user_id == bot.user.id:
		return

	if message_id == 898159645380714545:
		if payload.emoji.name == "🔃":
			getrole = discord.utils.get(guild.roles, id = 790690635329962075)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🥘":
			getrole = discord.utils.get(guild.roles, id = 898160482073079808)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🐍":
			getrole = discord.utils.get(guild.roles, id = 790690334447108137)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🇯":
			getrole = discord.utils.get(guild.roles, id = 790690520733188196)
			await member.add_roles(getrole)

		elif payload.emoji.name == "👶":
			getrole = discord.utils.get(guild.roles, id = 800013291853709332)
			await member.add_roles(getrole)

		elif payload.emoji.name == "💵":
			getrole = discord.utils.get(guild.roles, id = 800413130244096033)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🧱":
			getrole = discord.utils.get(guild.roles, id = 800410934404710421)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🅿️":
			getrole = discord.utils.get(guild.roles, id = 790690860873809920)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🧮":
			getrole = discord.utils.get(guild.roles, id = 855392977555947530)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🥖":
			getrole = discord.utils.get(guild.roles, id = 798881583850455091)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🥔":
			getrole = discord.utils.get(guild.roles, id = 798881351611711502)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🎞️":
			getrole = discord.utils.get(guild.roles, id = 800408491297996840)
			await member.add_roles(getrole)

		elif payload.emoji.name == "📷":
			getrole = discord.utils.get(guild.roles, id = 790691619971792896)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🐟":
			getrole = discord.utils.get(guild.roles, id = 790691478070493244)
			await member.add_roles(getrole)

		elif payload.emoji.name == "🖥️":
			getrole = discord.utils.get(guild.roles, id = 790691158216278016)
			await member.add_roles(getrole)


	else:
		if payload.emoji.name == "🍪":
			with open('bot_constants.json','r', encoding='utf-8') as f:
				const = json.load(f)

			cookies = const["cookies"]

			if not member.name in cookies:
				mcookies = 0
				const["cookies"] = {f'{member.name}': 1}
				channel = bot.get_channel(payload.channel_id)
				message = await channel.fetch_message(message_id)

				await message.add_reaction('1️⃣')


			else:
				mcookies = 0
				for i in cookies.items():
					if member.name == i[0]:
						mcookies = i[1]

				tc = mcookies + 1

				const["cookies"] = {f'{member.name}': tc}

				channel = bot.get_channel(payload.channel_id)
				message = await channel.fetch_message(message_id)

				if tc == 2:
					await message.add_reaction('2️⃣')

				elif tc == 3:
					await message.add_reaction('3️⃣')

				elif tc == 4:
					await message.add_reaction('4️⃣')

				elif tc == 5:
					await message.add_reaction('5️⃣')

				elif tc == 6:
					await message.add_reaction('6️⃣')

				elif tc == 7:
					await message.add_reaction('7️⃣')

				elif tc == 8:
					await message.add_reaction('8️⃣')

				elif tc == 9:
					await message.add_reaction('9️⃣')

				elif tc == 10:
					await message.add_reaction('1️⃣0️⃣')

				elif tc >= 10:
					await message.add_reaction('1️⃣0️⃣➕')

			with open('bot_constants.json','w') as f:
				json.dump(const,f)



# METHODS




# COMMANDS
# Information
# Help
bot.remove_command('help')
@bot.command()
async def help(ctx, command=None):
	if command == None:
		embed = discord.Embed(title = 'Мои команды:', color = 0x326cfc, description = "\n**Информация**\n`!help` `!info`\n\n**Модерация**\n`!ban` `!unban` `!kick` `!mute` `!unmute`\n`!sendmember` `!sendchannel`\n\n**Прочие**\n`!embedc` `!randid` `!randnum` `!setstats`\n`!print` `!hello`\n\n*Секретные: `1`*")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809274410049339452/816321656238768219/Screenshot_4.png")
		embed.set_footer(text="17 команд | Подробнее о командах - !help <команда>")
		await ctx.send(embed = embed)

	elif command != None:
		embed = discord.Embed()

		if command == "help" or command == "!help":
			embed = discord.Embed(title = '!help <команда>', color = 0x326cfc, description = "Используйте эту команду с аргументом в виде названия команды для получения подробной информации о ней.")

		elif command == "!info" or command == "!info":
			embed = discord.Embed(title = '!info', color = 0x326cfc, description = "Краткая информация о боте.")

		elif command == "ban" or command == "!ban":
			embed = discord.Embed(title = '!ban <Участник> <Причина>', color = 0x326cfc, description = "Бан участника на сервере")

		elif command == "unban" or command == "!unban":
			embed = discord.Embed(title = '!unban', color = 0x326cfc, description = "Разбан участника на сервере")

		elif command == "mute" or command == "!mute":
			embed = discord.Embed(title = '!mute <Участник> <Время(мин)> <Причина>', color = 0x326cfc, description = "Мьют участника на сервере, блокировка доступа к текстовым каналом и последующее ее снятие по окончанию времени мьюта.")

		elif command == "unmute" or command == "!unmute":
			embed = discord.Embed(title = '!unmute', color = 0x326cfc, description = "Снятие мьюта с участника.")

		elif command == "kick" or command == "!kick":
			embed = discord.Embed(title = '!kick <Участник> <Причина>', color = 0x326cfc, description = "Кик участника с сервера.")

		elif command == "sendmember" or command == "!sendmember":
			embed = discord.Embed(title = '!sendmember', color = 0x326cfc, description = "")

		elif command == "sendchannel" or command == "!sendchannel":
			embed = discord.Embed(title = '!sendchannel', color = 0x326cfc, description = "")

		elif command == "embedc" or command == "!embedc":
			embed = discord.Embed(title = '!embedc <Цвет(HEX)> <Заголовок> <Текст>', color = 0x326cfc, description = "Создание простого Discord embed для discord.py с указанными аргументами.")

		elif command == "setstats" or command == "!setstats":
			embed = discord.Embed(title = '!setstats <Текст>', color = 0x326cfc, description = "Смена статуса бота на 120 секунд.")

		elif command == "randid" or command == "!randid":
			embed = discord.Embed(title = '!randid', color = 0x326cfc, description = "Генерация случайного ID.")

		elif command == "randnum" or command == "!randnum":
			embed = discord.Embed(title = '!randnum <От> <До>', color = 0x326cfc, description = "Генерация случайного числа.")

		elif command == "print" or command == "!print":
			embed = discord.Embed(title = '!print <Текст>', color = 0x326cfc, description = "Отправка текста ботом.")

		elif command == "hello" or command == "!hello":
			embed = discord.Embed(title = '!hello', color = 0x326cfc, description = "Здравствуйте!")

		elif command == "array" or command == "!array":
			embed = discord.Embed(title = '!array <Действие> || <Параметры>', color = 0x326cfc, description = "Работа с пользовательским массивом.\n\n**Аргументы**\nКоманда без аргументов выводит весь массив\n`add` - Добавляет элемент в массив.\n`pop <индекс>` - Удаление элемента с индексом n\n`clear` - Очистка массива.\n`max` - Сортировка массива по длинне или размеру числа.")

		else:
			embed = "Команда не была найдена."

		await ctx.send(embed = embed)

# Info
@bot.command()
async def info(ctx):
	embed = discord.Embed(title = 'Обо мне', color = 0x326cfc, description = f"Подробную информацию обо мне можно получить [здесь](https://discord.com/channels/775520099112189974/782877918208065596/898092325400641546).\n\nМой репозиторий на GitHub:\n`https://github.com/Innokentie/ours-bot`.")
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/774646187440865290/643380e6d2dd7bbbe0aaae4c2815382c.png?size=256")
	embed.set_footer(text = "HTTPs")
	await ctx.send(embed = embed)


# Moderation
# Ban
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def ban(ctx, member: discord.Member, *, about: str):
	await member.ban()
	await ctx.message.add_reaction('✅')

# Unban
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def unban(ctx, member: discord.Member, *, about: str):
	await member.unban()
	await ctx.message.add_reaction('✅')

# Kick
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def kick(ctx, member: discord.Member, *, about: str):
	await member.kick()
	await ctx.message.add_reaction('✅')

# Mute
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def mute(ctx, member: discord.Member, time: int, *, about: str):
	getrole = discord.utils.get(ctx.guild.roles, id = 808691502191738891)
	await member.add_roles(getrole)
	await ctx.message.add_reaction('✅')
	await asyncio.sleep(time*60)
	await member.remove_roles(getrole)
	embed = discord.Embed(color = 0x326cfc, description = f'Участник **{member.name}** был размьючен спустя {time} минут')
	await ctx.send(embed = embed)

# Unmute
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def unmute(ctx, member: discord.Member):
	getrole = discord.utils.get(ctx.guild.roles, id = 808691502191738891)
	await member.remove_roles(getrole)
	await ctx.message.add_reaction('✅')


# Member send
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def sendmember(ctx, member: discord.Member, *, text):
	await member.send()
	await ctx.message.add_reaction('✅')

# Channel send
@bot.command()
@commands.has_any_role(782860394297294858, 782860246321856534, 782860339342737408)
async def sendchannel(ctx, channel: int, *, text):
	channelm = bot.get_channel(channel)
	await channelm.send(f'{text}')
	await ctx.message.add_reaction('✅')


# Other
# Create role
@bot.command()
async def get_role(ctx, *, name):
	if ctx.channel.id == 782905071473393694:
		role = await ctx.guild.create_role(name=str(name))
		getrole = discord.utils.get(ctx.guild.roles, id = role.id)
		await ctx.message.author.add_roles(getrole)
		await ctx.message.add_reaction('✅')
		await asyncio.sleep(1.5)
		await ctx.channel.purge(limit=1)

	else:
		await ctx.send('Эту команду можно использовать только <#782905071473393694>')

@bot.command()
async def array(ctx, command = None, *, parametr = None):
	with open('bot_constants.json','r', encoding='utf-8') as f:
		const = json.load(f)

	array = const["list"]

	if command == None and parametr == None or command == "see" or command == "look":
		await ctx.send(f'`{array}`')

	elif command == "add":
		const["list"].append(f'{parametr}')
		await ctx.message.add_reaction('✅')

	elif command == "pop":
		const["list"].pop(int(parametr))
		await ctx.message.add_reaction('✅')

	elif command == "clear":
		const["list"] = []
		await ctx.message.add_reaction('✅')

	else:
		await ctx.send(f'Указан неверный параметр, спотрите `!help array`')

	with open('bot_constants.json','w') as f:
		json.dump(const,f)


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
	await asyncio.sleep(120)
	activity = discord.Game(name="!help", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)

# Hello
@bot.command()
async def hello(ctx):
	await ctx.send(f'{ctx.message.author.mention}, Привет!')


bot.run('')
