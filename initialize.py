from XIANG import XIANG
from GUA import GUA
from YAO import YAO
from enums import Sky, Earth
import hashlib
import random
from lunar_python import Solar
import datetime

def initialization():

    xiang = XIANG()
    base = GUA()
    yaos_base = [YAO() for _ in range(6)]
    xiang.question = input('所占何事：')
    xiang.sex = input('卦主性别：')

    random_res = getRandomList(xiang.question, xiang.sex)
    for i in range(6):
        transfer(yaos_base[i], random_res[i])

    if 0 in random_res or 3 in random_res:
        xiang.flag = 1
    xiang.base = base

    setDate(xiang)

    base.yaos = yaos_base

    return xiang


def getRandomList(question, sex):
    my_string = question + sex + str(datetime.datetime.now())
    my_bytes = str.encode(my_string)
    my_hash = hashlib.sha256(my_bytes).hexdigest()
    seed = int(my_hash, 16)
    random.seed(seed)
    random_list = [random.randint(0, 10000)%4 for _ in range(6)]
    return random_list


def transfer(y:YAO, integer):
    # 0老阴1少阴2少阳3老阳
    match integer:
        case 0:
            y.essence = 0
            y.feature = 0
        case 1:
            y.essence = 0
            y.feature = 1
        case 2:
            y.essence = 1
            y.feature = 1
        case 3:
            y.essence = 1
            y.feature = 0
        case _:
            return


def setDate(xiang:XIANG):
    current = datetime.datetime.now()
    lunar = Solar.fromYmdHms(current.year, current.month, current.day, 
                             current.hour, current.minute, current.second).getLunar()
    date = lunar.getEightChar()
    year = date.getYear()
    month = date.getMonth()
    day = date.getDay()
    hour = date.getTime()
    lacks = date.getDayXunKong()

    xiang.year = [matchSkyEnum(year[0]), matchEarthEnum(year[1])]
    xiang.month = [matchSkyEnum(month[0]), matchEarthEnum(month[1])]
    xiang.day = [matchSkyEnum(day[0]), matchEarthEnum(day[1])]
    xiang.hour = [matchSkyEnum(hour[0]), matchEarthEnum(hour[1])]
    xiang.lacks = [matchEarthEnum(lacks[0]), matchEarthEnum(lacks[1])]


def matchSkyEnum(s:str):
    return Sky(s)


def matchEarthEnum(e:str):
    return Earth(e)