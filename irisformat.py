# iris dataset formatting exercise 6
# G00219132 Susan Hudson 
# this script opens the Iris dataset csv file
# for each line of the dataset it displays the first four values in columns of 5 characters width

with open ("iris.csv") as f:
    for line in f:
        print ('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
        
        #whilst this returns data it does also contain an index error