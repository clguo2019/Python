

fruits = ('watermelon', 'grape') 
m=(30,50)

# zip會比對組合起來
print(list(zip(fruits,m)))

# 分別綑綁 方便一筆筆查看
for i in zip(fruits,m):
    print(i)

for i in zip(fruits,m):
    print(i)
print('-'*50)

for f,m in zip(fruits,m):
    print(f'水果{f}售價{m}')



# '-'：一個減號字元。
# * 50：將這個字串重複 50 次。
# print()：把結果印出來。