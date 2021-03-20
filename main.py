rows = int(input("Enter size of rows\n"))
clmns = int(input("Enter number of columns\n"))
arr = []

#gets values from user
def get_2d_array():
    print("Enter numbers in rows and columns")
    for i in range(0, rows):
        a = []
        for j in range(0, clmns):
            element = int(input())
            a.append(element)
        arr.append(a)

c_arr=[]
get_2d_array()


def counts1s():
    for i in range(rows):
        count = 0
        for j in range(clmns):
            if arr[i][j] == 1:
                count += 1
            print(arr[i][j], end=" ")
        c_arr.append(count)
        #prints array
        print()
        print(count)


counts1s()
print(c_arr)

