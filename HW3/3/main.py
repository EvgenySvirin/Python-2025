import numpy as np
from hashmatrix import Matrix

if __name__ == '__main__':
    np.random.seed(0)
    A = Matrix([[1, 0], [0, 1]])
    B = Matrix([[1, 0], [0, 1]])
    C = Matrix([[3, 0], [0, 1]])
    D = Matrix([[1, 0], [0, 1]])


    AB = A@B
    CD = C@D


    A.save("../artifacts/3/A.txt")
    B.save("../artifacts/3/B.txt")
    C.save("../artifacts/3/C.txt")
    D.save("../artifacts/3/D.txt")
    AB.save("../artifacts/3/AB.txt")
    CD.save("../artifacts/3/CD.txt")

    assert A.__hash__() == C.__hash__() and A.arr != C.arr and B.arr == D.arr and AB.arr != CD.arr
    with open("../artifacts/3/hash.txt", 'w') as f:
        f.write(f"AB hash: {str(AB.__hash__())} \n")
        f.write(f"CD hash: {str(CD.__hash__())} \n")
