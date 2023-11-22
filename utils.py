from GUA import GUA
from XIANG import XIANG
from YAO import YAO

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


# 寻卦宫，后纳甲
def matchSkyandEarch(xiang:XIANG):
    return 0

# 寻六亲
def seekForReps(xiang:XIANG):
    return 0

# 缺六亲
def seekForDefects(xiang:XIANG):
    return 0

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


def showGUA(g:GUA):
    for i in range(5, -1, -1):
        y = g.yaos[i]
        showYAO(y)

def showYAO(y:YAO):
    line = ''
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