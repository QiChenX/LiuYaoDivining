from initialize import initialization
import utils

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