# 项目架构及设计说明

## 基础概念
爻/YAO：有老阴、少阴、老阳、少阳四种情况，其中老阴和老阳为变爻，少阴和少阳为静爻。
本卦/GUA-base：摇卦六次，每次得到一爻，从下至上排列六爻，即得本卦。
变卦/GUA-change：若本卦中包含变爻，则变爻阴阳转换，得到变卦。
卦象/XIANG：若本卦中有变爻，则本卦和变卦共同组成卦象，否则本卦自成卦象。

## 类的设计
### 爻/YAO:
essence：爻的本质，0为阴，1为阳
feature：爻的特征，0为老，1为少
ego：1为世爻
other：1为应爻
najia：纳甲，应为枚举的列表，分别表示干支
representation：六亲，应为枚举
soul：六神，应为枚举

### 卦/GUA
yaos：六爻，应为列表

### 象/XIANG
flag：0表示本卦不变，1表示本卦生变卦
base：本卦
change：变卦
origin：卦宫，乾7坎2艮4震1巽6离5坤0兑3
defects：缺失的六亲，应为列表
year：年份，应为枚举的列表，分别表示干支，下同
month：月份
day：日期
hour：时辰
lacks：空亡，应为枚举的列表，表示缺失的地支
question：所占何事
sex：卦主性别

## 起卦
### 随机数

1. 把所占事项、卦主性别以及当前时间拼接为种子字符串my_string
2. 把my_string转化为字节码my_bytes
3. 使用SHA256对my_bytes进行加密得到my_hash
4. 把my_hash转换为十进制数字作为种子输入random

### 阳历转八字

https://github.com/6tail/lunar-python/tree/master