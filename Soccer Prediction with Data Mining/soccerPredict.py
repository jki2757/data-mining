#THIS CODE IS MY OWN WORK_ GABRIEL KIM_JAEKYUM_KIM
import sqlite3
import random
import pandas as pd
from scipy.spatial import distance


def connection(sql, source):
	conn = sqlite3.connect('database.sqlite') 
	cur = conn.cursor()
	statement = sql 
	cur.execute(statement)
	result = cur.fetchall()
        return(result)

def compiler():
	sql = "SELECT * From MATCH WHERE id <1200 "
	src = "MATCH"
	sql1 = "SELECT * From Player_attributes"
	src1 = "Player_attributes"
	data_1 = connection(sql, src) # MATCH
	data_2 = connection(sql1, src1) # Player_attributes

	role = ["GK","DF","MF","ATK"]
	attack = [4,10,11]
	midfielder = [4,10,15]
	defense = [4,15,18]
	goalkeeper = [4,37,41]
	total_ = [goalkeeper,defense,midfielder,attack]
	kvalue = 3

	############ Function begins here ############

	matchAttributes_ = matchAttributes(data_1)
        print("finished matchAttributes!")
	abilityExtract = playerAbilityExtract(matchAttributes_, data_2, role, total_)
        print("finished playerAbilityExtract!")
	criteria = criteriaMaker(abilityExtract, role, kvalue)
        print("almost! just finihsed making criteria!")

	prediction = playerComparison(criteria, matchAttributes_, data_2, role, total_)
	returnVal = winloseChecked(matchAttributes_, prediction)
        return(returnVal)
def matchAttributes(inputD):
    match = inputD

    temp = []
    a = [0,6,7,8,9,10]
    count = 0
    for each in match:
        both = []
        checker = 0 
        t = []
        count += 1
        homeTeam = []
        awayTeam = []
        homeCoordinates = []
        awayCoordinates = []
        homeFormation = []
        awayFormation = []
        tp = []
        win = []
        for _ in a: 
            tp.append(each[_])
        both.append(tp)
        if each[9] == None or each[10] == None:
            win.append(0)
        elif each[9] > each[10]:
            win.append(1)
        elif each[9] < each[10]:
            win.append(2)
        elif each[9] == each[10]:
            win.append(3)
   
        for x in range(55,66):
            homeTeam.append(each[x])
        both.append(homeTeam)
        for x in range(66,77):
            awayTeam.append(each[x])
        both.append(awayTeam)
        hc = []
        ac = []
        for x in range(0,11):
            hc_x = x+11
            hc_y = x+33
            ac_x = x+22
            ac_y = x+44
            if x == 0:
                homeCoordinates.append([5.0,1.0])
                awayCoordinates.append([5.0,1.0])
            else: 
                homeCoordinates.append([each[hc_x],each[hc_y]])
                awayCoordinates.append([each[ac_x],each[ac_y]])
            homeFormation = squadFormation(homeCoordinates)
            awayFormation = squadFormation(awayCoordinates)
        both.append(homeCoordinates)
        both.append(awayCoordinates)
        both.append(homeFormation)
        both.append(awayFormation)
        both.append(win)
        temp.append(both)
    return(temp)

def squadFormation(inputList):
    formation = []
    
    for each in range(12): 
        playerCount = 0 
        for each_ in inputList: 
            if each == each_[1]:
                playerCount += 1
            else: 
                pass
        if playerCount != 0:
            
            formation.append(playerCount)
    return formation


