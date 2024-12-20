
def readFile(file):
    firstList = []
    secondList = []

    with open(file) as f:
        lines = f.readlines() 

        for line in lines:
            line = line.strip() # remove leading/trailing white spaces
            if line:
                data = line.split(' ')
                data = list(filter(None,data)) #Remove empty strings from the list

                firstList.append(int(data[0])) # append first part to list
                secondList.append(int(data[1])) #append second part to list
    return firstList,secondList

def calc_distances(list1, list2):
    list1.sort()
    list2.sort()
    distances = [abs(b - a) for a,b in zip(list1,list2)]
    return distances

def similarity_score(list1,list2):
    return [x * list2.count(x) for x in list1]

if __name__=="__main__":

    firstList,secondList = readFile("input.txt")
    distances = calc_distances(firstList,secondList)
    for i in range(5):
        print(f"{firstList[i]} {secondList[i]} with distance: {distances[i]}") #Debug: check that it works fine
    print(f"sum of all distance = {sum(distances)}") #End of first task

    similarity = similarity_score(firstList, secondList)
    print(f"The similarity score is: {sum(similarity)}") #End of second task


    
    
    
