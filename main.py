import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.client(intents=intents)

@bot.event
async def on_voice_state_update(member, before,after):
    try:
        if before.channel is None and after.channel is not None and after.channel == bot.voice_clients[0].channel:
            channel = bot.get_channel(channel_id) # ระบุ id ของ channel ที่ต้องการส่งข้อความแจ้งเตือน
            await channel.send(f"{member.mention} เข้าห้องแล้ว")
        elif after.channel is None and before.channel is not None and before.channel == bot.voice_clients[0].channel:
            channel = bot.get_channel(channel_id) # ระบุ id ของ channel ที่ต้องการส่งข้อความแจ้งเตือน
            await channel.send(f"{member.mention} ออกจากห้องแล้ว")
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            channel = bot.get_channel(channel_id) # ระบุ id ของ channel ที่ต้องการส่งข้อความแจ้งเตือน
            await channel.send(f"{member.mention} ย้ายจากห้อง {before.channel.name} ไปยังห้อง {after.channel.name}")
    except IndexError:
        pass

bot.run('your_token')