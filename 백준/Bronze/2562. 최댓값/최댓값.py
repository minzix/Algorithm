arr = []
for i in range(9): 
    try: 
        arr.append(int(input()))
    except:
        break
max_num = 0
max_index = 0
for i in range(len(arr)): 
    if arr[i] > max_num: 
        max_num = arr[i]
        max_index = i
print(max_num)
print(max_index+1)