from array import array

arr = array('i', [10, 20, 30])

print(arr)  # array('i', [10, 20, 30])

for i in range(len(arr)):
    print(arr[i], end=" ")  # 10 20 30

arr.append(40)

print(arr)  # array('i', [10, 20, 30, 40])

arr.insert(1, 30)

print(arr)  # array('i', [10, 30, 20, 30, 40])

arr.remove(10)

print(arr)  # array('i', [30, 20, 30, 40])

arr.pop()

print(arr)  # array('i', [30, 20, 30])

arr.reverse()

print(arr)

lst = list(arr)

print(lst)

lst.sort(reverse=True)

print(lst)

arr = array('i', lst)

print(arr)

# using array's package array method we can create only 1d array multi dimenstional is not posible
