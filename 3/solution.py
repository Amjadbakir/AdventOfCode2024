
#I know I can use regex but I wanted to make it in a more manual state-transition way
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