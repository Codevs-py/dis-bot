import discord
from discord.ext import commands
import asyncio
import time as tt


bot = commands.Bot(command_prefix = "d! ", description = "Padhna to seekh phle")


@bot.event
async def on_ready():
    print("started as ", bot.user.name)


@bot.event
async def on_member_update(before, after):
    if before.status == discord.Status.online:
        if after.status == discord.Status.offline:
            channel = after.guild.system_channel
            if channel is not None:
                time = tt.gmtime()
                time = f"{time.tm_hour}:{time.tm_min}:{time.tm_sec} GMT"
                await channel.send(f"{after.name} is {after.status} at {time}")
            

    elif before.status == discord.Status.offline:
        if after.status == discord.Status.online:
            channel = after.guild.system_channel
            if channel is not None:
                time =tt.gmtime()
                time = f"{time.tm_hour}:{time.tm_min}:{time.tm_sec} GMT"
                await channel.send(f"{after.name} is {after.status} at {time}")

@bot.command()
async def info(ctx):
    await ctx.send(f"I am {bot.user.name}\n My Id {bot.user.id}")



@bot.command()
async def start_attendence(ctx): #command to start attendce
    emoji = '\N{WHITE HEAVY CHECK MARK}'
    try:
        msg = await ctx.send("Give Your Attendence By reacting") #send message
        await msg.add_reaction(emoji) #add tick mark
        id = msg.id #get message id

        async def wait(delay): #create delay
            await asyncio.sleep(15.0)
            return True
        await wait(0)

        msg = await ctx.channel.fetch_message(id) #get message
        reaction = msg.reactions #get reactions
        for i in reaction: #check members reacted with tick mark
            if i.emoji == emoji:
                users = await i.users().flatten()
        name = []
        for user in users: #get names of attenders
            name.append(str(user))
        print(name)

    except Forbidden: #if dont have perm
        await ctx.send("I don't have perm to react")

    except HTTPException: #if failing reason is smh else
        await ctx.send("Can't add reactions")

bot.run("NzAzMTY0NzE5NDg5NjEzODM1.XwWkOw.vGI8s-YGEZio9-eLsEvDb1KtIiE")