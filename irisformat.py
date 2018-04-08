# iris dataset formatting exercise 6
# G00219132 Susan Hudson Programming and Scripting.
# this script opens the Iris dataset csv file
# for each line of the dataset it displays the first four values in columns of 5 characters width
# I played around with right or left justifying (< and >), no huge difference as same number of characters in each column
# have centred as csv includes headers
# what I wanted to do was not have to split out each column with format line split but couldn't, hence the long print command
# https://pyformat.info/ and python tutorial used as well as lecture videos

with open ("irisdata.csv") as f:

     for line in f:

         print ('{:^12} {:^12} {:^12} {:^12}'.format(line.split (',')[0], line.split (',')[1], line.split(',')[2], line.split (',')[3]))

## note - had been getting index error messages when running, attempted to tidy up at work but did not have access to dataset. 
## downloaded dataset again from a different source and re wrote script printing unformatted, column by column then formatting
## no index errors so am assuming problem was within original dataset not my script
    
## used data set from www.saedsayad.com/datasets/Iris.xls, stripping out summaries and saving as csv