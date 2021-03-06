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

## rewrite this function os that it works with punctuation
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

def vectorizedMatrix (distinctWordList,textMsgDictionary):
    print(len(distinctWordList))
    vectorizedMatrix = []
    for user in  textMsgDictionary:
        for msg in textMsgDictionary[user]:
            vector = textVectorization(distinctWordList,msg)
            vectorizedMatrix.append(vector)
    return vectorizedMatrix
            
data= readData("topusers.txt")

textMsgDictionary = textParsing(data)

distinctWordList = getDistinctWords(textMsgDictionary)
print(distinctWordList)

matrix = vectorizedMatrix(distinctWordList,textMsgDictionary)
print(matrix)


fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')

# clustering data using Kmeans and PCA
X = np.array(matrix)
reduced_data = PCA(n_components=3).fit_transform(X)
kmeans = KMeans(n_clusters=7, random_state=0).fit_predict(reduced_data)
ax.scatter(reduced_data[:, 0], reduced_data[:, 1],reduced_data[:, 2], c=kmeans)

pyplot.show()

##what to do next: text the precision of the clustering in k-means algorithm 
##reduce dimension of data then test group them with the texters' identification 


