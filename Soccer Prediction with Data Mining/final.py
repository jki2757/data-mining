#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:37:37 2020

@author: jaekyumkim
"""
import math
import operator
import collections
import numpy as np 
import random

infile = open("2015:2016_EPL_Matches.csv","r")
matches = infile.readlines()

infile = open("Player_Recent_Form.csv","r")
players = infile.readlines()

players_dict = {}
Team_Virtual_Features = []
count = 1

for i in range(1, len(players)):
    players_vector = players[i].split(",")
    players_dict[ players_vector[0] ] = [ players_vector[i] for i in range(4, len(players_vector) ) ]

for i in range(1,len(matches)):
    #print("Match "+str(count)+" added")
    count+=1
    
    match_vector = matches[i].split(",")
    
    Attacking = []
    Attack_aggregate=[]
    Skills = []
    Skills_aggregate=[]
    Movement = []
    Movement_aggregate=[]
    Power = []
    Power_aggregate=[]
    Mentality = []
    Mentality_aggregate=[]
    Defending = []
    Defending_aggregate=[]
    Goalkeeping = []
    
    for eachplayer in range(4,15):
        #if no such player exists, i.e. youth player who is not registered
        if(match_vector[eachplayer] == ''):
            continue;
        
        if(eachplayer == 4):
            Goalkeeping = [int(players_dict[match_vector[eachplayer]][j]) for j in range(28,33)]
            continue;
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(0,5)]
        Attacking.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(5,10)]
        Skills.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(10,15)]
        Movement.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(15,20)]
        Power.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(20,25)]
        Mentality.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer]][j]) for j in range(25,28)]
        Defending.append(tmp)
    
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Attacking)):
            tmp.append(Attacking[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,4)])/4 
        Attack_aggregate.append(tmp)

    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Skills)):
            tmp.append(Skills[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5 
        Skills_aggregate.append(tmp)

    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Movement)):
            tmp.append(Movement[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Movement_aggregate.append(tmp)
        
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Power)):
            tmp.append(Power[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Power_aggregate.append(tmp)
        
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Mentality)):
            tmp.append(Mentality[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Mentality_aggregate.append(tmp)
        
    for i in range(0,3):
        tmp=[]
        for j in range(0,len(Defending)):
            tmp.append(Mentality[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,4)])/4 
        Defending_aggregate.append(tmp)
            
    #pick out best features from home team
    
    Team_Virtual_Features.append([sum(Attack_aggregate)/5] + [sum(Power_aggregate)/5] + [sum([Goalkeeping[i] for i in range(5)])/5] + [sum(Mentality_aggregate)/5]  + [sum(Defending_aggregate)/3] + [sum(Movement_aggregate)/5] + [sum(Skills_aggregate)/5])
    
    #print("Home team's Team_Virtual_Features appended")
    
    Attacking = []
    Attack_aggregate=[]
    Skills = []
    Skills_aggregate=[]
    Movement = []
    Movement_aggregate=[]
    Power = []
    Power_aggregate=[]
    Mentality = []
    Mentality_aggregate=[]
    Defending = []
    Defending_aggregate=[]
    Goalkeeping = []
    
    #print("Now append away team...")
    for eachplayer in range(15,26):
        
        if(match_vector[eachplayer] == ''): 
            continue;
            
        if(eachplayer == 15):
            Goalkeeping = [int(players_dict[match_vector[eachplayer]][j]) for j in range(28,33)]
            continue;

        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(0,5)]
        Attacking.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(5,10)]
        Skills.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(10,15)]
        Movement.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(15,20)]
        Power.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(20,25)]
        Mentality.append(tmp)
        
        tmp = [int(players_dict[match_vector[eachplayer].rstrip()][j]) for j in range(25,28)]
        Defending.append(tmp)
    
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Attacking)):
            tmp.append(Attacking[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,4)])/4 
        Attack_aggregate.append(tmp)

    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Skills)):
            tmp.append(Skills[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5 
        Skills_aggregate.append(tmp)

    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Movement)):
            tmp.append(Movement[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Movement_aggregate.append(tmp)
        
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Power)):
            tmp.append(Power[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Power_aggregate.append(tmp)
        
    for i in range(0,5):
        tmp=[]
        for j in range(0,len(Mentality)):
            tmp.append(Mentality[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,5)])/5
        Mentality_aggregate.append(tmp)
        
    for i in range(0,3):
        tmp=[]
        for j in range(0,len(Defending)):
            tmp.append(Mentality[j][i])
        tmp.sort(reverse=True)
        tmp = sum([tmp[k] for k in range(0,4)])/4 
        Defending_aggregate.append(tmp)
    
    Team_Virtual_Features.append([sum(Attack_aggregate)/5] + [sum(Power_aggregate)/5] + [sum([Goalkeeping[i] for i in range(5)])/5] + [sum(Mentality_aggregate)/5]  + [sum(Defending_aggregate)/3] + [sum(Movement_aggregate)/5] + [sum(Skills_aggregate)/5])
    #print("Away team's Team_Virtual_Features appended")

#Normalize
for i in range(0, len(Team_Virtual_Features)):
    total = sum(Team_Virtual_Features[i])
    for j in range(0, len(Team_Virtual_Features[i])):
        Team_Virtual_Features[i][j] = Team_Virtual_Features[i][j] / total
            
#Kmeans
initialization = []

for i in range(0,5):
    index = random.randrange(0, len(Team_Virtual_Features))
    initialization.append(Team_Virtual_Features[index])    
    
assignments = collections.defaultdict(list)

def assignEachitem(initialization):
    assignments.clear()

    for eachitem in Team_Virtual_Features:
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

def euclideanDistance(a,b):
    difference = map(operator.sub, a, b)
    squared = [i ** 2 for i in difference]
    listsummed = sum(squared)
    euclidean = math.sqrt(listsummed)
    return euclidean

assignments = assignEachitem(initialization) # compares each datapoint with each of new clusters
initialization = newCluster(assignments) # checks each of cluster-bucket and recalcualte the mean and assign

while True:
    assignments = assignEachitem(initialization) # compares each datapoint with each of new clusters
    oldinitialization = initialization
    initialization = newCluster(assignments)
    if all(i in oldinitialization for i in initialization):
        break
    
#########################

d={}
d1={}
assignments.clear()
assignments = collections.defaultdict(list)
winning_odds={}
winning_odds = collections.defaultdict(list)
match_counter = {}
match_counter = collections.defaultdict(list)
win_counter = {}
win_counter = collections.defaultdict(list)
match_history = {}
win_counter = collections.defaultdict(list)

target=[]
for i in range(1,len(matches)):
    match_vector = matches[i].split(",")
    
    home_team = match_vector[0]
    away_team = match_vector[1]
    if(match_vector[2] > match_vector[3]): win = True
    else: win = False
    
    for eachcentroid in initialization:
        d[tuple(eachcentroid)] = euclideanDistance(eachcentroid,Team_Virtual_Features[i*2-2])
        d1[tuple(eachcentroid)] = euclideanDistance(eachcentroid,Team_Virtual_Features[i*2-1])
        
    home_assigned = min(d, key=d.get)
    target.append(initialization.index(list(home_assigned)))
    away_assigned = min(d1, key=d1.get)
    target.append(initialization.index(list(away_assigned)))

    """
    if(home_assigned==away_assigned):
        print("Both team has same strategy")
        continue
    """
    
    match_index = str("Strategy: " + str(initialization.index(list(home_assigned))) + " vs. Strategy: " + str(initialization.index(list(away_assigned))))
    
    if(match_index not in match_counter):
        match_counter[match_index] = 0
    if(match_index not in win_counter):
        win_counter[match_index] = 0
    
    if(match_index not in match_history):
        match_history[match_index] = []


    match_history[match_index].append([home_team,away_team])

    if(win == True):
            win_counter[match_index] += 1
            match_counter[match_index] += 1
            winning_odds[match_index] = win_counter[match_index] / (match_counter[match_index])
    else:
            match_counter[match_index] += 1
            winning_odds[match_index] = win_counter[match_index] / (match_counter[match_index])
    
    #print(match_index)
    #print("Home team won? :" + str(win))
    #print("Winning odds of home team: " + str(winning_odds[match_index]))
    

#sanity check
    
teamid={}
infile = open("teams.csv","r")
teamline = infile.readlines()

for i in range(len(teamline)):
    team_vector = teamline[i].split(",")
    teamid[team_vector[0]] = team_vector[1]

for each in winning_odds:
    print(each+"'s winning probability: "+str(winning_odds[each]))

for eachstrategy in match_history:
    print("Games that have played in these two strategies: "+eachstrategy)
    for eachgame in match_history[eachstrategy]:
        print( teamid[eachgame[0]].rstrip() +" vs. "+ teamid[eachgame[1]].rstrip() )
    print("\n")
        
    
success=0
for i in range(1,len(matches)):
    match_vector = matches[i].split(",")
    
    home_team = match_vector[0]
    away_team = match_vector[1]
    if(match_vector[2] > match_vector[3]): win = True
    else: win = False
    
    for eachcentroid in initialization:
        d[tuple(eachcentroid)] = euclideanDistance(eachcentroid,Team_Virtual_Features[i*2-2])
        d1[tuple(eachcentroid)] = euclideanDistance(eachcentroid,Team_Virtual_Features[i*2-1])
    home_assigned = min(d, key=d.get)
    away_assigned = min(d1, key=d1.get)
    
    """
    if(home_assigned==away_assigned):
        print("Both team has same strategy")
        continue
    """
    
    match_index = str("Strategy: " + str(initialization.index(list(home_assigned))) + " vs. Strategy: " + str(initialization.index(list(away_assigned))))
    
    if(win == True):
        if(winning_odds[match_index] > 0.5):
            success += 1
    if(win == False):
        if(winning_odds[match_index] <= 0.5):
            success += 1
print("My prediction's success rate if applied to my own data: " +str(success/380))


#########################
#visualization
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

x = pd.DataFrame(Team_Virtual_Features) 
x = StandardScaler().fit_transform(x)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

y = pd.DataFrame(target, columns=['target']) 

finalDf = pd.concat([principalDf, y['target']], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title("2 component PCA of players' attributes", fontsize = 20)
targets = [0,1,2,3,4]
colors = ['r', 'g', 'b','y','purple']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()



        
        

