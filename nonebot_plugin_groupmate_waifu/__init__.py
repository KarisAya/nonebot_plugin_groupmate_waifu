from nonebot import require, get_plugin_config
from nonebot.plugin import PluginMetadata
from clovers.config import Config as CloversConfig
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="娶群友",
    description="娶一个群友做老婆",
    usage="娶群友，透群友",
    type="application",
    config=Config,
    homepage="https://github.com/KarisAya/nonebot_plugin_groupmate_waifu",
    supported_adapters=None,
)

IMPORT_NAME = "clovers_groupmate_waifu"
PREFIX_LENGTH = len("groupmate_waifu_")
CloversConfig.environ()[IMPORT_NAME] = {k[PREFIX_LENGTH:].lower(): v for k, v in get_plugin_config(Config).model_dump().items()}
require("nonebot_plugin_clovers").client.load_plugin(IMPORT_NAME)
