import numpy as np
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def readData(textFile):
    file = open(textFile)
    data = []
    for line in file:
        data.append(line)
    return data


def textParsing (data):
    textMsgDictionary= {}
    for i in range(len(data)):
        subdata = data[i].split(":~:")
        textMsgDictionary[subdata[0]]= subdata[1:]
    return textMsgDictionary


def textMsgConversion(msg):
       #remove unwanted characters
    i = 0
    msg_length = len(msg)
    msg = msg.lower()
    while i< msg_length:
        if msg[i] not in "qwertyuiopasdfghjklzxcvbnm.,#~?!/><+$%_)(][+-=\@^*':":
            msg = msg.replace(msg[i], " ")
            i+=1
        elif msg[i] in ".,#~?!/><+$%_)(][+-=\@^*':":
            msg = msg[:i]+" "+msg[i]+" "+msg[(i+1):]
            msg_length+=2        
            i+=3
        else:
            i+=1
            
##    for char in msg: 
##        if char not in "qwertyuiopasdfghjklzxcvbnm":
##            msg = msg.replace(char," ")
            
   #split msg into word list 
    wordList = msg.split(" ")
    return wordList

def getDistinctWords(textMsgDictionary):
    #print(textMsgDictionary.keys())
    distinctWordList = []
    for user in  textMsgDictionary:
        for msg in textMsgDictionary[user]:
            wordList = textMsgConversion(msg)
            for word in wordList:
                if word not in distinctWordList:
                    distinctWordList.append(word)
    return distinctWordList

            
def textVectorization (distinctWordList,msg):
    vector = []
    wordList = textMsgConversion(msg)
    for i in range(len(distinctWordList)):
        if distinctWordList[i] in wordList:
            vector.append(1)
        else:
            vector.append(0)
    return vector

def vectorizedDictionary (distinctWordList,textMsgDictionary):
    print(len(distinctWordList))
    vectorizedDictionary= {}
    for user in  textMsgDictionary:
        vectorizedMatrix = []
        for msg in textMsgDictionary[user]:
            vector = textVectorization(distinctWordList,msg)
            vectorizedMatrix.append(vector)
        vectorizedDictionary[user] = vectorizedMatrix
    return vectorizedDictionary

def getMaxLength(vectorDict):
    lenList = []
    for user in vectorDict:
        length = len(vectorDict[user])
        lenList.append(length)
    return max(lenList)


def transformData(vectorDict):
    transformedVectorDict= {}
    for key in vectorDict:
        X = np.array(vectorDict[key])
        print("numpy array: ", X)
        reduced_data = PCA(n_components=3).fit_transform(X) #data scatter differently on different runs
        print("reduced data: ", reduced_data)
        transformedVectorDict[key] = reduced_data
    return transformedVectorDict

           
data= readData("topusers.txt")
textMsgDictionary = textParsing(data)
distinctWordList = getDistinctWords(textMsgDictionary)
print(distinctWordList)
vectorDict = vectorizedDictionary(distinctWordList,textMsgDictionary)
print(vectorDict)
transformedVectorDict = transformData(vectorDict)

maxLength = getMaxLength(transformedVectorDict)
print(maxLength)


##for key in vectorDict:
##    print(key)
##    X = np.array(vectorDict[key])
##    print("numpy array: ", X)
##    reduced_data = PCA(n_components=2).fit_transform(X) #data scatter differently on different runs
##    print("reduced data: ", reduced_data)
##    pyplot.scatter(reduced_data[:, 0], reduced_data[:, 1],label=key ) #why cannot display label?
##pyplot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
##pyplot.show()

fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')


key_list= []
for key in transformedVectorDict:
    key_list.append(key)

print(key_list)

color_list= ["blue","pink","green","orange","red","yellow","purple"]


reduced_data = transformedVectorDict[key_list[6]]
ax.scatter(reduced_data[:, 0], reduced_data[:, 1], reduced_data[:, 1], color=color_list[6] ) 


# for i in range(maxLength):
#     for j in range(len(key_list)):
#             if i < len(transformedVectorDict[key_list[j]]):
#                 ax.scatter(transformedVectorDict[key_list[j]][i][0], transformedVectorDict[key_list[j]][i][1], transformedVectorDict[key_list[j]][i][2], color=color_list[j]) 
pyplot.show()

    




