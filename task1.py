from random import randint
n = int(input("Введите количество элементов: "))
arr = []
pref_arr = []

amount_0 = 0
amount_1 = 0
for i in range(n):
    arr.append(randint(0, 1))
    if arr[-1] == 0:
        amount_0 += 1
    else:
        amount_1 += 1
    pref_arr.append([amount_0, amount_1])
    
#print(arr)
if arr[n - 1] == 0:
    print("0 - ", (pref_arr[n - 1][0] - pref_arr[0][0] + 1) / n)
else:
    print("0 - ", (pref_arr[n - 1][0] - pref_arr[0][0]) / n)
    
if arr[n - 1] == 1:
    print("1 - ", (pref_arr[n - 1][1] - pref_arr[0][1] + 1) / n)
else:
    print("1 - ", (pref_arr[n - 1][1] - pref_arr[0][1]) / n)
    
w = 1
while True:
    l = 0
    r = l + w
    para_0 = 0
    para_1 = 0
    while r != n:
        count_0 = 0
        if (arr[r] == 0 and arr[l] == 1) or (arr[l] == 1 and arr[r] == 1):
            count_0 = pref_arr[r][0] - pref_arr[l][0]
        else:
            count_0 = pref_arr[r][0] - pref_arr[l][0] + 1
        
        count_1 = 0
        if (arr[r] == 1 and arr[l] == 0) or (arr[l] == 0 and arr[r] == 0):
            count_1 = pref_arr[r][1] - pref_arr[l][1]
        else:
            count_1 = pref_arr[r][1] - pref_arr[l][1] + 1
        
        if count_0 == w + 1:
            para_0 += 1
        if count_1 == w + 1:
            para_1 += 1
        
        l, r = l + 1, r + 1
    #print(para_0, para_1)
    if para_0 != 0 and para_1 != 0:
        print("[" + "0" * (w + 1) + "] - ", para_0 / (n - 1))
        print("[" + "1" * (w + 1) + "] - ", para_1 / (n - 1))
        w += 1
    else:
        break
            