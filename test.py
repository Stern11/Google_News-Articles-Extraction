import csv

newDict=[{'a':1, 'b':2},{'a':3,'b':4}]
A=[{'a':5, 'b':6},{'a':7,'b':8}]

for i in range(len(A)):
    newDict.append(A[i])
print(newDict)

for i in range(0,2):
    with open('file1.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['a','b'])
        writer.writeheader()
        writer.writerows(newDict)
        

