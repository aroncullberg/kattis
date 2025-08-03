pool = dict()
for _ in range(int(input())):
    Name, Prio, Date = input().split()
    if Date in pool.keys():
        #print(f"found {Name} with prio {Prio} at date {Date} in pool, comparing to {pool[Date]}")
        if int(pool[Date][1]) < int(Prio):
            pool.update({Date: (Name, Prio)})
    else:
        pool.update({Date: (Name, Prio)})

print(len(pool.values()),"\n" + '\n'.join(sorted([name for name, prio in pool.values()])))