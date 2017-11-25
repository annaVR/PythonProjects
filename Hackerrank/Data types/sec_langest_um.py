__author__ = 'anna'
n = int(input())
inp = input()
lst = list(map(int, inp.split()))
ln = None
for i in lst:
    if ln is None:
        ln = i
    elif i > ln:
        ln = i
cts = lst.count(ln)
for ct in range(cts):
    lst.remove(ln)
min_diff = None
ind = None
min_ind = None
for j in lst:
    diff = ln - j
    if ind is None and min_diff is None:
        ind = 0
        min_diff = diff
        min_ind = ind
    elif diff < min_diff:
        min_diff = diff
        ind+= 1
        min_ind = ind
    else:
        ind+= 1
print(lst[min_ind])

#second solution (latest)
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] and arr[i] > arr[i + 1]:
        print(arr[i + 1])
        break
    elif arr[i] == arr[i - 1] and arr[i] == arr[i + 1]:
        continue
    else:
        print(arr[i])
        break







