def move_zeros(array):
    k=0
    array1=[]
    for i in array:
        if i=='0':
            continue
        if str(i)=='0' or str(i)=="0.0":
            k+=1
    for j in array:
        if j=='0':
            array1.append(j)
            continue
        if str(j)!='0'and str(j)!="0.0":
            array1.append(j)
    for z in range(k):
        array1.append(0)
    return array1

print(move_zeros([0,0,0,1,1,11,1]))