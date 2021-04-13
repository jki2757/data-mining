#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:51:05 2020

@author: jaekyumkim
THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jaekyum Kim

"""

from operator import itemgetter, attrgetter
import csv

name = input("Name of the graph file: " )
output=input("Name of the output file: " )

infile = open(name,"r")
lineReadStrings = infile.readlines()

incoming={}
outgoing={}
pr = {}
pr_tmp = {}

damping = 0.85

for i in range(1,len(lineReadStrings)-1):
    tmp = lineReadStrings[i].split(" -> ")
    source = str(tmp[0]).strip()
    target = str(tmp[1]).strip()
    
    incoming.setdefault(target,[]).append(source)
    outgoing.setdefault(source,[]).append(target)
    
for each in incoming.keys():
    pr[each] = 1/len(incoming.keys())

#set up complete now run iteration
    
while True:
    
    for eachLetter in incoming.keys():
        tmp = 0

        for eachIncoming in incoming[eachLetter]:
            tmp = tmp + pr[eachIncoming] / len(outgoing[eachIncoming])
            
        #damping factor
        tmp = (1-damping)/len(incoming.keys()) + damping*tmp
        pr_tmp[eachLetter] = tmp
    
    sortedTuple = sorted(pr.items(), key=itemgetter(1))
    sortedTuple_tmp = sorted(pr_tmp.items(), key=itemgetter(1))
    
    pr = dict(pr_tmp)

    orderedLetter = [i[0] for i in sortedTuple]
    orderedLetter_tmp = [i[0] for i in sortedTuple_tmp]
    
    #print("Iterated.")
    if orderedLetter == orderedLetter_tmp:
        #print("Results converged, exit.")
        break;

rows=[]
for each in range(len(orderedLetter)-1, -1, -1):
    index = orderedLetter[each]
    temp = [orderedLetter[each] + "," + str( pr[ index ])]
    rows.append( temp )
        
        
with open(output, 'w') as file:
    writer = csv.writer(file)
    
    writer.writerow(["vertex,pagerank"])
    writer.writerows(rows)
        
file.close()        
infile.close()
        


    


    
