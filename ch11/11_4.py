# 利用function


# 加法
def add(a, b):
    return a + b

# 減法
def subtract(a, b):
    return a - b

# 乘法
def multiply(a, b):
    return a * b

# 除法
def divide(a, b):
    if b == 0:
        return "錯誤：除數不能為 0！"
    return a / b

# 主程式
# 如果這個檔案是當作一個工具給其他檔案引用
# 就不會跑main了
# 可以參考課本13-7

def main():
    num1 = 20
    num2 = 5

    print(f"加法：{num1} + {num2} = {add(num1, num2)}")
    print(f"減法：{num1} - {num2} = {subtract(num1, num2)}")
    print(f"乘法：{num1} × {num2} = {multiply(num1, num2)}")
    print(f"除法：{num1} ÷ {num2} = {divide(num1, num2)}")

# 執行主程式
if __name__ == "__main__":
    main()