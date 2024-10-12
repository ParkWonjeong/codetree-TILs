a, b = tuple(map(int, input().split()))

# 2로 나누어 떨어지는 경우
# 일의 자리가 5인 경우
# 3으로 나누어 떨어지면서 9로는 나누어 떨어지지 않는 수

def whole_number_1(i):
    if i % 2 != 0:
        return whole_number_2(i)
    else:
        return False

def whole_number_2(i):
    if i % 10 != 5:
        return whole_number_3(i)
    else:
        return False

def whole_number_3(i):
    if i % 3 == 0 and i % 9 != 0:
        return False
    else:
        return True

whole_number_cnt = 0

for i in range(a, b + 1):
    if whole_number_1(i):
        whole_number_cnt += 1

print(whole_number_cnt)