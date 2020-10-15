
# read the ciphertext.txt
# with open("ciphertext.txt", 'r') as f:
#     s = f.readline()
#     ascii_arr = s.split()
#     print(ascii_arr)
#     for i in range(0, len(ascii_arr)):
#         ascii_arr[i] = chr(int(ascii_arr[i]))
#
#     print(ascii_arr)

from collections import Counter
with open("ciphertext.txt","r") as f:
    s = f.readline()
    ascii_arr = s.split(" ")

    strs = []

    for i in range(0, len(ascii_arr)):
        list = [85,111,76]
        if i % 3 == 0:
            a = 85 ^ int(ascii_arr[i])
            strs.append(chr(a))
            #print(chr(a),85,int(ascii_arr[i]))
        if i % 3 == 1:
            a = 111 ^ int(ascii_arr[i])
            strs.append(chr(a))
        if i % 3 == 2:
            a = 76 ^ int(ascii_arr[i])
            strs.append(chr(a))

    print(strs)

    with open("first.txt","w") as f2:
        f2.writelines(strs)


    #print(ascii_arr)
    alph_arr =[]
    for i in range(0, len(ascii_arr)):
        alph_arr.append(chr(int(ascii_arr[i])))

    res = Counter(ascii_arr)
    #print(res)
    ## 108-l  79-O  117 -u
    #print(alph_arr)
    res1 = Counter(alph_arr)
    #print(res1)




## 130 l, 108 O, u 91
# print(32 ^ 130)

## U 85 o 111 L 76




