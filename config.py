from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    waifu_cd_bye :int = 3600
    waifu_save:bool = True
    waifu_reset:bool = True
    waifu_he :int = 25
    waifu_be :int = 25
    waifu_ntr :int = 20
    yinpa_he :int = 50
    yinpa_be :int = 0
    yinpa_cp :int = 65
