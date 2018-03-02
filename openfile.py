with open ("iris.csv") as f:
    for line in f:
        print ('{:2d} {:2d} {:2d} {:2d}'.format(line.split(',')[:4], end=' '))