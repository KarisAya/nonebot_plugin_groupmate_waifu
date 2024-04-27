from nonebot.plugin import PluginMetadata
from nonebot_plugin_clovers import clovers
__plugin_meta__ = PluginMetadata(
    name="娶群友",
    description="娶一个群友做老婆",
    usage="娶群友，透群友",
    type="application",
    homepage="https://github.com/KarisAya/nonebot_plugin_groupmate_waifu",
    supported_adapters={"nonebot.adapters.onebot.v11"},
)
clovers.load_plugin("clovers_apscheduler")
clovers.load_plugin("clovers_groupmate_waifu")
