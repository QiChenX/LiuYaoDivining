from enum import Enum, unique

@unique
class Sky(Enum):
    jia = '甲'
    yi = '乙'
    bing = '丙'
    ding = '丁'
    wu = '戊'
    ji = '己'
    geng = '庚'
    xin = '辛'
    ren = '壬'
    gui = '癸'

@unique
class Earth(Enum):
    zi = '子'
    chou = '丑'
    yin = '寅'
    mao = '卯'
    chen = '辰'
    si = '巳'
    wu = '午'
    wei = '未'
    shen = '申'
    you = '酉'
    xu = '戌'
    hai = '亥'

@unique
class Reps(Enum):
    guan = '官鬼'
    qi = '妻财'
    xiong = '兄弟'
    fu = '父母'
    zi = '子孙'

@unique
class Soul(Enum):
    long = '青龙'
    hu = '白虎'
    que = '朱雀'
    wu = '玄武'
    chen = '勾陈'
    she = '腾蛇'
