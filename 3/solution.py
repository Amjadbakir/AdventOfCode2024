


#def solution(s):
    #state = 0
    #number1 = ""
    #number2 = ""
    #for c in s:
    #    number1,number2,state = state_transition(number1,number2,state, c)
    #print(number2)
    

    #list = [c for c in s if c in "mul(,)"]
    #format = ''.join(str(x) for x in list)
    #print(format)


'''string = ""
    number1 = ""
    number2 = ""
    sum = 0
    i = 0
    while i < len(s):
        
        if s[i] == 'm':
            while(s[i] != '('):
                string += s[i]
                i += 1
            i += 1
            if string == "mul":
                while(s[i] != ','):
                    number1 += s[i]
                    i += 1
                i+=1
                if number1.isdigit():
                    while(s[i] != ')'):
                        number2 += s[i]
                        i += 1
                    #i += 1
                    if number2.isdigit():
                        lhs = int(number1)
                        rhs = int(number2)
                        sum = sum + rhs * lhs
                        number1 = ""
                        number2 = ""
                        string = ""
        i += 1
    return sum'''

'''def mul(s,i,j,n1,n2):
    if i==len(s):
        return n1, n2
    
    k = "mul(,)"
    if j >= len(k):
        return mul(s,i,0,n1,n2)
    elif s[i] == k[j]:
        j+=1
        i+=1
        return mul(s,i,j,n1,n2)
    elif s[i].isdigit() and j==4:
        n1 += s[i]
        i+=1
        return mul(s,i,j,n1,n2)
    elif s[i].isdigit() and j==5:
        n2 += s[i]
        i+=1
        return mul(s,i,j,n1,n2)
    else:
        return mul(s,i+1,j,n1,n2)'''
                        


            
            
    


def state_transition(number1,number2,state, s):
    
    sum = 0
    for input in s:
        if state == 0:
            number1 = ""
            number2 = ""
        if input == 'm':
            state = 1
        elif input == 'u' and state == 1:
            state = 2
        elif input == 'l' and state == 2:
            state = 3
        elif input == '(' and state == 3:
            state = 4
        elif input.isdigit() and state == 4:
            number1 = number1 + input
            state = 5
        elif input.isdigit() and state == 5:
            number1 = number1 + input
        elif input == ',' and state == 5:
            state = 6
        elif input.isdigit() and state == 6:
            number2 = number2 + input
            state = 7
        elif input.isdigit() and state == 7:
            number2 = number2 + input
        elif input == ')' and state == 7:
            state = 0
            sum = sum + int(number1) * int(number2)
            

        else:
            state = 0
            number1 = ""
            number2 = ""

    return sum


if __name__ == "__main__":
    #s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(4,)mul(4,5)"
    #s = "mul(1,2)mmmul(1,2)"
    s = open("input.txt").read()
    print(state_transition(number1="",number2="",state=0,s=s))