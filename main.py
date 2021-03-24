import random
rows = int(input("Enter size of rows\n"))
clmns = int(input("Enter number of columns\n"))
arr = []

#gets values from user
def get2dArrayRand():
  for i in range (0,rows):
      a=[]
      for j in range(0,clmns):
        a.append(random.randint(0,clmns))
      arr.append(a)
  


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


def swap(arr1,arr2):
  temp=arr1
  arr1=arr2
  arr2=temp
  print(arr1, arr2) 


def countSort(c_arr, rows, clmns):
  #l=list(map(int,input("Enter Numbers:").split()))
  for i in range(0,len(c_arr)-1):
    for j in range(0,len(c_arr)-1):
        if(c_arr[j+1]>c_arr[j]):
            c_arr[j],c_arr[j+1]=c_arr[j+1],c_arr[j]
  print(c_arr)


def arrSort(c_arr, arr):
  for i in range(0,len(c_arr)-1):
    for j in range(0,len(c_arr)-1):
      if(c_arr[j+1]>c_arr[j]):
        arr[i],arr[i+1]=arr[i+1],arr[i]
        print(f'arrays are{arr[i]}')
get2dArrayRand()
#get_2d_array()
counts1s()
#countSort(c_arr, rows, clmns)
arrSort(c_arr, arr)


