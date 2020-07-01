import numpy

a213 = numpy.array([[210, 212, 10],
                    [211, 213, 12],
                    [213, 214, 11]])

a12 = numpy.array([[212, 10, 12],
                   [213, 12, 216],
                   [214, 11, 14]])

a214 = numpy.array([[211, 213, 12],
                    [213, 214, 11],
                    [214, 210, 15]])

a11_g = numpy.array([[213, 12, 216],
                     [214, 11, 14],
                     [210, 15, 13]])

a11_b = numpy.array([[15, 13, 13],
                     [213, 11, 12],
                     [210, 212, 14]])

a210 = numpy.array([[212, 213, 11],
                    [214, 210, 212],
                    [212, 211, 142]])

a62 = numpy.array([[211, 142, 64],
                   [146, 62, 13],
                   [61, 14, 12]])

labels = ["a213", "a12", "a214", "a11_g", "a11_b", "a210", "a62"]
matrixs = [a213, a12, a214, a11_g, a11_b, a210, a62]

prewitt_right = numpy.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

prewitt_bottom = numpy.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])

sobel_right = numpy.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

sobel_bottom = numpy.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]])

for xx in range(len(matrixs)):

    matrix = matrixs[xx]
    parts = []
    sum = 0

    for inx in range(3):
        for iny in range(3):
            # w = prewitt_right[inx, iny]
            # w = prewitt_bottom[inx, iny]
            # w = sobel_right[inx, iny]
            w = sobel_bottom[inx, iny]
            pixel = w * matrix[inx, iny]

            sum += pixel
            parts += [str(pixel)]

    # print(labels[xx])
    print(labels[xx], "::", " + ".join(parts), "=", sum)
