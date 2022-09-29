# -*- coding: utf-8 -*-

x= [[3,4,7],[1,2,8]]
y= [[1,2,3],[1,3,0]]

result= [[0,0,0],[0,0,0]]


for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]= x[i][j]+y[i][j]

print(result)