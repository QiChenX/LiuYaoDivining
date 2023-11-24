from XIANG import XIANG
from GUA import GUA
from YAO import YAO
from enums import Sky, Earth
import utils

def initialization():

    xiang = XIANG()
    base = GUA()
    yaos_base = [YAO() for _ in range(6)]

    xiang.flag = 1
    xiang.base = base
    xiang.year = [Sky.GUI, Earth.MAO]
    xiang.month = [Sky.REN, Earth.XU]
    xiang.day = [Sky.GENG, Earth.XU]
    xiang.hour = [Sky.BING, Earth.XU]
    xiang.lacks = [Earth.YIN, Earth.MAO]
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
utils.deriveChange(xiang)
# 寻世应
utils.seekForEgo(xiang)
# 纳甲
utils.matchSkyandEarch(xiang)
# 寻卦宫，定六亲
utils.seekForReps(xiang)
# 缺六亲
utils.seekForDefects(xiang)
# 寻六神
utils.seekForSouls(xiang)
# 输出
utils.show(xiang)