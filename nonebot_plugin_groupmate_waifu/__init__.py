from clovers.core.plugin import PluginLoader
from nonebot_plugin_clovers import clovers
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="娶群友",
    description="娶一个群友做老婆",
    usage="娶群友，透群友",
    type="application",
    homepage="https://github.com/KarisAya/nonebot_plugin_groupmate_waifu",
    supported_adapters={"nonebot.adapters.onebot.v11"},
)


def load_plugin(name: str):
    plugin = PluginLoader.load(name)
    if plugin is None:
        logger.error(f"未找到{name}")
    elif plugin not in clovers.plugins:
        clovers.plugins.append(plugin)
        logger.success(f"{name}加载成功")
    else:
        logger.success(f"{name}已存在")


load_plugin("clovers_apscheduler")
load_plugin("clovers_groupmate_waifu")
