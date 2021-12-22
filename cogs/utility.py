import disnake as discord
from disnake.ext import commands
import random
import asyncio
import datetime, time
from replit import db

botbuild = "3.73.24" # major.sub.fix
pyver = "3.8.2"
dnver = "2.2.2"

waiquotes = ["Your cool", "Your pro", "I dont know who are you", "Your 228 iq", "Your The Le` Pro!", "Que pro"]
pollemojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
if "afk" not in db:
  db["afk"] = {}

if "notes" not in db:
  db["notes"] = {}
  
class Utility(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #ping command
  @commands.command(help = "Shows bot's ping", description = "Usage: pb!ping") 
  async def ping(self, ctx):
    before = time.time()
    message = await ctx.send("Pinging...")
    after = time.time()
    e = discord.Embed(title = "Pong!", description = f"Bot ping: {int(ctx.bot.latency * 1000)}ms\nReply ping: {int((time.time() - ctx.message.created_at.timestamp()) * 1000) - int((after - before) * 1000)}ms (original: {int((time.time() - ctx.message.created_at.timestamp()) * 1000)}ms)\nEdit ping: {int((after - before) * 1000)}ms\nUp since: <t:{int(self.bot.launch_time.timestamp())}:R>", color = random.randint(0, 16777215))
    await message.edit(content = None, embed = e)
    
  #bot info command
  @commands.command(help = "Shows bot's info", description = "Usage: pb!botinfo")
  async def botinfo(self, ctx):
    e = discord.Embed(title = "About PythonBot", description = f"PythonBot is bot. Bot. Discord bot.\nBot made by Number1#4325.\nTotal amount of commands: {len(tuple(command for command in ctx.bot.commands if not command.hidden))}/{len(ctx.bot.commands)} ({len(ctx.bot.commands) - len(tuple(command for command in ctx.bot.commands if not command.hidden))} hidden)\nIn: {len(self.bot.guilds)} servers",  color = random.randint(0, 16777215))
    e.add_field(name = "Contributors:", value = "icemay#6281 - Helper\nSenjienji#8317 - Helper, Tester\nBricked#7106 - Helper, Tester\nDark dot#5012 - Contributor, Tester\nTjMat#0001 - Contributor\nR3DZ3R#8150 - Contributor\nRage#6456 - Tester", inline = False)
    e.add_field(name = f"Versions", value = f"Bot: {botbuild}\nPython: {pyver}\nDisnake: {dnver}", inline = False)
    await ctx.send(embed = e)

  #server info command
  @commands.command(aliases = ["si", "server"], help = "Shows server's info", description = "Usage: pb!serverinfo")
  async def serverinfo(self, ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [self.bot.mention for self.bot in ctx.guild.members if self.bot.bot]
    e = discord.Embed(title = f"Server info: {ctx.guild.name}", description = f"Icon url: {str(ctx.guild.icon)[:-10]}\nServer creation date: <t:{str(time.mktime(ctx.guild.created_at.timetuple()))[:-2]}:R>", color = random.randint(0, 16777215))
    e.add_field(name = "Members", value = f"Total: {ctx.guild.member_count}\nHumans: {ctx.guild.member_count - len(list_of_bots)}\nBots: {len(list_of_bots)}", inline = False)
    e.add_field(name = "Moderation", value = f"Server owner: {ctx.guild.owner.name}\nVerification level: {str(ctx.guild.verification_level)}\nNumber of roles: {role_count}\nNumber of channels: {len(ctx.guild.channels)}\nList of bots({len(list_of_bots)}): " + ", ".join(list_of_bots), inline = False)
    e.set_thumbnail(url = str(ctx.guild.icon))
    e.set_footer(text = f"ID: {ctx.guild.id}")
    await ctx.send(embed = e)
  
  #member info command
  @commands.command(aliases = ["mi", "whois", "user", "member"], help = "Shows mentioned member's info", description = "Usage: pb!memberinfo (@mention)")
  async def memberinfo(self, ctx, member: discord.Member = None):
    if member != None:
      role_list = []

      for role in member.roles:
        if role.name != "@everyone":
          role_list.append(role.mention)

      b = ",".join(role_list)
      e = discord.Embed(title = f"Member info: {member}", description = f"Joined server date: <t:{str(time.mktime(member.joined_at.timetuple()))[:-2]}:R>\nCreated account date: <t:{str(time.mktime(member.created_at.timetuple()))[:-2]}:R>", color = random.randint(0, 16777215))
      e.set_thumbnail(url = str(member.avatar))
      if len(role_list) != 0:
        e.add_field(name = f"Roles ({len(role_list)}):", value = "".join([b]), inline = False)
      else:
        e.add_field(name = "Roles (0)", value = "None")
      e.add_field(name = "Top role:", value = member.top_role.mention, inline = False)
      if member.guild_permissions.administrator:
        e.add_field(name = "Administrator?", value = "True" , inline = False)
      else:
        e.add_field(name = "Administrator?", value = "False", inline = False)
      e.add_field(name = "Icon url:", value = str(member.avatar)[:-10], inline = False)
      e.set_footer(text = f"ID: {member.id}")
      await ctx.send(embed = e)
    else:
      rgwai = waiquotes[random.randint(0, len(waiquotes) - 1)]
      role_list = []

      for role in ctx.author.roles:
        if role.name != "@everyone":
          role_list.append(role.mention)

      b = ",".join(role_list)
      e = discord.Embed(title = f"Member info: {ctx.author}", description = f"Joined server date: <t:{str(time.mktime(ctx.author.joined_at.timetuple()))[:-2]}:R>\nCreated account date: <t:{str(time.mktime(ctx.author.created_at.timetuple()))[:-2]}:R>", color = random.randint(0, 16777215))
      e.set_thumbnail(url = str(ctx.author.avatar))
      if len(role_list) != None:
        e.add_field(name = f"Roles ({len(role_list)}):", value = "".join([b]), inline = False)
      else:
        e.add_field(name = "Roles (0):", value = "None")
      e.add_field(name = "Top role:", value = ctx.author.top_role.mention, inline = False)
      if ctx.author.guild_permissions.administrator:
        e.add_field(name = "Administrator?", value = "True" , inline = False)
      else:
        e.add_field(name = "Administrator?", value = "False", inline = False)
      e.add_field(name = "Icon url:", value = str(ctx.author.avatar)[:-10], inline = False)
      e.add_field(name = "Quote:", value = f"{rgwai}")
      e.set_footer(text = f"ID: {ctx.author.id}")
      await ctx.send(embed = e)

  #suggest command
  @commands.command(help = "Suggest an idea", description = "Suggest an idea for server improvement or a bot maker!\nexample: pb!suggest \"hello world\" @Number1#4325\nexample 2: pb!suggest \"hello world\"")
  async def suggest(self, ctx, text, member: discord.Member = None):
    e = discord.Embed(title = f"Suggestion from: {ctx.author}", description = f"{text}", color = random.randint(0, 16777215))
    e.set_thumbnail(url = str(ctx.author.avatar))
    msg = await ctx.send(embed = e)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    if member != None:
      e = discord.Embed(title = f"Suggestion from: {ctx.author}", description = f"Idea: {text}", color = random.randint(0, 16777215))
      e.set_thumbnail(url = str(ctx.author.avatar))
      await member.send(embed = e)
    await ctx.message.add_reaction("✅")
  
  #invite command
  @commands.command(help = "See invites", description = "See invites  to bot support server and invite bot to your server")
  async def invite(self, ctx):
    e = discord.Embed(title = "Invites", description = "Click the buttons below!", color = random.randint(0, 16777215))
    view = discord.ui.View()
    style = discord.ButtonStyle.gray
    item = discord.ui.Button(style = style, label = "Invite bot to your server", url = "https://discord.com/api/oauth2/authorize?client_id=912745278187126795&permissions=8&scope=bot")
    style1 = discord.ButtonStyle.gray
    item1 = discord.ui.Button(style = style1, label = "Invite to support server", url = "https://discord.gg/jRK82RNx73")
    view.add_item(item = item)
    view.add_item(item = item1)
    await ctx.send(embed = e, view = view)
    
  #emoji command
  @commands.command(aliases = ["emo"], help = "See emoji info", description = "See selected emoji info")
  async def emoji(self, ctx, emoji: discord.Emoji):
    e = discord.Embed(title = f"Emoji info: {emoji.name}", description = f"Animated?: {'True' if emoji.animated else 'False'}\nCreated at: <t:{int(emoji.created_at.timestamp())}:F>\nLink: [Link here]({emoji.url})", color = random.randint(0, 16777215))
    e.set_image(url = emoji.url)
    e.set_footer(text = f"ID: {emoji.id}")
    await ctx.send(embed = e)

  #servers command
  @commands.command(help = "See other servers' member counter", description = "This command is useless don't use it")
  async def servers(self, ctx):
    await ctx.trigger_typing()
    counter = "\n".join(f"{index}. `{guild.name}` by `{guild.owner.name}`: {guild.member_count}" for index, guild in enumerate(sorted(ctx.bot.guilds, key = lambda guild: guild.me.joined_at.timestamp()), start = 1))
    e = discord.Embed(title = "Servers' member counts:", description = f"Total: {len(ctx.bot.users)}\n{counter}", color = random.randint(0, 16777215))
    await ctx.send(embed = e)

  #afk command
  @commands.command(help = "Set your afk and reason for it")
  async def afk(self, ctx, *, reason = "None"):
      db["afk"][str(ctx.author.id)] = reason
      e = discord.Embed(title = "AFK", description = f"Set your afk reason to `{reason}`", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  #poll command
  @commands.command(help = "Make polls")
  async def poll(self, ctx, name = None, option1 = "", option2 = "", option3 = "", option4 = "", option5 = ""):
    if name != None:
      e = discord.Embed(title = f"Poll from {ctx.author.name}: {name}", description = f"{pollemojis[0] if not option1 == '' else ''} {option1}\n{pollemojis[1] if not option2 == '' else ''} {option2}\n{pollemojis[2] if not option3 == '' else ''} {option3}\n{pollemojis[3] if not option4 == '' else ''} {option4}\n{pollemojis[4] if not option5 == '' else ''} {option5}", color = random.randint(0, 16777215))
      msg = await ctx.send(embed = e)
      num = 1
      list = [option1, option2, option3, option4, option5]
      for i in range(len(pollemojis) - 1):
        if not list[i] == "": await msg.add_reaction(pollemojis[i])
        num += 1
    else:
      e = discord.Embed(title = "Error", description = "You can't make nameless poll", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  #group smh
  @commands.group(aliases = ["n"], help = "Make notes with the bot (BETA)")
  async def note(self, ctx):
    if str(ctx.author.id) not in db["notes"]:
        db["notes"][str(ctx.author.id)] = {}
    if ctx.invoked_subcommand == None:
      e = discord.Embed(title = "Error", description = "Type a subcommand!\nAvaliable subcommands: add, read, list, replace, create, newline, readraw and del", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
  
  @note.command(help = "Shows list of notes you have")
  async def list(self, ctx):
    if str(ctx.author.id) in db["notes"] and db["notes"][str(ctx.author.id)] != {}:
      notes = "\n".join(f"{index}. `{name}`" for index, (name) in enumerate(db["notes"][str(ctx.author.id)].keys(), start = 1))
      e = discord.Embed(title = f"{ctx.author}'s notes:", description = notes, color = random.randint(0, 16777215))
      await ctx.send(embed = e)
    else:
      e = discord.Embed(title = f"Notes: {ctx.author}", description = "You have nothing right now", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
  
  @note.command(help = "Creates note")
  async def create(self, ctx, name = None, *, text = None):
    if str(ctx.author.id) in db["notes"]:
      if name not in db["notes"][str(ctx.author.id)]:
        if text != None:
          updatenotes = db["notes"][str(ctx.author.id)]
          updatenotes[name] = text
          db["notes"][str(ctx.author.id)] = updatenotes
          e = discord.Embed(title = "Success", description = f"Note named `{name}` is created!", color = random.randint(0, 16777215))
          await ctx.send(embed = e)
        else:
          updatenotes = db["notes"][str(ctx.author.id)]
          updatenotes[name] = "New note"
          db["notes"][str(ctx.author.id)] = updatenotes
          e = discord.Embed(title = "Success", description = f"Note named `{name}` is created!", color = random.randint(0, 16777215))
          await ctx.send(embed = e)
      else:
        e = discord.Embed(title = "Error", description = "This name is used!", color = random.randint(0, 16777215))
        await ctx.send(embed = e)
    else:
      if text != None:
        db["notes"][str(ctx.author.id)] = {}
        updatenotes = db["notes"][str(ctx.author.id)]
        updatenotes[name] = text
        db["notes"][str(ctx.author.id)] = updatenotes
        e = discord.Embed(title = "Success", description = f"Note named `{name}` is created!", color = random.randint(0, 16777215))
        await ctx.send(embed = e)
      else:
        db["notes"][str(ctx.author.id)] = {}
        updatenotes = db["notes"][str(ctx.author.id)]
        updatenotes[name] = "New note"
        db["notes"][str(ctx.author.id)] = updatenotes
        e = discord.Embed(title = "Success", description = f"Note named `{name}` is created!", color = random.randint(0, 16777215))
        await ctx.send(embed = e)
  
  @note.command(help = "Replaces whole note text")
  async def replace(self, ctx, name = None, *, text = None):
    try:
      updatenotes = db["notes"][str(ctx.author.id)]
      updatenotes[name] = text
      db["notes"][str(ctx.author.id)] = updatenotes
      e = discord.Embed(title = "Success", description = f"Changed `{name}`'s text", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
    except KeyError:
      e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  @note.command(help = "Inserts text at the end\nread - reads selected note")
  async def add(self, ctx, name = None, *, text = None):
    try:
      updatenotes = db["notes"][str(ctx.author.id)]
      updatenotes[name] += f" {text}"
      db["notes"][str(ctx.author.id)] = updatenotes
      e = discord.Embed(title = "Success", description = f"Changed `{name}`'s text", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
    except KeyError:
      e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  @note.command(help = "Inserts text at the end on new line")
  async def newline(self, ctx, name = None, *, text = None):
    try:
      updatenotes = db["notes"][str(ctx.author.id)]
      updatenotes[name] += f"\n{text}"
      db["notes"][str(ctx.author.id)] = updatenotes
      e = discord.Embed(title = "Success", description = f"Changed `{name}`'s text", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
    except KeyError:
      e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
  
  @note.command(help = "Reads selected note")
  async def read(self, ctx, *, name = None):
    if name in db["notes"][str(ctx.author.id)]:
      e = discord.Embed(title = f"Notes: {name}", description = f"{db['notes'][str(ctx.author.id)].get(name)}", color = random.randint(0, 16777215))
      await ctx.send(embed = e)
    else:
      e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  @note.command(help = "Deletes selected note")
  async def delete(self, ctx, name = None):
    if str(ctx.author.id) in db["notes"]:
      if name != None:
        if name in db["notes"][str(ctx.author.id)]:
          updatenotes = db["notes"][str(ctx.author.id)]
          e = discord.Embed(title = "Success", description = f"Note named `{name}` is deleted!", color = random.randint(0, 16777215))
          await ctx.send(embed = e)
          updatenotes.pop(name)
          db["notes"][str(ctx.author.id)] = updatenotes
        else:
          e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist!", color = random.randint(0, 16777215))
          await ctx.send(embed = e)
      else:
        e = discord.Embed(title = f"Error", description = "You can't delete nothing!", color = random.randint(0, 16777215))
        await ctx.send(embed = e)
    else:
      e = discord.Embed(title = f"Error", description = "You have no notes!", color = random.randint(0, 16777215))
      await ctx.send(embed = e)

  @note.command(help = "Reads selected note but **text** is \*\*text\*\*")
  async def readraw(self, ctx, name = None):
    if str(ctx.author.id) in db["notes"]:
      if name in db["notes"][str(ctx.author.id)]:
        text = db['notes'][str(ctx.author.id)].get(name).replace('_', '\_').replace('*', '\*').replace('`', '\`').replace('~', '\~')
        e = discord.Embed(title = f"Notes: {name}", description = text, color = random.randint(0, 16777215))
        await ctx.send(embed = e)
      else:
        e = discord.Embed(title = f"Error", description = f"Note `{name}` doesn't exist!", color = random.randint(0, 16777215))
        await ctx.send(embed = e)
    else:
      e = discord.Embed(title = f"Error", description = "You have no notes!", color = random.randint(0, 16777215))
      await ctx.send(embed = e)



def setup(bot):
  bot.add_cog(Utility(bot))