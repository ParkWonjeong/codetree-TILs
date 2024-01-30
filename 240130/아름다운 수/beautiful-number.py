n = int(input()) # n 자릿수의 아름다운 수
beautiful = 0 # 아름다운 수의 개수

def beautiful_num(cnt):
    if cnt == n:
        global beautiful
        beautiful += 1
        return
    
    for num in range(1, 5):
        if cnt + num > n:
            return
        
        beautiful_num(cnt + num)

beautiful_num(0)
print(beautiful)