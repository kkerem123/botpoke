
from dotenv import load_dotenv
load_dotenv()
import os
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.message_content = True
intents.members = True # üye eklemek kaldırmak için
bot = commands.Bot(command_prefix= "!", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("hi")

araba_listesi=[]

class Car:
     def __init__(self,name,motor_gücü,tür,fiyat):
        self.name=name
        self.motor_gücü=motor_gücü
        self.tür=tür #sportif #benzinli #elektrikli tarzı
        self.fiyat=fiyat
     def show_info(self):
        return f"Arabanızın markası: {self.name},MOTOR GÜCÜ: {self.motor_gücü}, TÜRÜ:{self.tür} ve FİYATI: {self.fiyat}"
araba1=Car(name=input(),motor_gücü=input,tür=input(),fiyat=input())


araba_listesi=[]

class Car:
     def __init__(self,name,motor_gücü,tür,fiyat):
        self.name=name
        self.motor_gücü=motor_gücü
        self.tür=tür #sportif #benzinli #elektrikli tarzı
        self.fiyat=fiyat
     def show_info(self):
        return f"Arabanızın markası: {self.name},MOTOR GÜCÜ: {self.motor_gücü}, TÜRÜ:{self.tür} ve FİYATI: {self.fiyat}"


@bot.command()
async def araba_oluşturmaca(ctx, name, motor_gücü, tür, fiyat):
    araba1 = Car(name, motor_gücü, tür, fiyat)
    araba_listesi.append(araba1)
    await ctx.send(araba1.show_info())

@bot.command()
async def listele(ctx):
        if not  araba_listesi:
            await ctx.send("arabanız daha eklenmedi.")
        else:
            for araba in araba_listesi:
                await ctx.send(araba.show_info())
            

        


bot.run(DISCORD_TOKEN)