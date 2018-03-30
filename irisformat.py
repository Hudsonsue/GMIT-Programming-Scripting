with open ("iris.csv") as f:
    for line in f:
        print ('{:2} {:2} {:2} {:2}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3], end=' '))
