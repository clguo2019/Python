# ch10_5.py difference差集
# 用差集就有先後次序的問題
# 參加這個沒參加那個的人
# 蝴蝶翅膀兩邊 中間沒有交集的 另外一個符號的寫法 
# len就是問基數 長度 裡面有多少個元素

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
result=math.symmetric_difference(physics)
print(result)

print(len(a))
