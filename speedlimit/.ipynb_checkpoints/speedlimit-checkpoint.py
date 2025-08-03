while True:
    n = int(input())
    
    if n == -1:
        break
    
    sum = 0 
    lst = 0
    for _ in range(n):
        speed, hours = map(int, input().split())
        sum += speed * (hours-lst)
        # print(sum, speed, hours-lst)
        lst = hours
    print(sum, "miles")