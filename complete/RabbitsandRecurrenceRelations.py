def rabFib(param):
    param = param.split()
    n = int(param[0])
    k = int(param[1])
    f = []
    for x in range(n):
        if x == 0 or x == 1:
            f.append(1)
        else:
            f.append(f[x-1] + f[x-2]*k)
    # print(*f)
    print(f[-1])

rabFib("32 4")
