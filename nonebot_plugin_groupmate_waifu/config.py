from pydantic import BaseModel


class Config(BaseModel):
    groupmate_waifu_fontname: str = "simsun"
    groupmate_waifu_fallback_fonts: list[str] = [
        "Arial",
        "Tahoma",
        "Microsoft YaHei",
        "Segoe UI",
        "Segoe UI Emoji",
        "Segoe UI Symbol",
        "Helvetica Neue",
        "PingFang SC",
        "Hiragino Sans GB",
        "Source Han Sans SC",
        "Noto Sans SC",
        "Noto Sans CJK JP",
        "WenQuanYi Micro Hei",
        "Apple Color Emoji",
        "Noto Color Emoji",
    ]

    groupmate_waifu_waifu_path: str = "./data/waifu/"
    """文件记录存档路径"""
    groupmate_waifu_waifu_reset: bool = True
    """是否每日重置cp记录"""
    groupmate_waifu_at_listen: bool = True
    """是否监听 at 事件"""
    groupmate_waifu_waifu_he: int = 40
    """指定成功概率"""
    groupmate_waifu_waifu_be: int = 20
    """指定失败概率"""
    groupmate_waifu_waifu_ntr: int = 50
    """NTR概率"""
    groupmate_waifu_happy_end_tips: list[str] = [
        "好耶~",
        "婚礼？启动！",
        "需要咱主持婚礼吗qwq",
        "不许秀恩爱！",
        "(响起婚礼进行曲♪)",
        "比翼从此添双翅，连理于今有合枝。\n琴瑟和鸣鸳鸯栖，同心结结永相系。",
        "金玉良缘，天作之合，郎才女貌，喜结同心。",
        "繁花簇锦迎新人，车水马龙贺新婚。",
        "乾坤和乐，燕尔新婚。",
        "愿天下有情人终成眷属。",
        "花团锦绣色彩艳，嘉宾满堂话语喧。",
        "火树银花不夜天，春归画栋双栖燕。",
        "红妆带绾同心结，碧树花开并蒂莲。",
        "一生一世两情相悦，三世尘缘四世同喜",
        "玉楼光辉花并蒂，金屋春暖月初圆。",
        "笙韵谱成同生梦，烛光笑对含羞人。",
        "祝你们百年好合,白头到老。",
        "祝你们生八个。",
    ]
    """成功提示列表"""
    groupmate_waifu_bad_end_tips: list[str] = [
        "你没有娶到群友，强者注定孤独，加油！",
        "找不到对象.jpg",
        "雪花飘飘北风萧萧～天地一片苍茫。",
        "要不等着分配一个对象？",
        "恭喜伱没有娶到老婆~",
        "醒醒，伱没有老婆。",
        "哈哈哈哈哈哈哈哈哈",
        "智者不入爱河，建设美丽中国。",
        "智者不入爱河，我们终成富婆",
        "智者不入爱河，寡王一路硕博",
    ]
    """失败提示列表"""
    groupmate_waifu_waifu_last_sent_time_filter: int = 2592000
    """时间过滤"""
    groupmate_waifu_yinpa_he: int = 50
    """指定涩涩成功率"""
    groupmate_waifu_yinpa_cp: int = 80
    """指定cp涩涩成功率"""
    groupmate_waifu_bg_image: str = "./data/waifu/bg.png"
    """背景图片"""
