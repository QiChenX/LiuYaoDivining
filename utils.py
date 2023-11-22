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
    return 0


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
    print(line)