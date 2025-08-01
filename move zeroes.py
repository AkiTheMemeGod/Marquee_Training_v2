x = [1,0,2,23,0,12,0,3,4,0,5]
l,r = 0,len(x)-1
while l<=r:
    if x[l]==0:
        x[l],x[r]=x[r],x[l]
        r-=1
    else:
        l+=1
print(x)
