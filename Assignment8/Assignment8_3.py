import threading
def evenlist(list1):
    list=[]
    for num in list1:
        if num%2==0:
            list.append(num)
    print("The even number from list is:", list)
    sum = 0
    for element in range(0, len(list)):
        sum = sum + list[element]
    print("The sum of even list is:", sum)

def oddlist(list1):
    list=[]
    for num in list1:
        if num%2!=0:
            list.append(num)
    print("The odd number from list is:",list)
    sum = 0
    for element in range(0, len(list)):
        sum = sum + list[element]
    print("The sum of odd list is:", sum)
def main():
    n=int(input("length of list:"))
    list1=[]
    for i in range(n):
        element= int(input("Enter the Number:"))
        list1.append(element)
    print("list of Number:",list1)


    thread1=threading.Thread(target=evenlist,args=(list1,))
    thread2=threading.Thread(target=oddlist,args=(list1,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__=="__main__":
    main()