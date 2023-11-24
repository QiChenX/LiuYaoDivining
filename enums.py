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

@unique
# 金0木3水1火4土2
class PropertyPair(Enum):
    GUAN = [[0, Earth.WU], [0, Earth.SI], [1, Earth.CHEN], [1, Earth.XU], [1, Earth.CHOU], [1, Earth.WEI], 
            [2, Earth.YIN], [2, Earth.MAO], [3, Earth.SHEN], [3, Earth.YOU], [4, Earth.HAI], [4, Earth.ZI]]
    QI = [[0, Earth.YIN], [0, Earth.MAO], [1, Earth.SI], [1, Earth.WU], [2, Earth.HAI], [2, Earth.ZI], 
            [3, Earth.CHEN], [3, Earth.XU], [3, Earth.CHOU], [3, Earth.WEI], [4, Earth.SHEN], [4, Earth.YOU]]
    XIONG = [[0, Earth.SHEN], [0, Earth.YOU], [1, Earth.ZI], [1, Earth.HAI], [2, Earth.CHEN], [2, Earth.XU], 
            [2, Earth.WU], [2, Earth.WEI], [3, Earth.YIN], [3, Earth.MAO], [4, Earth.SI], [4, Earth.WU]]
    FU = [[0, Earth.CHEN], [0, Earth.XU], [0, Earth.CHOU], [0, Earth.WEI], [1, Earth.SHEN], [1, Earth.YOU], 
          [2, Earth.SI], [2, Earth.WU], [3, Earth.HAI], [3, Earth.ZI], [4, Earth.YIN], [4, Earth.MAO]]
    ZI = [[0, Earth.HAI], [0, Earth.ZI], [1, Earth.YIN], [1, Earth.MAO], [2, Earth.SHEN], [2, Earth.YOU], 
          [3, Earth.SI], [3, Earth.WU], [4, Earth.CHEN], [4, Earth.XU], [4, Earth.CHOU], [4, Earth.WEI], ]