import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Message
from discord import DMChannel
import json
import asyncio
import base64
import os
import ctypes
from colorama import Fore, Back, Style
from colorama import init
init()

r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE

trollascii = f"""{g}QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQQQQQWQQQQQWWWBBBHHHHHHHHHBWWWQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQD!{w}`__ssaaaaaaaaaass_ass_s____.  -~""{g}??9VWQQQQQQQQQQQQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQP'{w}_wmQQQWWBWV?GwwwmmWQmwwwwwgmZUVVHAqwaaaac,{g}"?9$QQQQQQQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQW! {w}aQWQQQQW?qw#TTSgwawwggywawwpY?T?TYTYTXmwwgZ$ma/-{g}?4QQQQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQW' {w}jQQQQWTqwDYauT9mmwwawww?WWWWQQQQQ@TT?TVTT9HQQQQQQw,{g}-4QQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQ[ {w}jQQQQQyWVw2$wWWQQQWWQWWWW7WQQQQQQQQPWWQQQWQQw7WQQQWWc){g}WWQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQf {w}jQQQQQWWmWmmQWU???????9WWQmWQQQQQQQWjWQQQQQQQWQmQQQQWL {g}4QQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQQQQQQP'{w}.yQQQQQQQQQQQP"       <wa,.!4WQQQQQQQWdWP??!"??4WWQQQWQQc {g}?QWQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQWQQQQQQQQQQQQQQQP'{w}_a.<aamQQQW!<yF "!` ..  "??$Qa "WQQQWTVP'    "??' =QQmWWV?46/ {g}?QQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQQP'{w}sdyWQP?!`.-"?46mQQQQQQT!mQQgaa. <wWQQWQaa _aawmWWQQQQQQQQQWP4a7g {g}-WWQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQWQQQQQQQQQQQQQ[ {w}j@mQP'adQQP4ga, -????" <jQQQQQWQQQQQQQQQWW;)WQWWWW9QQP?"`  -?QzQ7L {g}]QQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQW {w}jQkQ@ jWQQD'-?$QQQQQQQQQQQQQQQQQWWQWQQQWQQQc "4QQQQa   .QP4QQQQfWkl {g}jQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQE {w}]QkQk $D?`  waa "?9WWQQQP??T?47`_aamQQQQQQWWQw,-?QWWQQQQQ`"QQQD\Qf(.{g}QWQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQWQQQQQQQQQQQQQ,{w}-Qm4Q/-QmQ6 "WWQma/  "??QQQQQQL 4W"- -?$QQQQWP`s,awT$QQQ@  "QW@?$:.{g}yQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQWQQQQQQQQQQQQQm/-{w}4wTQgQWQQ,  ?4WWk 4waac -???$waQQQQQQQQF??'<mWWWWWQW?^  ` ]6QQ' {g}yQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQQQw,{w}-?QmWQQQQw  a,    ?QWWQQQw _.  "????9VWaamQWV???"  a j/  ]QQf {g}jQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQWQQQQQQQQQQQQQQQQw,{w}"4QQQQQQm,-$Qa     ???4F jQQQQQwc <aaas _aaaaa 4QW ]E  )WQ`{g}=QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQWQ/ {w}$QQQQQQQa ?H ]Wwa,     ???9WWWh dQWWW,=QWWU?  ?!     )WQ {g}]QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQc-{w}QWQQQQQW6,  QWQWQQQk <c                             jWQ {g}]QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQ,{w}"$WQQWQQQQg,."?QQQQ'.mQQQmaa,.,                . .; QWQ.{g}]QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQWQa {w}?$WQQWQQQQQa,."?( mQQQQQQW[:QQQQm[ ammF jy! j( ] jQQQ({g}:QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQWWma {w}"9gw?9gdB?QQwa, -??T$WQQ;:QQQWQ ]WWD _Qf +?! _jQQQWf {g}QQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQws {w}"Tqau?9maZ?WQmaas,,    --~-- ---  . _ssawmQQQQQQk {g}3QQQQWQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQWQga,{w}-?9mwad?1wdT9WQQQQQWVVTTYY?YTVWQQQQWWD5mQQPQQQ {g}]QQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQWQQQQQQQQQQQQQQQWQQQQQQQQQQQWQQwa,{w}-??$QwadV]<wBHHVHWWBHHUWWBVTTTV5awBQQD6QQQ {g}]QQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWQQga,{w}-"9$WQQmmwwmBUUHTTVWBWQQQQWVT?96aQWQQQ {g}]QQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQQQQQQWQQQQQQQQQQQQQQQQWQQQQWQQQQQQQQQQQWQQma,{w}-?9$QQWWQQQQQQQWmQmmmmmQWQQQQWQQW({g}.yQQQQQWQQQQQQQQQWQQQQQQQQQQQQQ
QQQQQQQQQQQQQWQQQQQQWQQQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQga%,.  {w}-??9$QQQQQQQQQQQWQQWQQV? {g}sWQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQWQQQQQQQQQQQQQQWQQQQQQQQQQQWQQQQmywaa,{w};~^"!???????!^`{g}_saQWWQQQQQQQQQQQQQQQQWQQQQQQQQQQQQ
QQQQQQQQQWQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWWWQQQQQmwywwwwwwmQQWQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ"""

          
adbot = f"""

                                        {r}█████{w}╗ {r}██████{w}╗ {r}██████{w}╗  {r}██████{w}╗ {r}████████{w}╗
                                       {r}██{w}╔══{r}██{w}╗{r}██{w}╔══{r}██{w}╗{r}██{w}╔══{r}██{w}╗{r}██{w}╔═══{r}██{w}╗╚══{r}██{w}╔══╝
                                       {r}███████{w}║{r}██{w}║  {r}██{w}║{r}██████{w}╔╝{r}██{w}║   {r}██{w}║   {r}██{w}║   
                                       {r}██{w}╔══{r}██{w}║{r}██{w}║  {r}██{w}║{r}██{w}╔══{r}██{w}╗{r}██{w}║   {r}██{w}║   {r}██{w}║   
                                       {r}██{w}║  {r}██{w}║{r}██████{w}╔╝{r}██████{w}╔╝╚{r}██████{w}╔╝   {r}██{w}║   
                                       {w}╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝    ╚═╝

      {Fore.CYAN}                       ╔═════════════════════════[{Style.RESET_ALL}AdBot{Fore.CYAN}]════════════════════════╗
                             ║ {Fore.MAGENTA}Version: {Style.RESET_ALL}1.0{Fore.CYAN}                                           ║
                             ║ {Fore.MAGENTA}Created By: {Style.RESET_ALL}Daddy Lazarus{Fore.CYAN}                              ║
      {Fore.CYAN}                       ╚════════════════════════════════════════════════════════╝
      
      
"""
ctypes.windll.kernel32.SetConsoleTitleW("Loading AdBot...")
print(trollascii + Style.RESET_ALL)
with open('config.json', "rb") as infile:
    config = json.load(infile)
    token = config["userdata"].get('token')
    channelids = config["userdata"].get('channelids')

