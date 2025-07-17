#  Rotate the matrix by 90 degrees
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n =len(matrix)
for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][i]
    
for i in range(0,n):
    matrix[i].reverse()

print(matrix)