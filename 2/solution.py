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


def safe_check2(level, reversed = False):
    increasing = True if level[0] < level[1] else False
    
    if set_check(level):
        return True
    
    check = False
    for i in range(len(level)-1):
        if abs(level[i+1]-level[i]) > 3 or 1 > abs(level[i+1]-level[i]): #If any level has a difference greater than 3 or less than 1 then we recheck
            check = set_check(level[:i+1] + level[i+2:]) or set_check(level[:i] + level[i+1:]) 
        if increasing and level[i+1]-level[i] < 0: #If increasing and there is decreasing numbers, recheck
            check = set_check(level[:i+1] + level[i+2:])
        if (not increasing) and level[i+1]-level[i] > 0: #If decreasing and there is an increasing number, also recheck
            check = set_check(level[:i+1] + level[i+2:])

        if check:
            return True
    if reversed:
        return False
    else: #Final check: reverse the list since the first element might be increasing and others decreasing or vice versa
        return safe_check2(level[::-1], reversed=True)
        

def set_check(level):
    diff_set = set([level[i+1]-level[i] for i in range(len(level)-1)])
    if diff_set <= {1,2,3} or diff_set <= {-1,-2,-3}:
        return True
    return False

def brute(level, bad_count=0):
    def is_valid_sequence(level):
        # Check if the sequence is strictly increasing or strictly decreasing
        increasing = level[0] < level[1]
        for i in range(len(level) - 1):
            diff = abs(level[i+1] - level[i])
            if diff > 3 or diff < 1:  # Check difference constraint
                return False
            if (increasing and level[i] >= level[i+1]) or (not increasing and level[i] <= level[i+1]):
                return False
        return True

    # Base Case: If sequence is valid, return True
    if is_valid_sequence(level):
        return True

    # If more than one bad value is already found, return False
    if bad_count > 0:
        return False

    # Recursive Case: Try removing each element and see if it becomes valid
    for i in range(len(level)):
        if brute(level[:i] + level[i+1:], bad_count + 1):
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
        brute_check = brute(level)
        safety.append(safety_check)
        if safety_check != brute_check:
            print(f"For level: {level} the safety check is: {safety_check} and the brute check is {brute_check}")
    print(f"Sum of safety check is: {sum(safety)}")





