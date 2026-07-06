# ch10_4.py  union聯集
# 如果想知道所有夏令營成員
# 也是有兩種方式 會把重複的名字刪掉
# 哪個放前面都無所謂 交集和聯集都一樣

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)


