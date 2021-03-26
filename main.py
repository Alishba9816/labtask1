import random

rows = int(input("Enter size of rows\n"))
clmns = int(input("Enter number of columns\n"))
arr = []
toprows = 5
c = 0


# gets random number in array
def get2dArrayRand():
    for i in range(0, rows):
        a = []
        for j in range(0, clmns):
            a.append(random.randint(0, clmns))
        arr.append(a)


# gets values from user
def get_2d_array():
    print("Enter numbers in rows and columns")
    for i in range(0, rows):
        a = []
        for j in range(0, clmns):
            element = int(input())
            a.append(element)
        arr.append(a)
        print('\n')


c_arr = []


# counts and sort rows
def counts1s(c, arr, rows, clmns):
    for i in range(rows):
        count = 0
        c += 1
        for j in range(clmns):
            if arr[i][j] == 1:
                count += 1
            # print(arr[i][j], end=" ")
        c_arr.append(count)
        # prints array
        print()
        print(f'Row{c}) {arr[i]} --> ones "{count}" ')
        countSort(c_arr, rows, clmns, arr)


c_arr.sort()


# sorts row and used in counts1s()
def countSort(c_arr, rows, clmns, arr):
    # l=list(map(int,input("Enter Numbers:").split()))
    for i in range(0, len(c_arr) - 1):
        for j in range(0, len(c_arr) - 1):
            if (c_arr[j + 1] > c_arr[j]):
                c_arr[j], c_arr[j + 1] = c_arr[j + 1], c_arr[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def display_sorted_rows(arr):
    c = 0
    print('\n \n SORTED ROWS ARE:')
    for i in arr:
        c += 1
        print(f'\n Row {c} is {i} \n')


def display_top(c,arr):
    print(f'\n \n TOP {toprows} ROWS ARE:')
    for i in arr and range(0, toprows):
        c += 1
        print(f'\n Row{c}) {arr[i]} --> ones "{c_arr[i]}" \n')


mutationRow=[]
r = random.randint(0, clmns)
def mutation(clmn, arr, r):
    print("\n APPLYING MUTATION ON ROW 1 \n")
    print(f'Random number selected was "{arr[0][r]}" so Row1 is\n')
    if arr[0][r] <= 5:
        arr[0][r] = 1
    if arr[0][r] > 5:
        arr[0][r] = 9
    mutationRow.append(arr[0])
    print(f'{arr[0]}')


heads = []
tails = []
def spit_array():
    print('\n INHERITENCE OF LAST 4 ROWS:')
    for i in arr and range(0, toprows):
        heads.append(arr[i][0:5])
        tails.append(arr[i][5:10])
    print(f'Heads --> {heads}')
    print(f'Tails --> {tails}')


inhetnc=[]
print('HEAD TO TAIL COMBINATIONS ARE:')
def inheritence(heads, tails,c):
    for i in range (1,len(heads)):
        for j in range (0,len(tails)):
          if i!=j:
            temp= heads[i]+tails[j]
            inhetnc.append(temp)
            #else:
             # pass
    for i in inhetnc:
        c += 1
        print(f'New Row{c}) --> {i}')

arr2=[]
def scndArr(arr2,c):
    print('\n\n\n NEW ARRAYS ARE:')
    arr2=mutationRow+inhetnc
    for i in arr2:
      c +=1
      print(f'{c} --> {i}')
    #counts1s(c, arr2, rows, clmns)
    #display_top(c, arr2)
   # mutation(clmns, arr2)

# def arrSort(c_arr, arr):
# get_2d_array()
# countSort(c_arr, rows, clmns)
# arrSort(c_arr, arr)
get2dArrayRand()
counts1s(c, arr, rows, clmns)
# display_sorted_rows()
display_top(c, arr)
mutation(clmns, arr, r)
spit_array()
inheritence(heads, tails, c)
scndArr(arr2,c)


