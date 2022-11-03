import sys
list1 = [5, 2, 3, 1, 4]

list1.sort(reverse=True)
list1.sort(key= lambda a : a % 4)
print(list1)

list2 = [
    (0,0),
    (1,7),
    (5, 19),
    (12, 9),
    (18, 0),
    (2, 6)
]
print(sys.getsizeof(list1))
print(sys.getsizeof(list2))
print(list2)
list2.sort(key= lambda a : a[0]**2 + a[1]**2)
print(list2)

# enumerate()

dict1 = {
    "john": 10,
    "jill": 20,
    "sam": 500
}

for val in enumerate(dict1):
    print(val)

list1.reverse()

print(list1)



class exampleObject:
    def __init__(self):
        self.variable = 0

object1 = exampleObject()

# id function used for viewing unique IDs for python class objects
print(id(object1))

print(object1.__dict__)
print(vars(object1))
print(object1.__module__)
print(object1.__doc__)
print(object1.__class__)
print(object1.__weakref__)
print(object1.__str__)
print(object1.__hash__)


# thinking about lambdas
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

matrix = [ [0] * (3) for _ in range(6)]
# matrix = [[0] * 3] * 6
print(matrix)
matrix[0][1] = 1
print(matrix)
