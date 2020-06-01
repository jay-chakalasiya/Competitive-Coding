# given an matrix MxN, if an element in matrix is 0 then make the row and column of the same cell 0

import numpy as np
def make_row_zero(matrix, row_index):
    for i in range(len(matrix[0])):
        matrix[row_index][i]=0
def make_colun_zero(matrix, column_index):
    for i in range(len(matrix)):
        matrix[i][column_index]=0
def zero_matrix(matrix):
    print(np.array(matrix))
    rows=[]
    columns=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                if i not in rows:
                    rows.append(i)
                if j not in columns:
                    columns.append(j)
    for r in rows:
        make_row_zero(matrix, r)
    for c in columns:
        make_colun_zero(matrix, c)
    #print(rows, columns)
    print(np.array(matrix))
    return matrix
def main():
    print(zero_matrix([[0,2,3], [4,5,6], [7,8,0]]))
    print(zero_matrix([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]))
if __name__ == "__main__":
    main()