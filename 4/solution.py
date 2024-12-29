
if __name__ == "__main__":
    s = []
    with open('input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            s.append(line.strip())
    
    number_lines = len(s)
    line_length = len(s[0])
    horizontal = [s[i][j:j+4] for i in range(len(s)) for j in range(line_length) if len(s[i][j:j+4]) == 4]

    big_s = ''.join(s)
    vertical = [big_s[i:i+(3*line_length+1):line_length] for i in range(number_lines*line_length) if len(big_s[i:i+(3*line_length+1):line_length]) == 4]
    diagonal_right = [big_s[i:i+(3*line_length+4):line_length+1] for i in range(number_lines*line_length) if len(big_s[i:i+(3*line_length+4):line_length+1]) == 4 and (i % line_length) < (line_length - 3)]
    diagonal_left = [big_s[i:i+(3*line_length+1):line_length-1] for i in range(number_lines*line_length) if len(big_s[i:i+(3*line_length+1):line_length-1]) == 4 and (i % line_length) > 2]

    print(sum([x == "XMAS" or x == "SAMX" for x in horizontal + vertical + diagonal_right+ diagonal_left]))
    # End of task 1

    #Task 2
    diagonals = [big_s[i-line_length-1] + big_s[i-line_length+1] + big_s[i+line_length-1] + big_s[i+line_length+1] for i in range(line_length,(number_lines-1)*line_length) if (i % line_length) != 0 and (i % line_length) != (line_length - 1) and big_s[i] == 'A']
    sum_x = sum([x == "MMSS" or x == "SMSM" or x == "SSMM" or x == "MSMS" for x in diagonals])
    print(sum_x)

    
