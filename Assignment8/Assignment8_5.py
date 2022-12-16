import threading

def Thread1(no1):
    for i in range(1,51):
        print(i ,end="  ")

def Thread2(no2):
    print()
    for i in range(50,0,-1):
        print(i ,end="  ")

if __name__=="__main__":
    no1=(1,50)
    no2=(50,0)
    thread1=threading.Thread(target=Thread1,args=(no1,))
    thread2=threading.Thread(target=Thread2,args=(no2,))
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()