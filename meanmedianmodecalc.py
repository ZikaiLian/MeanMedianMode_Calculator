def average(arr):
    a = 0
    for i in range(0, len(arr)):
        a += arr[i]
    print(a/len(arr))

from collections import defaultdict
def mode(arr):
    arr.sort()
    diction = defaultdict(int)
    for i in range(0, len(arr)):
        diction[arr[i]] += 1
    max_key = max(diction, key=diction.get)
    print(max_key)
    #in case there are multiple modes
    print(diction)

def median(arr):
    med = 0
    arr.sort()
    if len(arr) % 2 == 1:
        med = (arr[int((len(arr)+1)/2)-1])
    else:
        med = (arr[int(len(arr)/2-1)] + arr[int(len(arr)/2)])/2
    print(med)