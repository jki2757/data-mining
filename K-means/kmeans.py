# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.

"""
#THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTINGA TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jae Kyum Kim

import math
import operator
import collections
import numpy as np 
import random



k = 3
my_list = []
dataset = []
name = raw_input("data file name including '.data': " )
k = raw_input("number of k:  ")
k = int(k)
outputfile = raw_input("output file name including '.txt:' ")
 
infile = open(name,"r")
lineReadStrings = infile.readlines()

###########################################


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
#########################################
for eachline in lineReadStrings:
    linelist = eachline.split(',')
    for eachelement in linelist:
        if is_number(eachelement) and len(eachelement) != 0:
            my_list.append(float(eachelement))
            
    if len(my_list) != 0:
        dataset.append(list(my_list)) #pass by value of ref?
        my_list = []
    
initialization = [tuple(dataset[0])]
firstcentroid = dataset[0]


#########################################



distDict={} 
def spitDist(firstcentroid, my_list):
    distDict.clear()
    
    for eachline in dataset:
        difference = map(operator.sub, firstcentroid, eachline)
        squared = [i ** 2 for i in difference]
        listsummed = sum(squared)
        euclidean = math.sqrt(listsummed)
    
        #print("calculating distance between: ",eachline,"and",firstcentroid)
        #print("calculated euclidean for this edge: ", euclidean)
        eachline = tuple(eachline)
        if eachline not in initialization:
            distDict[tuple(eachline)] = euclidean #node that is farthest out
            maxlength = euclidean
        
    return distDict

orderedlist=[]

    
result = orderedlist
flag = 1


candidateslist = []
result = []
ans = []
#initialization process; able to locate about 3 initial sub-obtimal clusters but need more work

if k >= 2:
    for eachcluster in initialization:
        tmp=spitDist(eachcluster, my_list)
        a = sorted(tmp.items(), key=lambda x: x[1],reverse=True)
            
        candidateslist = []
            
        for eachvector in a:
            candidateslist.append(eachvector[0])#make list of candidates in sorted order
            
        if len(initialization) != 1:
            ans = []
            for eachItemI in candidateslist:
                for eachItemJ in result:
                    if eachItemI == eachItemJ:
                        ans.append(eachItemI)
            result = list(ans)

            initialization.append(ans[0])
        elif len(initialization) == 1:
            initialization.append(candidateslist[0])
            result = list(candidateslist)

        if(len(initialization) == k):
            break
"""
        
##########################################################################################
#random initial point generation; the drawback is it doesnt give consistent answer all the time
        
initialization.clear()
for i in range(0,k):
    index = random.randrange(0, len(dataset), 3)
    initialization.append(dataset[index])

"""
##########################################################################################            
def euclideanDistance(a,b):
    difference = map(operator.sub, a, b)
    squared = [i ** 2 for i in difference]
    listsummed = sum(squared)
    euclidean = math.sqrt(listsummed)
    return euclidean


assignments = collections.defaultdict(list)

def assignEachitem(initialization):
    assignments.clear()

    for eachitem in dataset:
        d={}
        for eachcluster in initialization:
            if eachitem == eachcluster:
                continue;
            d[tuple(eachcluster)] = euclideanDistance(eachitem,eachcluster)
            #print("selected each cluster: ",eachcluster ,"to the distance to eachcluster: ", d[eachcluster])
            #print("the chosen cluster to be assigned: ",min(d, key=d.get) ,"the distance was: ", d[min(d, key=d.get)])
        assignments[tuple(min(d, key=d.get))].append(eachitem)
    return assignments

def newCluster(assignments):
    initialization = []
    for eachcluster in assignments:
        matrix = np.asarray(assignments[eachcluster])
        mean = sum(matrix)/len(assignments[eachcluster])
        initialization.append(mean.tolist())
    return initialization
#####################################################################################
    
assignments = assignEachitem(initialization) # compares each datapoint with each of new clusters
initialization = newCluster(assignments) # checks each of cluster-bucket and recalcualte the mean and assign

def silhouette(eachItemO, assignments):
    sumInCluster = 0
    for eachcluster in assignments:
        if eachItemO in assignments[eachcluster]:#detected the corresponding cluster
            for eachotheritem in assignments[eachcluster]:
                if eachItemO != eachotheritem: #if the checked item is not itself
                    sumInCluster += euclideanDistance(eachItemO, eachotheritem)
            break
            
        
    aOfZero = sumInCluster/(k-1)
    
    tmpset = set()
    
    exclusiveSum = 0
    for eachLine in assignments:
        if eachItemO != eachLine:
            for eachList in assignments[eachLine]:
                exclusiveSum += euclideanDistance(eachItemO, eachList)
            tmpset.add((exclusiveSum/k))
    bOfZero = min(tmpset)
    
    answer = (bOfZero - aOfZero)/ max([aOfZero,bOfZero])
    
    return answer
    

def sse(assignments):
    sse = 0
    for eachcluster in assignments:
        withinClusterVar = 0
        for eachItem in assignments[eachcluster]:
            dist = euclideanDistance(list(eachcluster), eachItem)
            squared = dist * dist
            withinClusterVar += squared
        sse += withinClusterVar
    return sse
while True:
    
    checker = 0
    compareBin = dict(assignments)
    assignments = assignEachitem(initialization) # compares each datapoint with each of new clusters
    SumSqerr = sse(assignments)
    print("SSE must decrease until minimized: ", SumSqerr)
    """
    for eachComparebin in compareBin:
        for eachAssignments in assignments:
            eachComparebin = set(eachComparebin)
            eachAssignments = set(eachAssignments)
            
            if all(i in eachComparebin for i in eachAssignments):
                checker += 1
                break
            else: continue
    """
        
    oldinitialization = initialization

    if checker == k:
        break
    initialization = newCluster(assignments) # checks each of cluster-bucket and recalcualte the mean and assign
    if all(i in oldinitialization for i in initialization):
        break
total = 0

for eachItem in dataset:
    total += silhouette(eachItem, assignments)
    
total = total/len(dataset)

indexing = {}
idx =0
for eachcluster in assignments:
    indexing[frozenset(eachcluster)] = str(idx)
    idx += 1


outF = open(outputfile, "w")

for eachdata in dataset:
    for eachclusterpt in assignments:
        if eachdata in assignments[eachclusterpt]:
            print(indexing[frozenset(eachclusterpt)])
            idxBuffer = indexing[frozenset(eachclusterpt)]
            outF.write(idxBuffer)
            outF.write("\n")

            break

print("Silhouette: ", total)
outF.write("Silhouette: ")
totals = str(total)
outF.write(totals)

print("SSE: ", SumSqerr)
outF.write("SSE: ")
SumSqerrs = str(SumSqerr)
outF.write(SumSqerrs)









    

    
    

        

        
        
            
    




