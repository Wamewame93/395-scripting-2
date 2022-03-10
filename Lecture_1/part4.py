#variables
arrValues = [5, 7, 5, -5, 1, 23, 8]
highest = int
lowest = int
i=0
#print the array to visualize the values
print (arrValues)
#loop the array
for x in arrValues:
    #set first value
    if i==0:
        highest = x
        lowest = x
    #set highest and lowest value
    if x>highest:
        highest=x
    elif x<lowest:
        lowest
    #itterate next loop
    i+=1
#lowest and highest result put into a tuple
result = (lowest,highest)
print (result)
print (type(result))