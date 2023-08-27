def quick_sort(a,left_range,right_range):
    if left_range>=right_range:
        return
    mid = a[right_range]
    r , l = right_range-1,left_range
    while l<r:
        while l<r and a[l]<mid:
            l+=1
        while l<r and a[r]>mid:  # 注意，这个结构用来保持循环不变量非常合适  
            r+=1
        a[l],a[r] = a[r],a[l]
    if a[l]<mid:
        l+=1
    a[l],a[right_range] = a[right_range],a[l] 
    quick_sort(a,left_range,l-1) 
    quick_sort(a,l+1,right_range) 

l = [5,2,9,3,8]
quick_sort(l,0,4)    
print(l)
