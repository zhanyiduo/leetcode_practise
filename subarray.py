def find_sub_array(a,num):
    count = 0
    for i in range(0,len(a)):
        if a[i]>num:
            continue
        else:
            sum = a[i]
            for j in range(i+1, len(a)):
                if sum == num:
                    count +=1
                    break
                elif sum>num:
                    break
                else:
                    sum += a[j]
    return count

count = find_sub_array([1,1,1,2,3,0,0,0,4,5,5],4)

print(count)