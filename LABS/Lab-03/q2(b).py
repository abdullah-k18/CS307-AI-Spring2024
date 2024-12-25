X = [[1, 2, 3],
    [4 , 5, 6],
    [7 , 8, 9]]
result = [[0, 0, 0],
         [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
print("Transpose of X = ")
for r in result:
   print(r)