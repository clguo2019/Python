# ch10_9.py add
# 增加後不會照次序排

cities = { 'Taipei', 'Beijing', 'Tokyo'}
# 增加一般元素
cities.add('Chicago')
print('cities集合內容 ', cities)
# 增加已有元素並觀察執行結果
cities.add('Beijing')
print('cities集合內容 ', cities)
# 增加元組元素並觀察執行結果
tup = (1, 2, 3)
cities.add(tup)
print('cities集合內容 ', cities)


