from XIANG import XIANG
from GUA import GUA
from YAO import YAO
from enums import Sky, Earth, Reps, Soul

def initialization():

    xiang = XIANG()
    base = GUA()
    yaos_base = [YAO() for _ in range(6)]

    xiang.flag = 1
    xiang.base = base
    xiang.year = [Sky.gui, Earth.mao]
    xiang.month = [Sky.ren, Earth.xu]
    xiang.day = [Sky.geng, Earth.xu]
    xiang.hour = [Sky.bing, Earth.xu]
    xiang.lacks = [Earth.yin, Earth.mao]
    xiang.question = '事业'

    base.yaos = yaos_base

    yaos_base[0].essence = 0
    yaos_base[0].feature = 0
    yaos_base[1].essence = 0
    yaos_base[1].feature = 1
    yaos_base[2].essence = 1
    yaos_base[2].feature = 1
    yaos_base[3].essence = 0
    yaos_base[3].feature = 0
    yaos_base[4].essence = 1
    yaos_base[4].feature = 1
    yaos_base[5].essence = 0
    yaos_base[5].feature = 1

    return xiang

xiang = initialization()

# 本卦推变卦
# 寻世应
# 寻卦宫，后纳甲
# 寻六亲
# 缺六亲
# 寻六神