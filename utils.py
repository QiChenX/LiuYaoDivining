from GUA import GUA
from XIANG import XIANG
from YAO import YAO
from enums import Earth, PropertyPair, Reps, Sky

# 本卦推变卦
def deriveChange(xiang:XIANG):
    if xiang.flag == 1:
        change = GUA()
        xiang.change = change
        change.yaos = [YAO() for _ in range(6)]
        for i in range(len(xiang.base.yaos)):
            if xiang.base.yaos[i].feature == 0:
                change.yaos[i].feature = 0
                change.yaos[i].essence = (xiang.base.yaos[i].essence+1)%2
            else:
                change.yaos[i].feature = 1
                change.yaos[i].essence = xiang.base.yaos[i].essence


# 寻世应
def seekForEgo(xiang:XIANG):
    base = xiang.base
    yaos = base.yaos
    
    s = False
    h = False
    e = False
    if yaos[0].essence == yaos[3].essence:
        e = True
    if yaos[1].essence == yaos[4].essence:
        h = True
    if yaos[2].essence == yaos[5].essence:
        s = True
    
    if s and h and e:
        yaos[5].ego = 1
        yaos[2].other = 1
    if not (s or h or e):
        yaos[2].ego = 1
        yaos[5].other = 1
    if s and not h and not e:
        yaos[1].ego = 1
        yaos[4].other = 1
    if not s and h and e:
        yaos[4].ego = 1
        yaos[1].other = 1
    if not s and not h and e:
        yaos[3].ego = 1
        yaos[0].other = 1
    if s and h and not e:
        yaos[0].ego = 1
        yaos[3].other = 1
    if not s and h and not e:
        yaos[3].ego = 1
        yaos[0].other = 1
    if s and not h and e:
        yaos[2].ego = 1
        yaos[5].other = 1


# 纳甲
def matchSkyandEarch(xiang:XIANG):
    base = xiang.base
    innerMatch(base)
    outerMatch(base)
    if xiang.flag == 1:
        change = xiang.change
        innerMatch(change)
        outerMatch(change)


def innerMatch(g:GUA):
    sum = 0
    yaos = g.yaos
    # 计算卦宫
    for i in range(3):
        if yaos[i].essence == 1:
            sum += 2**i
    starting_point = getStartingPoint(sum, 0)
    jia = sort(starting_point, sum)
    yaos[0].najia = jia[0]
    yaos[1].najia = jia[1]
    yaos[2].najia = jia[2]


def outerMatch(g:GUA):
    sum = 0
    yaos = g.yaos
    # 计算卦宫
    for i in range(3,6):
        if yaos[i].essence == 1:
            sum += 2**(i-3)
    starting_point = getStartingPoint(sum, 1)
    jia = sort(starting_point, sum)
    yaos[3].najia = jia[0]
    yaos[4].najia = jia[1]
    yaos[5].najia = jia[2]


def getStartingPoint(sum, in_or_out):
    # in=0, out=1
    # 乾7坎2艮4震1巽6离5坤0兑3
    match sum:
        case 0:
            if in_or_out == 0:
                return [Sky.YI, Earth.WEI]
            else:
                return [Sky.GUI, Earth.CHOU]
        case 1:
            if in_or_out == 0:
                return [Sky.GENG, Earth.ZI]
            else:
                return [Sky.GENG, Earth.WU]
        case 2:
            if in_or_out == 0:
                return [Sky.WU, Earth.YIN]
            else:
                return [Sky.WU, Earth.SHEN]
        case 3:
            if in_or_out == 0:
                return [Sky.DING, Earth.SI]
            else:
                return [Sky.DING, Earth.HAI]
        case 4:
            if in_or_out == 0:
                return [Sky.BING, Earth.CHEN]
            else:
                return [Sky.BING, Earth.XU]
        case 5:
            if in_or_out == 0:
                return [Sky.JI, Earth.MAO]
            else:
                return [Sky.JI, Earth.YOU]
        case 6:
            if in_or_out == 0:
                return [Sky.XIN, Earth.CHOU]
            else:
                return [Sky.XIN, Earth.WEI]
        case 7:
            if in_or_out == 0:
                return [Sky.JIA, Earth.ZI]
            else:
                return [Sky.REN, Earth.WU]
        case _:
            return [Sky.REN, Earth.WU]


