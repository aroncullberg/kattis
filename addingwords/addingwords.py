import sys

lines = sys.stdin.read().splitlines()

table = {}

for line in lines:
    # print(line.split()[:1], "---", line.split()[1:])
    cmd = line.split()[:1][0]
    args = line.split()[1:]
    #print("--------------------\n",cmd, args, table)
    if cmd == 'def':
        var, val = args
        #print("\tupdating talbe with", {var:val})
        table.update({var:val})
    if cmd == "calc":
        string = ""
        for arg in args:
            #print(string)
            if arg == "+":
                string += "+"
            elif arg == "-":
                string += "-"
            elif arg == "=":
                result = eval(string)
                print(' '.join(args), end=" ")
                whowaht = ""
                try:
                    whowaht = list(table.keys())[list(table.values()).index(str(result))]
                    print(whowaht)
                except:
                    print("unknown")
                break
            elif arg in table.keys():
                string += table[arg]
            else:
                print(' '.join(args), end=" unknown\n")
                break
    if cmd == "clear":
        table = {}




        