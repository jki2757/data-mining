# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools 
from itertools import combinations
import time

print("filename:")
filename = input() 

minsup = int(input("minimum support count: "))
output = input("output filename: ") 

start = time.time()
infile = open(filename)


linesReadString = infile.readlines()
infile.seek(0)

oneTransaction =  infile.read().split()
unsortedTransac = list(map(int, oneTransaction)) # converts to a one-liner string of transaction
candidates_list = sorted(list(dict.fromkeys(unsortedTransac))) #function removes duplicates and puts into a list sorted

whole={}
L1 = []
for eachcand in candidates_list:
    count = unsortedTransac.count(eachcand)
    if count >= minsup:
        whole[eachcand] = count
        L1.append(eachcand)
        
#print("qualified candidates listed: ", L1)
#print("before removal of unnecessary line of transaction: ", len(linesReadString))
for eachLine in linesReadString:
    convertedList = set([int(i) for i in eachLine.split()])
    
    if len(convertedList.intersection(set(L1))) == 0:
        linesReadString.remove(eachLine)
    
#print("the length after removal: ", len(linesReadString))
#convertedList = frozenset([int(i) for i in linesReadString[0].split()])
#tmp = set(convertedList).intersection(set(L1))
#print(tmp)
comb_length=2
d=whole
while True:
    proceednxt = False
    L2=[]
    d2={} #temp dictionary var i made

    for eachset in d: # breakdown into a one-liner
        if type(eachset) != int: #exception for one digits
            for eachitem in eachset:#rest of the receiving sets
                L2.append(eachitem)
        else:
            L2.append(eachset)

    L2 = list(dict.fromkeys(L2))#remove duplicates
    #print("L2: ", L2)

    for eachLine in linesReadString:
        convertedList = set([int(i) for i in eachLine.split()])
        #each line of transaction is converted into a list of integers per iterated per line

        modifed_list = sorted(list(convertedList.intersection(set(L2))))
        #list of candidates were formed by intersecting a line of transaction and
        #a set of possible candidates from previous iteration and sorted into order
        #("if not going to use all the item in a line of transaction then dont use it")
    
        C3 = list(itertools.combinations(modifed_list, comb_length))
        #this line unions and creats combinations of candidates and puts them into the list
        
        for eachcand in C3:
            index = frozenset(eachcand)
            d2[index] = d2.get(index, 0) + 1
            if d2[index] >= minsup:
                proceednxt = True
        
    for key in [key for key in d2 if int(d2[key]) < minsup]:
        del d2[key]#deletes those that didnt meet the minimum support count and proceed to next level
        

    whole.update(d2)    
    if proceednxt == False: 
        break;
    
    d = d2
    comb_length += 1

f= open(output,"w+")
for eachkey in whole:
    if type(eachkey) != int:
        tmp=sorted(list(eachkey))
        tmp = ' '.join(str(e) for e in tmp)
        print(tmp,"(",whole[eachkey],")" )
        string=str(tmp)+ " ( "+str(whole[eachkey])+" )\n"
        f.write(string)
    else:
        print(eachkey,"(",whole[eachkey],")")
        string=str(eachkey)+" ( "+str(whole[eachkey])+" )\n"
        f.write(string)
end = time.time()
print("Total Elapsed Time: ",end - start)

"""
for eachLine in linesReadString:
    convertedList = set([int(i) for i in eachLine.split()])

    modifed_list = sorted(list(convertedList.intersection(set(L1))))
    for i in range(0,len(modifed_list)-1):
        for j in range(i+1,len(modifed_list)):
            index = frozenset({modifed_list[i],modifed_list[j]})
            d[index] = d.get(index, 0) + 1
        j = i

print("before the size of d was: ",len(d))
for key in [key for key in d if int(d[key]) <= 500]:
    del d[key]
        
print("after the size of d was: ",len(d))
whole.update(d)
"""


    
        

