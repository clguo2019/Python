'''
TQC+ 程式語言Python 710 詞典搜尋

1. 題目說明:
請開啟PYD710.py檔案，依下列題意進行作答，為一詞典輸入資料並進行搜尋，使輸出值符合題意要求。作答完成請另存新檔為PYA710.py再進行評分。

2. 設計說明：
請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再輸入一鍵值並檢視此鍵值是否存在於該詞典中。

3. 輸入輸出：
輸入說明
先輸入一個詞典，直至end結束輸入，再輸入一個鍵值進行搜尋是否存在

輸出說明
鍵值是否存在詞典中

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Key: 123-4567-89
Value: Jennifer
Key: 987-6543-21
Value: Tommy
Key: 246-8246-82
Value: Kay
Key: end
Search key: 246-8246-82
True
'''
d = dict()
while True:
    key = input('Key: ')
    if key == 'end': break
    value = input('Value: ')
    d[key] = value
k = input('Search key: ')
print(k in d)


d = dict #{}
while True:
    key ==input('key:')
    if key =='end':
        break
    else:
        value=input('value:')
        d=[key]=value

print(d)    

# 前面迴圈結束 代表資料收集完全
# 後面還有一步驟 要搜尋目標key

target=input('search key: ')
# 有了目標key 就問它在不在d裡面
# (in d)和(in d.key())是一樣意思
print(target in d)