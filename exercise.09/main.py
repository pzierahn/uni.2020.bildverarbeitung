import numpy

arr = numpy.zeros((8, 8))
arr[2, 3:5] = numpy.ones(2)
arr[3, 2:6] = numpy.ones(4)
arr[4, 2:6] = numpy.ones(4)
arr[5, 3:5] = numpy.ones(2)

print(arr)
padding = numpy.zeros((8 + 2 * 2, 8 + 2 * 2))
padding[2:10, 2:10] = arr
print(padding)

laplace = numpy.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

value = numpy.zeros((8, 8))

for inx in range(8):
    for iny in range(8):
        x = inx + 2
        y = iny + 2
        slice = padding[x - 1:x + 2, y - 1:y + 2]
        value[inx, iny] = numpy.sum(slice * laplace)

print(value)
print(value / 4)