rows = int(input("Enter size of rows:\n"))
clmns = int(input("Enter number of columns:\n"))
arr = []
c_arr=[]
max_5=[]

#gets values from user
def get_2d_array():
    print("Enter numbers:")
    for i in range(0, rows):
        a = []
        for j in range(0, clmns):
            element = int(input())
            a.append(element)
        print('\n')
        arr.append(a)

ma=0
def counts1s():
    for i in range(rows):
        count = 0
        for j in range(clmns):
            if arr[i][j] == 1:
                count += 1
            #print(arr[i][j], end=" ")
        c_arr.append(count)
        print()
        print(f'number of 1s in row {arr[i]} is "{count}" ')
        if(i>=0):
          bubbleSort(c_arr,arr)
        
def bubbleSort(c_arr,arr): 
    for j in range(len(c_arr)):
      swapped = False
      i = 0
      while i<len(c_arr)-1:
        #comparing the adjacent elements
        if c_arr[i]>c_arr[i+1]:
            #swapping
              c_arr[i],c_arr[i+1] = c_arr[i+1],c_arr[i]
              arr[i],arr[i+1] = arr[i+1],arr[i]
            #Changing the value of swapped
              swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
      if swapped == False:
        break
    print (c_arr)
    print (arr[i])

"""def decending_sort():
  if c_arr[1]<c_arr[0]:
    print(c_arr[0])
    print(arr[i])
"""

get_2d_array()
counts1s()
#decending_sort()