if token == "null":
    os.system('cls')
    unset = True
    while unset == True:
        print(Fore.RED + "Error: " + Style.RESET_ALL + "No local userdata found!")
        token = input("Please enter your discord token: ")
        if len(token) > 0:
            oldtokenvalue = config["userdata"].get('token')
            oldmessagevalue = config["userdata"].get('message')
            oldchannelidsvalue = config["userdata"].get('channelids')
            update = {"userdata": {"token": token,"message": oldmessagevalue,"channelids": oldchannelidsvalue}}
            config.update(update)
            with open('config.json', "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
        else:
            print(Fore.RED + "Error: " + Style.RESET_ALL + "Invalid token!")
else:
    pass


ABT = commands.Bot(command_prefix = "?", self_bot=True, loop=None)

@ABT.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW("AdBot")
    os.system('cls')
    print(adbot + Style.RESET_ALL)
    print('Logged in as ' + Fore.RED + f'{ABT.user.name}#{ABT.user.discriminator}' + Style.RESET_ALL)
    advertise.start()

@tasks.loop(hours=1)
async def advertise():
    with open('config.json', "rb") as infile:
        config = json.load(infile)
        channelstosend = config["userdata"].get('channelids')
    if "null" in channelstosend:
        pass
    else:
        for i in channelstosend:
            decodedmsg = base64.b64decode(config["userdata"].get('message'))
            await ABT.get_channel(int(i)).send(decodedmsg.decode('utf-8'))

@ABT.command()
async def addchannel(ctx, *, id):
    with open('config.json', "rb") as infile:
        config = json.load(infile)
    oldtokenvalue = config["userdata"].get('token')
    oldmessagevalue = config["userdata"].get('message')
    oldchannelidsvalue = config["userdata"].get('channelids')
    if oldchannelidsvalue == "null":
        update = {"userdata": {"token": oldtokenvalue,"message": oldmessagevalue,"channelids": [id]}}
        config.update(update)
        with open('config.json', "w") as jsfile:
            json.dump(config, jsfile)
            jsfile.close()
    else:
        oldchannelidsvalue.append(id)
        update = {"userdata": {"token": oldtokenvalue,"message": oldmessagevalue,"channelids": oldchannelidsvalue}}
        config.update(update)
        with open('config.json', "w") as jsfile:
            json.dump(config, jsfile)
            jsfile.close()

@ABT.command()
async def setmsg(ctx, *, msg):
    await ctx.message.delete()
    encodedmsg = str(base64.b64encode(bytes(msg, 'utf-8')))[2:-1]
    with open('config.json', "rb") as infile:
        config = json.load(infile)
    oldtokenvalue = config["userdata"].get('token')
    oldchannelidsvalue = config["userdata"].get('channelids')
    update = {"userdata": {"token": oldtokenvalue,"message": encodedmsg,"channelids": oldchannelidsvalue}}
    config.update(update)
    with open('config.json', "w") as jsfile:
        json.dump(config, jsfile)
        jsfile.close()


ABT.run(token, bot=False)
input()
