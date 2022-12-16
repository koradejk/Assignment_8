import threading
def even(x):
    print("Thread name of even:", threading.current_thread().name)
    for i in range(1,21):
        if i%2==0:
            print(i, end="  ")
def odd(x):
    print()
    print("Thread name of odd:",threading.current_thread().name)
    for i in range(x):
        if (i%2==1):
            print(i,end="  ")
        i=i+1
if __name__=="__main__":
    no1=21
    #print()
    no2=20
    thread1=threading.Thread(target=even, args=(no1,),name="EvenThread")
    thread2=threading.Thread(target=odd, args=(no2,),name="OddThread")
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()