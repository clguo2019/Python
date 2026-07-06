# ch11_1.py fuction函數
# def 是define的意思
# def後面連接就是function的名字
# 因為有名字我們才可以重複呼叫
# 名字後面一訂有() 那就是function投料孔
# 這代表我可以重複呼叫 不用一直做一樣的事
# 


def greeting():
    """我的第一個Python函數設計"""
    print("Python歡迎你")
    print("祝福學習順利")
    print("謝謝")

# 以下的程式碼也可稱主程式
greeting()
greeting()
greeting()
#光只是叫它的名字 它是不會動的
# 要加上() 那就好像鑰匙孔一樣

# 投料孔放入的參數 可以想像要建立一個參數給 mark參考的
# 投料孔可以區分
# reture 可以回傳到主程式(貼牆的那些)
# none就是沒有東西
# function沒有寫retune python會自動幫你retune none
# 課本5-11

def mark(day,課):
    print(f'{day}看見我了?')
    print(f'我也在那學{課}')
    return f'user 輸入日期{day},那上{課}'
print(mark("明天","程式語言"))
mark('昨天','英文')
mark('前天','國文')