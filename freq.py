arr=[1,2,3,4,2,2,10000]
freq={}
for n in arr:
        freq[n]=freq.get(n,0)+1
'''    return freq
arr=[1,2,3,4,4,3,2,1,1,1,2,2,3,3,4,4]
frequencies=countf(arr)
for i, count in frequencies.items():
    print(i,count)

'''
print(freq)
maxx=max(freq,key=freq.get)
minn=min(freq,key=freq.get)
print(maxx)#max freq num
print(minn)#min freq num
