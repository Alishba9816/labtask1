import random
rows = int(input("Enter size of rows\n"))
clmns = int(input("Enter number of columns\n"))
arr = []
toprows=5

# gets random number in array
def get2dArrayRand():
  for i in range (0,rows):
      a=[]
      for j in range(0,clmns):
        a.append(random.randint(0,clmns))
      arr.append(a)
  

#gets values from user
def get_2d_array():
    print("Enter numbers in rows and columns")
    for i in range(0, rows):
        a = []
        for j in range(0, clmns):
            element = int(input())
            a.append(element)
        arr.append(a)
        print('\n')
c_arr=[]


#counts and sort rows
def counts1s():
    for i in range(rows):
        count = 0
        for j in range(clmns):
            if arr[i][j] == 1:
                count += 1
            #print(arr[i][j], end=" ")
        c_arr.append(count)
        #prints array
        print()
        print(f'number of 1s in row {arr[i]} is "{count}" ')
        countSort(c_arr, rows, clmns)
c_arr.sort()
    

#sorts row and used in counts1s()
def countSort(c_arr, rows, clmns):
  #l=list(map(int,input("Enter Numbers:").split()))
  for i in range(0,len(c_arr)-1):
    for j in range(0,len(c_arr)-1):
        if(c_arr[j+1]>c_arr[j]):
            c_arr[j],c_arr[j+1]=c_arr[j+1],c_arr[j]
            arr[j],arr[j+1]=arr[j+1],arr[j]


def display_sorted_rows():
  c=0
  print('\n \n Sorted rows are:')
  for i in arr:
    c += 1
    print(f'\n Row {c} is {i} \n')


def display_top():
  c=0
  print(f'\n \n top {toprows} rows are:')
  for i in arr and range(0,toprows):
    c += 1
    print(f'\n Row {c} is {arr[i]} with number of ones {c_arr[i]} \n')
#def arrSort(c_arr, arr):
#get_2d_array()
#countSort(c_arr, rows, clmns)
#arrSort(c_arr, arr)
get2dArrayRand()
counts1s()
#display_sorted_rows()
display_top()

 