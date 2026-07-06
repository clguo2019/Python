# 不用python預設房間號 自己定義房間就叫dict字典 用大花瓜

date={
    'name':'jeff',
    'en':90,
    'math':60,
    'ch':80
}

# 要叫哪個房間 方法和list一模一樣
print(date['name'])

# 分數錯了要修改
date['en']=85
print(f'{date['name']}英文考了{date['en']}分')

# 如果呼叫的房間不存在 它會在建立後直接幫你加進去
date['history']=65
print(date)
