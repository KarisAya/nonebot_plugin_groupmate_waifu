from nonebot import require
from nonebot.plugin.on import on_command
from nonebot.adapters.onebot.v11 import (
    GROUP,
    Bot,
    GroupMessageEvent,
    MessageSegment,
    )

import os
import random

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from .utils import *

scheduler = require("nonebot_plugin_apscheduler").scheduler

path = os.path.join(os.path.dirname(__file__),"data")

# 娶群友

record_waifu = {}

waifu = on_command("娶群友", permission=GROUP, priority = 90, block = True)

no_waifu = [
    "你没有娶到群友，强者注定孤独，加油！",
    "找不到对象.jpg",
    "恭喜你没有娶到老婆~",
    "さんが群友で結婚するであろうヒロインは、\n『自分の左手』です！"
    ]

@waifu.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.user_id
    global record_waifu
    record_waifu.setdefault(group_id,{})
    if record_waifu[group_id].get(user_id,0) == 0:
        member_list = await bot.get_group_member_list(group_id = event.group_id)
        i = 0
        while i < len(member_list):
            if member_list[i]['user_id'] in record_waifu[group_id].keys():
                del member_list[i]
            else:
                i += 1
        else:
            if member_list:
                member_list.sort(key = lambda x:x["last_sent_time"] ,reverse = True)
                member = random.choice(member_list[:80])
                record_waifu[group_id].update(
                    {
                        user_id:member['user_id'],
                        member['user_id']:user_id
                        }
                    )
            else:
                record_waifu[group_id][user_id] = 1
    else:
        member = await bot.get_group_member_info(group_id = group_id, user_id = record_waifu[group_id][user_id])

    if record_waifu[group_id][user_id] == event.user_id:
        msg = random.choice(no_waifu)
    elif record_waifu[group_id][user_id] == 1:
        msg = "群友已经被娶光了、\n" + random.choice(no_waifu)
    else:
        nickname = member['card'] if member['card'] else member['nickname']
        msg = (
            "さん的群友結婚对象是、\n",
            MessageSegment.image(file = await user_img(record_waifu[group_id][user_id])),
            f"『{nickname}』です！"
            )
    await waifu.finish(msg, at_sender=True)

# 查看娶群友卡池

waifu_list = on_command("查看群友卡池", aliases = {"群友卡池"}, permission=GROUP, priority = 90, block = True)

@waifu_list.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    member_list = await bot.get_group_member_list(group_id = event.group_id)
    i = 0
    while i < len(member_list):
        if member_list[i]['user_id'] in record_waifu.setdefault(event.group_id,{}).keys():
            del member_list[i]
        else:
            i += 1
    else:
        if member_list:
            member_list.sort(key = lambda x:x["last_sent_time"] ,reverse = True)
            msg ="Top80：\n——————————————\n"
            for i in range(len(member_list[:80])):
                nickname = member_list[i]['card'] if member_list[i]['card'] else member_list[i]['nickname']
                msg += f"{nickname}\n"
            else:
                output = text_to_png(msg[:-1])
                await waifu_list.finish(MessageSegment.image(output))
        else:
            await waifu_list.finish("卡池为空，群友已经被娶光了...")

# 透群友

record_yinpa = {}

yinpa = on_command("透群友", permission=GROUP, priority = 90, block = True)

@yinpa.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.user_id
    member_list = await bot.get_group_member_list(group_id = event.group_id)
    member_list.sort(key = lambda x:x["last_sent_time"] ,reverse = True)
    member = random.choice(member_list[:80])

    if member["user_id"] == event.user_id:
        msg = "不可以涩涩！"
    else:
        nickname = member['card'] if member['card'] else member['nickname']
        global record_yinpa
        record_yinpa.setdefault(member['user_id'],0)
        record_yinpa[member['user_id']] += 1
        msg = (
            "さんが群友で涩涩するであろうヒロインは、\n",
            MessageSegment.image(file = await user_img(member["user_id"])),
            f"『{nickname}』です！"
            )
    await yinpa.finish(msg, at_sender=True)

# 查看涩涩记录

yinpa_list = on_command("涩涩记录",aliases = {"色色记录"}, permission=GROUP, priority = 90, block = True)

@yinpa_list.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    member_list = await bot.get_group_member_list(group_id = event.group_id)
    member_list.sort(key = lambda x:x["last_sent_time"] ,reverse = True)
    record = []
    for i in range(len(member_list)):
        nickname = member_list[i]['card'] if member_list[i]['card'] else member_list[i]['nickname']
        global record_yinpa
        times = record_yinpa.get(member_list[i]['user_id'],0)
        if times:
            record.append([nickname,times])
    else:
        record.sort(key = lambda x:x[1],reverse = True)

    msg_list =[]
    msg ="Top80：\n——————————————\n"
    for i in range(len(member_list[:80])):
        nickname = member_list[i]['card'] if member_list[i]['card'] else member_list[i]['nickname']
        msg += f"{nickname}\n"
    else:
        output = text_to_png(msg[:-1])
        msg_list.append(
            {
                "type": "node",
                "data": {
                    "name": "Top80",
                    "uin": event.self_id,
                    "content": MessageSegment.image(output)
                    }
                }
            )

    msg =""
    for i in range(len(record)):
        msg += f"{i+1}.【{record[i][0]}】\n        今日被透 {record[i][1]} 次\n"
    else:
        if msg:
            output = text_to_png("涩涩记录：\n——————————————\n" + msg[:-1])
            msg_list.append(
                {
                    "type": "node",
                    "data": {
                        "name": "记录",
                        "uin": event.self_id,
                        "content": MessageSegment.image(output)
                        }
                    }
                )
        else:
            pass
    await bot.send_group_forward_msg(group_id = event.group_id, messages = msg_list)

# 重置娶群友记录

@scheduler.scheduled_job("cron",hour = 0)
def _():
    global record_waifu,record_yinpa
    record_waifu = {}
    record_yinpa = {}