# ch10_3.py  intersection 交集
# 我現在手上有兩份名單 分別屬於兩個夏令營
# 我現在用set建立名單 第一裡面就不會有重名狀況
# 第二我要合併出總名單就很簡單




math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員

# 我想知道同時參加兩個營隊的人
# 就可以用set做交集
# 第一種寫法用符號& 就是and的意思
# 第二種寫法是用 .intersecsion 用用前面的去交集()內的 做比對


both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)


