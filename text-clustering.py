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


def getDistinctWords(textMsgDictionary):
    distinctWordList = []
    for user in  textMsgDictionary:
        for msg in textMsgDictionary[user]:
            wordList = textMsgConversion(msg)
            for word in wordList:
                if word not in distinctWordList:
                    distinctWordList.append(word)
    return distinctWordList

def textMsgConversion(msg):
    #remove unwanted characters
    for char in msg:
        if char in ".?!,":
            msg = msg.replace(char, " ")

    # stripped msg
    msg = msg.lower()
    wordList = msg.split(" ")
    return wordList
            
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
    vectorizedMatrix = []
    for user in  textMsgDictionary:
        for msg in textMsgDictionary[user]:
            vector = textVectorization(distinctWordList,msg)
            vectorizedMatrix.append(vector)
    return vectorizedMatrix
                     
            
        
#data= readData("test.txt")
data= readData("test1.txt")

textMsgDictionary = textParsing(data)
distinctWordList = getDistinctWords(textMsgDictionary)
print(vectorizedMatrix (distinctWordList,textMsgDictionary))