def kmeans(kval, inputCategory, inputData):
    entireData = inputData
    inputArray = inputCategory
    k = kval
    number = 0
    finalCluster = []
    for a_ in inputArray: #parts of a #cateogories of position 
        iteration = 0
        cluster = []
        temp = []
        initCluster = []
        maxandmin = []
        for each in entireData: 
            
            p = 0
            p_ = []
            for a in a_:
                
                if each[a] is not None: 
                    
                    p_.append(each[a])
                    
                else: 
                    p=1
            if p == 0: 
                temp.append(p_)
        for a in a_: 
            tmp = []
            for each in entireData: 
                if each[a] is not None: 
                    tmp.append(each[a])
            
            maxval = max(tmp)
            minval = min(tmp)
            maxandmin.append([maxval,minval])
            
        attributeLen = len(a_)    
        for p in range(k):
            clusterTemp = []
            for p_ in range(attributeLen):
                clusterVal = random.randint(maxandmin[p_][1],maxandmin[p_][0])
                clusterTemp.append(clusterVal)
        
            initCluster.append(clusterTemp)
        
        if len(cluster) == 0:
            cluster1 = []
            for g in initCluster:        
                cluster.append(g)
        oldcluster = []
        while cluster != oldcluster:
            list1 = []
            for element in temp:
                temp0 = []
                point = [] 
                for x in cluster: 
                    d = distance.euclidean(element, x)
                    temp0.append(d)
                    minvalue = min(temp0)
                    if minvalue == d:
                        point = x
                list1.append([element,point])
            oldcluster = cluster 
            cluster = []
            for clu in oldcluster: 
                clutemp = []
                for b in range(attributeLen): 
                    sumvalue = 0
                    length = 0
                    for element in list1: 
                        if element[1] == clu: 
                            sumvalue = sumvalue + element[0][b]
                            length += 1
                    if length == 0:
                        length = 1
                    newval = sumvalue / length
                    clutemp.append(newval)
                cluster.append(clutemp)
                iteration+= 1
        
        finalCluster.append([cluster,number])
        number += 1
    return(finalCluster)

def playerSearch(player_api,player_attributes):
    theplayer = []
    for each in player_attributes: 
        if player_api == each[2]:
            theplayer = each
    return(theplayer)


def playerAbilityExtract(matchAttributes, player_attributes, role_a, total_): 
    role = role_a

    tempList = matchAttributes #players information with victory


    total = total_
    generalStats = []
    iteration = 0
    name = []
    
    for each in tempList: 
        print("on playerAbilityExtract!")
        print(iteration)

        teamStats = []

        current = 0
        if len(each[5]) == 1 or len(each[6]) == 1: 
            pass 
        for x in range(0,2):
            current = 5 + x
            playerCount = 0
            positionStats = []
            count = 0
            if len(each[current]) == 4:
                for each_ in each[current]:
                    role_ = role[count]
#                 positionStats = []
                    for x_ in range(each_):
                        api = each[x+1][playerCount]
                        name.append(api)
                   
                        playerCount += 1
                        playerInfo = playerSearch(api, player_attributes)
                        temp = []
                        if playerInfo != []:
                            for x_1 in total[count]:
                                temp.append(playerInfo[x_1])
                            positionStats.append([temp,role_]) # attributes of players passed on 
                    
                    count += 1
            elif len(each[current]) == 5: 
                for each_ in each[current]:
                    role_ = role[count]
#                 positionStats = []
                    for x_ in range(each_):
                        api = each[x+1]
                        playerCount += 1
                        playerInfo = playerSearch(api,player_attributes)
                        temp = []
                        if playerInfo != []:
                            for x_1 in total[count]:
                                temp.append(playerInfo[x_1])      
                            positionStats.append([temp,role_])
                    
                    if count != 3: 
                            count += 1    
                
                
            teamStats.append(positionStats)
        # more code to be added here 
        
        
        #statsComparison()
        
        
        #statsComparison
        generalStats.append(teamStats)
    #kmeans stats 
        
        iteration += 1
    return(generalStats)

def criteriaMaker(abilityExtract, role, kvalue): #enter generalStats from playerAbilityExtract 
    # role = ["GK","DF","MF","ATK"]
    criteria = []
    data_ = abilityExtract
    data = []
    kval = kvalue
    for x_ in range(0,4):
        positionData = []
    
        length = []
        inputList = []
        for each in data_: #  0, 1
        
            for x in each:
                for y in x:
                    if y[1] == role[x_]:
                        positionData.append(y[0])
                        attributeLen = len(y[0])
                        length.append(attributeLen)
    
        for i in range(0,max(length)):
            inputList.append(i)
        criteria_ = kmeans(kval,[inputList],positionData)
        criteria.append([criteria_,role[x_]])
    
        data.append(positionData)
    return(criteria)

def winloseChecked(matchAttr, prediction):
    resultArr = []
    resultValue = 0.0
    result = 0.0
    data = matchAttr
    predictedResult = prediction
    leng = 0
    
    for each_ in predictedResult:
        if each_[1] == 0:
                pass
        for each in data:  
            
            if each[0][1] == each_[0]:
                if each[7][0] == each_[1]:
                    resultArr.append(1)
                leng+=1
                
    result = result + sum(resultArr)
    resultLength = len(predictedResult)
    resultValue = result/resultLength 
    # resultValue = resultValue
    print(resultValue)
    return(resultValue)
