import numpy as np

class LinearCode:
    def __init__(self):
        pass

    def ref(self, mat):
        row = 0
        n = mat.shape[0]
        m = mat.shape[1]
        lead = []
        for j in range(m):
            isSwap = False
            for i in range(row, n):
                if isSwap != True:
                    if mat[i][j] == 1:
                        mat[[row, i]] = mat[[i, row]]
                        isSwap = True
                        lead.append(j)
                        for k in range(row + 1, n):
                            if mat[k][j] == 1:
                                mat[k] = (mat[k] + mat[row]) % 2
                        row += 1
        return mat, lead

    def rref(self, mat):
        print(mat)
        print( )
        row = 0

        n = mat.shape[0]
        m = mat.shape[1]
        for i in range(row, n):
            find = False
            for j in range(m):
                if find != True:
                    if mat[i][j] == 1:
                        find = True
                        for k in range(0, row):
                            if mat[k][j] == 1:
                                mat[k] = (mat[k] + mat[row]) % 2
                        row += 1
        mat = self.delete_zero_row(mat)
        return mat

    @staticmethod
    def delete_zero_row(mat):
        n = mat.shape[0]
        for i in range(n):
            if not np.any(mat[i]):
                matn = np.delete(mat, i, 0)
        return matn

    @staticmethod
    def delete_column(mat, list):
        matt = mat
        m = matt.shape[0]
        for i in range(len(list)):
            matt = np.delete(matt, i, 1)
        return matt

    @staticmethod
    def count_rows_an_columns(mat):
        print("Result:")
        print("n = ", mat.shape[0])
        print("k = ", mat.shape[1])

x = 3
y = 4
#a = np.array([[0, 0, 1, 0],
# [1, 1, 0, 1],
# [1, 0, 0, 1]], dtype=int)

a = np.array([[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]], dtype=int)

# a = np.array([[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
# [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
# [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]], dtype = int)


Lc = LinearCode()
refa, lead = Lc.ref(a)
rrefa = Lc.rref(refa)
print(rrefa)
Lc.count_rows_an_columns(a)
print( )
print("Lead = ", lead)
print( )
newMat = Lc.delete_column(rrefa, lead)
print(newMat)