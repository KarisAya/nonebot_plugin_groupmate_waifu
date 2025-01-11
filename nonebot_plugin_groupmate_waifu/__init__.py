from nonebot import get_driver, on_message
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata
from nonebot_plugin_clovers import extract_command
from clovers import Leaf

from nonebot_plugin_clovers.adapters.onebot.v11 import __adapter__ as adapter
from clovers_apscheduler import __plugin__ as apscheduler
from clovers_groupmate_waifu import __plugin__ as waifu

__plugin_meta__ = PluginMetadata(
    name="娶群友",
    description="娶一个群友做老婆",
    usage="娶群友，透群友",
    type="application",
    homepage="https://github.com/KarisAya/nonebot_plugin_groupmate_waifu",
    supported_adapters={"nonebot.adapters.onebot.v11"},
)

leaf = Leaf(adapter)


@leaf.adapter.call_method("group_member_list")
async def _(group_id: str, /, bot: Bot):
    info_list = await bot.get_group_member_list(group_id=int(group_id))
    for user_info in info_list:
        user_id = str(user_info["user_id"])
        user_info["group_id"] = str(user_info["group_id"])
        user_info["user_id"] = user_id
        user_info["avatar"] = f"https://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640"
    return info_list


@leaf.adapter.call_method("group_member_info")
async def _(group_id: str, user_id: str, /, bot: Bot):
    user_info = await bot.get_group_member_info(group_id=int(group_id), user_id=int(user_id))
    member_user_id = str(user_info["user_id"])
    user_info["group_id"] = str(user_info["group_id"])
    user_info["user_id"] = member_user_id
    user_info["avatar"] = f"https://q1.qlogo.cn/g?b=qq&nk={member_user_id}&s=640"
    return user_info


leaf.plugins.append(apscheduler)
leaf.plugins.append(waifu)

driver = get_driver()
driver.on_startup(leaf.startup)
driver.on_shutdown(leaf.shutdown)

main = on_message(priority=20, block=False)


@main.handle()
async def _(bot: Bot, event: MessageEvent, matcher: Matcher):
    if await leaf.response(extract_command(event.get_plaintext()), bot=bot, event=event):
        matcher.stop_propagation()