def euc_distance (a1,a2): #function for euc_distance calculation
    

    t =[]
    v = 0.0
    

    len1 = len(a1)
    len2 = len(a2)
    for a in range(len1):
        v = a1[a] - a2[a]
        v = v**2
        t.append(v)
    sumV = sum(t)
    sumV = sumV ** (1/2)
    return(sumV)


                    

def playerComparison(criteria, dataInput, player_attributes, role, total_): #criteria from CriteriaMaker and dataInput from matchAttributes
    total = total_
    data = dataInput
    comparisonChart = criteria 
    generalStats = []
    iteration = 0
    name = []
    output = []
    print("safelyEntered!")
    c = 0
    cL = int(len(data)/2)
    for eachMatch in data:
        if c == cL:
            print("halfway there!")
        c+=1

        teamStats = []
        predict = []
        result = 4
        if len(eachMatch[5]) == 1 or len(eachMatch[6]) == 1: 
            # output.append([eachMatch[0][1],eachMatch[7][0]])
            output.append([eachMatch[0][1],0])
            pass 
        else:
            for x in range(0,2):
                predictionPoints = 0.0
                current = 5 + x
                playerCount = 0
                positionStats = []
                count = 0
                if len(eachMatch[current]) == 4: 
                    for each_ in eachMatch[current]: #squadFormation/eachTeam
                        role_ = role[count]
                        for x_ in range(each_): #defense, gk, mf, or attck 
                            api = eachMatch[x+1][playerCount]
                            name.append(api)
                            playerCount += 1
                            playerInfo = playerSearch(api, player_attributes)
                            temp = []
                            if playerInfo != []:
                                for x_1 in total[count]: #each player
                                    temp.append(playerInfo[x_1])
                                    
                                positionStats.append([temp,role_])
                        count += 1
                elif len(eachMatch[current]) == 5: 
                    for each_ in eachMatch[current]:
                        role_ = role[count]
#                 positionStats = []
                        for x_ in range(each_):
                            api = eachMatch[x+1]
                            playerCount += 1
                            playerInfo = playerSearch(api,player_attributes)
                            temp = []
                            if playerInfo != []:
                                for x_1 in total[count]:
                                    temp.append(playerInfo[x_1])      
                                
                                positionStats.append([temp,role_]) 
                            
                                
                        if count != 3: 
                                count += 1     
                teamStats.append(positionStats)
            
                num = 0
                storage = []
                for crit in criteria: #0,1,2,3
                    attributeLen = len(crit[0][0][0][0])
                    positionAvg = []
                    for player in range(attributeLen): #11 players 
                        
                        numbering = 0
                        value = 0.0
                        length = 0.0
                        avgValue = 0.0
                        for player_ in positionStats:
                            if player_[1] == crit[1] and player_[0][numbering] != None:
                                
                                value += player_[0][numbering]
                                length += 1
                        if length == 0.0:
                            length =1 
                        avgValue = value/length
                        numbering += 1
                        

                        positionAvg.append(avgValue)
                    comparison = []
                    ClusterNum = 0
                    sortedPoint = crit[0][0][0]
                    sortedPoint.sort()
                    for critValue in range(len(crit)): 
                    
                        euc = distance.euclidean(sortedPoint[critValue],positionAvg)
                        comparison.append([euc,ClusterNum])
                        ClusterNum += 1
                    closest = min(comparison)
                    pr = []
                    for n in positionAvg: 
                        jj = n**2
                        pr.append(jj)
                    for c in sortedPoint[closest[1]]: 
                        cc = c**2
                        pr.append(cc)
                    prsum = sum(pr)
                    prsum_ = prsum**(1/2)
                    predictionPoints = prsum_
                    #predictionPoints += closest[1]/ len(crit)
                predict.append(predictionPoints)
            if predict[0] > predict[1]:
                result = 1
            elif predict[0] < predict[1]:
                result = 2
            elif predict[0] == predict[1]:
                result = 3

            output.append([eachMatch[0][1],result])
    print(output)
            
    return(output)










if __name__ == "__main__":
	compiler()


    
    