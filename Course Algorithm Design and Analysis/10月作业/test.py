# 输入示例："1  2 3 4 "
numbers = input().split()  # split() 会自动去除多余的空格并分割数字
numbers_list = list(map(int, numbers))  # 使用 map 将字符串转换为整数

print(numbers_list)
