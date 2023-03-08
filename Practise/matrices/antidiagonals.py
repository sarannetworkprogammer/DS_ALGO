
mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]



def print_diagonals(mat):


    n = len(mat)
    m = len(mat[0])

    for c in range(0,m):
        print("printing diagonal")
        i = 0
        j = c
        while(i<n and j>=0):
            
            print(mat[i][j])
            i= i+1
            j = j-1

    for r in range(0,n):
        print("printing diagonal")


        i = r
        j = m-1

        while(i<n and j>=0):
            print(mat[i][j])

            i = i+1
            j=j-1



if __name__ == "__main__":
    print_diagonals(mat)


        






