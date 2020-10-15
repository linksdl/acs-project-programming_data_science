"""


"""
import itertools


def loop(key_logs):
    #for len_code in range(4, 100):
        # for code in itertools.permutations(list(range(10)), len_code):
    for i in range(300000, 999999999999):
        str_i  = str(i)
        code = tuple(str_i)
        login_counter = 0

        for key in key_logs:
            digits = (str(key // 100), str((key % 100) // 10), str(key % 10))
            if digits[0] in code:
                pos_0 = code.index(digits[0])
                curr_code = code[pos_0 + 1:]
                if digits[1] in curr_code:
                    pos_1 = curr_code.index(digits[1])
                    curr_code = curr_code[pos_1 + 1:]
                    if digits[2] in curr_code:
                        login_counter += 1
                    else:
                        break
                else:
                    break
            else:
                break

        # if all logins fit the code, it is a solution
        print(code, "===========", login_counter)
        if login_counter == len(key_logs):
            print(code)
            return code


def solution(n):
    key_logs = []
    with open("keylogs.txt", "r") as f:
        for i in range(0, n):
            line = f.readline().strip()
            line_key = line.replace(' ', '')
            key_logs.append(int(line_key))
    print(key_logs)
    pass
    return loop(key_logs)


num_tuples = 50
print("the string is ", solution(num_tuples))