def sort(starting_point, sum):
    jia1 = [starting_point[0]]
    jia2 = [starting_point[0]]
    jia = [starting_point, jia1, jia2]

    earth = starting_point[1]
    enum = list(Earth.__members__.values())
    starting_index = enum.index(earth)
    # 7\2\4\1顺序，6\5\0\3逆序
    if sum in [1,2,4,7]:
        e1 = (starting_index + 2)%12
        e2 = (starting_index + 4)%12
    else:
        e1 = (starting_index - 2)%12
        e2 = (starting_index - 4)%12
    earth1 = Earth(enum[e1])
    earth2 = Earth(enum[e2])
    jia1.append(earth1)
    jia2.append(earth2)
    return jia


# 寻六亲
def seekForReps(xiang:XIANG):
    xiang.origin = seekForOrigin(xiang.base)
    property = 5
    # 乾、兑属金
    if xiang.origin in [7, 3]:
        property = 0
    # 坎属水
    elif xiang.origin in [2]:
        property = 1
    # 艮、坤属土
    elif xiang.origin in [4, 0]:
        property = 2
    # 震、巽属木
    elif xiang.origin in [1, 6]:
        property = 3
    # 离属火
    else:
        property = 4
    for yao in xiang.base.yaos:
        findReps(property, yao)
    if xiang.flag == 1:
        for yao in xiang.change.yaos:
            findReps(property, yao)


def seekForOrigin(g:GUA):
    yaos = g.yaos
    s = (yaos[2].essence==yaos[5].essence)
    h = (yaos[1].essence==yaos[4].essence)
    e = (yaos[0].essence==yaos[3].essence)
    # 乾7坎2艮4震1巽6离5坤0兑3
    sum = 0
    if s and not h and e:
        for i in range(3):
            if yaos[i].essence == 1:
                sum += 2**i
    else:
        ego = 0
        for i in range(6):
            if yaos[i].ego == 1:
                ego = i
                break
        if ego <= 2:
            for i in range(3):
                if yaos[i+3].essence == 1:
                    sum += 2**i
        else:
            for i in range(3):
                if yaos[i].essence == 0:
                    sum += 2**i
    return sum


def findReps(property, yao:YAO):
    # 金0木3水1火4土2
    earth = yao.najia[1]
    pair = [property, earth]
    if pair in PropertyPair.GUAN.value:
        yao.representation = Reps.GUAN
    elif pair in PropertyPair.QI.value:
        yao.representation = Reps.QI
    elif pair in PropertyPair.XIONG.value:
        yao.representation = Reps.XIONG
    elif pair in PropertyPair.FU.value:
        yao.representation = Reps.FU
    else:
        yao.representation = Reps.ZI


# 缺六亲
def seekForDefects(xiang:XIANG):
    base = xiang.base
    reps_set = set()
    for y in base.yaos:
        reps_set.add(y.representation)
    all_reps = {Reps.FU, Reps.GUAN, Reps.XIONG, Reps.ZI, Reps.QI}
    xiang.defects = list(all_reps-reps_set)


# 寻六神
def seekForSouls(xiang:XIANG):
    return 0

# 输出
def show(xiang:XIANG):
    base = xiang.base
    showGUA(base)
    if xiang.flag == 1:
        print('')
        print('~~~~~~~~~~')
        print('')
        change = xiang.change
        showGUA(change)
    print('缺六亲：'+str([d.value for d in xiang.defects]))


def showGUA(g:GUA):
    for i in range(5, -1, -1):
        y = g.yaos[i]
        showYAO(y)


def showYAO(y:YAO):
    line = ''
    line += y.representation.value
    line += y.najia[0].value
    line += y.najia[1].value
    if y.essence == 0:
        line += '----  ----'
    else:
        line += '----------'
    if y.feature == 0:
        line += '  变'
    if y.ego == 1:
        line += ' 世'
    if y.other == 1:
        line += ' 应'
    print(line)