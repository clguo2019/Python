# for迴圈 定數迴圈


# 讓user連續輸入5個數字 根據輸入結果
# 確認裡面是奇數的加總結果
# 確認裡面是偶數的加總結果
# 確認大於10的加總結果



odd=[]  # 奇數籃子
even=[]  # 偶數籃子
over10=[]  # 大於十籃子

for i in range(5):
    user=int(input())
    if user%2 ==0:
        even.append(user)
    else:
        odd.append(user)
    if user>10:
        over10.append(user)
print("奇數加總:",sum(odd))
print("偶數加總:",sum(even))
print("大於10加總:",sum(over10))






