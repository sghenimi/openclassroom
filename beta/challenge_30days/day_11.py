# for _ in range(5):
#     print("e : ", _)

matrix = [
    [1, 1, 9, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 9, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 2, 0]]

martrix = [
    [-1 ,-1,  0 ,-9 ,-2 ,-2],
    [-2 ,-1 ,-6 ,-8 ,-2 ,-5],
    [-1 ,-1 ,-1 ,-2 ,-3 ,-4],
    [-1 ,-9 ,-2 ,-4 ,-4 ,-5],
    [-7 ,-3 ,-3 ,-2 ,-9 ,-9],
    [-1 ,-3 ,-1 ,-2 ,-4 ,-5]
]

def get_max_hourglass(list_matrix):
    sum = -100
    for i in range(4):
        for j in range(4):
            temp_hg = 0
            # top row
            temp_hg += list_matrix[i][j]
            temp_hg += list_matrix[i][j+1]
            temp_hg += list_matrix[i][j+2]
            # middle row
            temp_hg += list_matrix[i+1][j+1]
            # bottom row
            temp_hg += list_matrix[i+2][j]
            temp_hg += list_matrix[i+2][j+1]
            temp_hg += list_matrix[i+2][j+2]

            if(temp_hg > sum):
                sum = temp_hg
    
    print(sum)
    
get_max_hourglass(matrix)