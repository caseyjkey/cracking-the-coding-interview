# Given two straight line segments as start and end points, compute the intersection, if any

def intersect(a, b):
    xdif = (a[0][0] - a[1][0], b[0][0] - b[1][0])
    ydif = (a[0][1] - a[1][1], b[0][1] - b[1][1])

    def det(A, B):
        return A[0] * B[1] - A[1] * B[0]

    div = det(xdif, ydif)
    if div == 0:
        raise Exception('no intersection')

    d = (det(*a), det(*b))
    x = det(d, xdif) / div
    y = det(d, ydif) / div

    return x, y

print(intersect(((0, 0), (0, 2)), ((-1, 1), (1, 1))))
