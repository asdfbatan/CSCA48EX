def radix_sort(numbers, degit=0):
    temp_list = numbers[:]
    bins = []
    cts = False
    for i in range(10):
        bins.append([])
    while temp_list != []:
        num = temp_list.pop(0)
        temp = int(num/10**degit)
        if temp >= 10:
            cts = True
        bins[(temp) % 10].append(num)
    for b in bins:
        temp_list += b
    if cts:
        return radix_sort(temp_list, degit + 1)
    else:
        return temp_list
