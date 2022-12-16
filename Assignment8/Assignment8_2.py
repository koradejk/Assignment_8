import threading
def evenfactor(mylist1):
    sum=0
    for element in range(0,len(mylist1)):
        sum=sum+mylist1[element]
    print("The sum of even number is:",sum)
def oddfactor(mylist2):
    sum = 0
    for element in range(0,len(mylist2)):
        sum = sum + mylist2[element]
    print("The sum of odd number is:", sum)
def main():
    list=[]
    n=int(input("Enter the Number:"))
    for i in range(1,n+1):
        if n%i==0:
            list.append(i)
    print("The factors of number are:", list)
    mylist1=[]
    for n in list:
        if n%2==0:
            mylist1.append(n)
    print("Even factor list:",mylist1)
    mylist2=[]
    for n in list:
        if n%2!=0:
            mylist2.append(n)
    print("Odd factor list:",mylist2)
    thread1=threading.Thread(target=evenfactor,args=(mylist1,))
    thread2=threading.Thread(target=oddfactor,args=(mylist2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exit from Main")
if __name__=="__main__":
    main()