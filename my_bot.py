import discord
from googlesearch import search
import random
import datetime
import time
import requests
import json
from googletrans import Translator

token = "NjcwMjg0NTA1ODg1NTczMTgz.XlDUUA.oUYtENddJt24-8cu0toER32gPv8"

url = "https://notify-api.line.me/api/notify"
access_token = "BIpNpPokdscqRrQLGlO3bovDymapN2Oo2w0duR0JSmr"
headers = {'Authorization': 'Bearer ' + access_token}

client = discord.Client()
good_morning_say = [
    "おは～",
    "おはよ!",
    "おふぁようござす",
    "おはようナス!",
    "zzzzz...ふぁぁ\nおはよぉ",
    "good morning",
    "早くしたくしなさい！\nおくれちゃうわよ"
]
good_night_say = [
    "おやすみナスぅ...zzz",
    "おやすぅ",
    "おやすみ!!!!!",
    "おすやみ",
    "眠いからそういうのいいんで",
    "good by 君の...zzz",
    "zzzzz....\nうるせぇぇぇ!!",
    "はいはいバイバイ",
    "ねるねるねーるネzzz",
    "zzzzzz",
    "good luck!",
    "good night",
    "いい夢見ろヨ"
]

f = open("properties.json","r",encoding="utf-8")
data = json.load(f)

google_mode = False
new_load = False
search_set_mode = False
search_set_select_user = 0
select_user = 0
set_count = 5
end_command = "$end"
dbc = 0
my_sister_DS = False
DMSG = False
say_count = {}
delete_list = []
translator = Translator()

@client.event
async def on_ready():
    if client.get_channel(669514169766248459):
        start_channel = client.get_channel(669514169766248459)
        await start_channel.send("私がキタぁ\n" + client.user.name + "がログインしました")
    print("rogin clear")
@client.event
async def on_message(message):
    global google_mode,select_user,search_set_mode,search_set_select_user,end_command,set_count,set_count,new_load,dbc,my_sister_DS,say_count,msg,payload,r,url,access_token,headers,date,bad_m_pos,DMSG,T_pos,TM
    print(message.content)
    um = message.content
    if message.content.startswith("$delete "):
        if message.author != client.user:
            DELETE_COUNT = message.content[len("$delete "):]
            print(DELETE_COUNT)
            i = 0
            while True:
                await message.delete()
                i += 1
                if i > int(DELETE_COUNT):
                    await message.channel.send("削除かんりょー")
                    break
        return
    if message.author != client.user:
        for dt in data["msg"]["bad"]:
            if dt in um:
                print(dt)
                ucm = um.replace(dt,len(dt) * "X")
                um = ucm
                DMSG = True
    if DMSG == True:
        if message.author != client.user:
            await message.delete()
            await message.channel.send("user : " + message.author.name + "\n" + ucm)
    msg = "ユーザー[" + message.author.name + "] : " + um + "[" + message.channel.name + "]"
    payload = {'message': msg}
    
    r = requests.post(url, headers=headers, params=payload)
    print(msg)
    T_all_data = translator.detect(message.content)
    T_lang = T_all_data.lang
    print(T_lang)
    if message.author != client.user:
        if T_lang != "ja":
            for i in ["www","WWW","https"]:
                if i in um:
                    return
            if DMSG == True:
                await message.channel.send("[ word error ]>>> Unable to translate if there is an inappropriate word <<<")
                return
            TM = translator.translate(message.content,src=T_lang,dest="ja")
            embed = discord.Embed(title='翻訳',color=0xff0000)
            embed.add_field(name='User',value=message.author.name)
            embed.add_field(name="Before",value=um,inline=False)
            embed.add_field(name='After Transformation',value=TM.text,inline=False)
            await message.channel.send(embed=embed)
    DMSG = False
    if message.author != client.user:
        if "/T" in message.content:
            T_pos = message.content.find("/T") + 2
            if T_lang == "ja":
                TM = translator.translate(message.content[len("/T"):],src=T_lang,dest="en")
            else:
                await message.channel.send("Language not supported")
                return
            await message.delete()
            await message.channel.send(message.author.name + " : " + TM.text)
            return
    if message.content.startswith("おはよう"):
        if message.author != client.user:
            await message.channel.send(random.choice(good_morning_say))
    if message.content.startswith("おやすみ") or message.content.startswith("お休み"):
        if message.author != client.user:
            await message.channel.send(random.choice(good_night_say))
    if search_set_mode == True:
        if message.author.id == search_set_select_user:
            if not message.content == end_command:
                if not int(message.content) == 0:
                    if not int(message.content) > 15:
                        set_count = int(message.content)
                        search_set_mode = False
                        await message.channel.send("googleの検索が上から" + str(set_count) + "個ずつ表示されるようになりました")
                    else:
                        await message.channel.send("15以上は設定できません")
                else:
                    await message.channel.send("0はせってできません")
    if message.content == "$set_search":
        search_set_mode = True
        search_set_select_user = message.author.id
        await message.channel.send("Please specify a numerical value")
    if new_load == True:
        if message.author != client.user:
            await message.delete()
    if google_mode == True:
        if message.author != client.user:
            if message.author.id == select_user:
                if not message.content.startswith("!"):
                    if not message.content == end_command:
                        if not new_load == True:
                            if not search_set_mode == True:
                                cot = message.content
                                await message.channel.send("上位" + str(set_count) + "位の検索結果を表示しまぁす")
                                count = 0
                                new_load = True
                                for url in search(cot, lang="jp",num = 5):
                                    print(msg)
                                    await message.channel.send(url)
                                    count += 1
                                    if(count == set_count):
                                        google_mode = False
                                        new_load = False
                                        await message.channel.send("完了")
                                        return
                    else:
                        google_mode = False
                        new_load = False
                        await message.channel.send("検索モードちゅーし")
                else:
                    await message.channel.send("[MSG Error] { This message uses command symbols }")
    if message.content == "!google":
        if message.author != client.user:
            if google_mode == True:
                await message.channel.send("すでに実行済みです終了するまでお待ちください。")
            else:
                google_mode = True
                select_user = message.author.id
                await message.channel.send("検索したいことを発言よろしくぅ\n(実行した人にしかbotは反応しません)")
                return
    #list
    if not say_count.get(message.author.name):
        say_count[message.author.name] = 0
    say_count[message.author.name] += 1
    print(say_count[message.author.name])
    if message.content == "$say_list":
        for i in say_count:
            await message.channel.send(i + " : " + str(say_count.get(i)))
        say_count[message.author.name] -= 1

@client.event
async def on_member_join(member):
    mein_channel = client.get_channel(666922870563143691)
    set_role = discord.utils.get(member.guild.roles, name='new join user')
    await member.add_roles(set_role)
    await mein_channel.send(member.mention + "０８２\nみんな～\n" + member.name + "がこのサーバーにはいったぞぉおおお!!")
client.run(token)
