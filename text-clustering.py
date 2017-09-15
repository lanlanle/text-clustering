def readData(textFile):
    file = open(textFile,"r")
    data = file.read().splitlines() 
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

            #remove unwanted characters

            for char in msg:
                if char in ".?!":
                    msg = msg.replace(char, " ")

            # stripped msg 
            wordList = msg.split(" ")
            for word in wordList:
                if word not in distinctWordList:
                    distinctWordList.append(word)
    return distinctWordList
            
        

#def textParsing(textfile):
#print(readData("parsedxmlnew.txt"))
data= readData("test.txt")
textMsgDictionary = textParsing(data)
print(getDistinctWords(textMsgDictionary))
