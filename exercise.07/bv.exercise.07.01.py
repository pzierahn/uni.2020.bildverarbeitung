import numpy

g = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 0, 0, 0, 0],
                [0, 1, 3, 5, 0, 0, 0, 0],
                [0, 1, 2, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])

f = numpy.array([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])

k1 = numpy.array([[0,   0.2, 0],
                 [0.2, 0.2, 0.2],
                 [0,   0.2, 0]])

k2 = numpy.array([[0, 0, 0],
                  [0, 2/3, 1/3],
                  [0, 0, 0]])

k3 = numpy.array([[0, 0, 0],
                  [0, 0, 1],
                  [0, 0, 0]])

def main(f: numpy.array, k1: numpy.array):
    result = numpy.zeros((f.shape[0] - 2, f.shape[1] - 2))

    for inx in range(1, f.shape[0] - 1):
        for iny in range(1, f.shape[1] - 1):

            print(f[inx - 1 : inx + 2, iny - 1 : iny + 2])
            print((f[inx - 1 : inx + 2, iny - 1 : iny + 2] * k1))
            print("sum", numpy.sum(f[inx - 1 : inx + 2, iny - 1 : iny + 2] * k1))
            result[ inx - 1 ][ iny - 1 ] = numpy.sum(f[inx - 1 : inx + 2, iny - 1 : iny + 2] * k1)

    print("result")
    print(result)

# print("flip", numpy.flip(k2))
main(g, numpy.flip(k3))
# main(g, k3)