# given an image matrix of size NxN, where each pixel in image is 4 bytes 
# make a function which rotate image by 90 degrees
# Try to do it in place
import numpy as np
def rotate_matrix(matrix):
    print(np.array(matrix))
    N = len(matrix)
    for i in range(N//2):
        for j in range(i, N-i-1, 1):
            matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i], matrix[i][j]
    print(np.array(matrix))
    return matrix
def main():
    print(rotate_matrix([[1,2,3], [4,5,6], [7,8,9]]))
if __name__ == "__main__":
    main()