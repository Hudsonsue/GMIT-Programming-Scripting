# iris dataset formatting exercise 6
# G00219132 Susan Hudson
# this script opens the Iris dataset csv file
# for each line of the dataset it displays the first four values in columns of 5 characters width

with open ("irisdata.csv") as f:

     for line in f:

         print ('{:5} {:5} {:5} {:5}'.format(line.split (';')[0], line.split (';')[1], line.split(';')[2], line.split (';')[3]))

         ## note - had been getting index error messages when running, attempted to tidy up at work but did not have access to dataset. 
         ## downloaded dataset again from a different source and re wrote script printing unformatted, column by column then formatting
         ## no index errors so am assuming problem was within original dataset not my script
         ## this csv is ; seperated not 

         ## www.saedsayad.com/datasets/Iris.xls, stripping out summaries and saving as csv