def readFile(file):
    levels = []
    with open(file) as f:
        lines = f.readlines()
        levels = [[int(val) for val in line.split()] for line in lines]
    return levels

def safe_check1(level):
    increasing = True if level[0] < level[1] else False

    if increasing:
        sorted_level = sorted(level)
    else:
        sorted_level = sorted(level,reverse=True)

    i = 0
    for x,y in zip(level, sorted_level):
        if x != y: #Compared the sorted one with this list, if they are not the same then there is a wrong value
            return False #If we already found a bad value and this is the second, return false
        if i < (len(level) - 1):
            if abs(level[i+1]-level[i]) > 3 or 1 > abs(level[i+1]-level[i]):
                return False
        i += 1
    return True


def safe_check2(level):
    for i in range(len(level)):
        if set_check(level[:i] + level[i+1:]):
            return True
    return False

def set_check(level):
    diff_set = set([level[i+1]-level[i] for i in range(len(level)-1)])
    if diff_set <= {1,2,3} or diff_set <= {-1,-2,-3}:
        return True
    return False

if __name__ == "__main__":
    levels = readFile("input.txt")
    safety = []
    for level in levels:
        safety.append(safe_check1(level))
    print(f"The sum of safe levels for task 1 is: {sum(safety)}")
    #End of task 1 ^

    safety = []
    for level in levels: 
        safety_check = safe_check2(level)
        safety.append(safety_check)
    print(f"Sum of safety check is: {sum(safety)}")





