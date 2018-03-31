with open ("iris.csv") as f:
    for line in f:
<<<<<<< HEAD:openfile.py
        print ('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
=======
        print ('{:2} {:2} {:2} {:2}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3], end=' '))
>>>>>>> 09af162ca87f6f26975e4bbbeb8fd1a4a8bb1146:irisformat.py
