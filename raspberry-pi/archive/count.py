def COUNT(arr):
    count_zeros = 0
    count_ones = 0
    for num in arr:
        if num == 0:
            count_zeros += 1
        elif num == 1:
            count_ones += 1

    print(f"0数量: {count_zeros}, 1数量: {count_ones}")

answer = input("请输入一系列的0和1，用逗号分隔: ")
arr = [int(num) for num in answer.split(',')]

COUNT(arr)