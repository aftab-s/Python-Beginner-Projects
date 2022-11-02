def binary_search(a,target):

    middle = 0
    #middle = int(middle)
    start = 0
    #start = int(start)
    end = len(a)
    #end = int(end)

    
    while start <= end:
        middle = (start + end) // 2

        if target == a[middle]:
            print(f"Target Found at Position : {middle+1}")
            break

        elif target > a[middle]:
            start = middle + 1
        elif target < a[middle]:
            end = middle - 1
        else:
            print("Target Not Found.")

def a_sort(a):

    end = len(a)

    for i in range(end-1):
        for j in range(end - i - 1):
            if a[j] > a[j + 1]:

                #Swapping
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    print("Sorted Array : ")
    
    for i in range(end -1):
        print(a[i])


#a = list(int(input("Enter The List : ")))
#a = list(a)
a = [10, 21, 5, 1, 2, 7, 20]

# lst = []
# a = int(input("Enter The Array : "))

# for i in range(0,a):
#     element = int(input())

#     lst.append(element)

# print("Unsorted Array : ", lst)

print("Given Array :",a)

target = input("Enter The Target To Be Searched : ")
target = int(target)
a_sort(a)
binary_search(a,target)

