# 9-2-1 items

date={
    'name':'jeff',
    'en':90,
    'math':60,
    'ch':80
}

# 一般來說 直接把dist拿來用for迴圈 掃描一下
# 看到的就是key值
# 把key帶回你的dict就可以找到裡面住誰
# 而且根據key就可以找到應對的不同處理方式
for i in date:
    if i =='name':
        print(f'這個學生是{date[i]}')
    else:
        print(f'這個學生是{i}成績是{date[i]}')
# 針對dict的鑑值對資料 可以直接讓你把values取出來
for v in date.values:
    print(v)

# items就會把每一組鍵值打包起來給你
for key.values in date.items():
    print(f'{key}位置的值是{value}')

    # print(f'現在找到的key是{i} 裡面的值是{date[i]}')



