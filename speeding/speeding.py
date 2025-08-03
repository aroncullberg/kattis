snapshots = []
for _ in range(int(input())):
    snapshots.append([*map(int, input().split())])
    
maxspeed = 0
lasttime=0
for time, distance in snapshots:
    print("\n", time, distance, lasttime, end=" ")
    
    print(time, lasttime)
    speed = distance/(time-lasttime)
    if speed > maxspeed:
        maxspeed = speed
    if lasttime == 0:
        print(lasttime, "is 0 settin git to", time)
        lasttime = time
        continue
print(maxspeed)