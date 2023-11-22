from enum import Enum, unique

@unique
class Sky(Enum):
    JIA = '甲'
    YI = '乙'
    BING = '丙'
    DING = '丁'
    WU = '戊'
    JI = '己'
    GENG = '庚'
    XIN = '辛'
    REN = '壬'
    GUI = '癸'

@unique
class Earth(Enum):
    ZI = '子'
    CHOU = '丑'
    YIN = '寅'
    MAO = '卯'
    CHEN = '辰'
    SI = '巳'
    WU = '午'
    WEI = '未'
    SHEN = '申'
    YOU = '酉'
    XU = '戌'
    HAI = '亥'

@unique
class Reps(Enum):
    GUAN = '官鬼'
    QI = '妻财'
    XIONG = '兄弟'
    FU = '父母'
    ZI = '子孙'

@unique
class Soul(Enum):
    LONG = '青龙'
    HU = '白虎'
    QUE = '朱雀'
    WU = '玄武'
    CHEN = '勾陈'
    SHE = '腾蛇'
