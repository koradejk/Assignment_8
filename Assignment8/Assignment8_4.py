import os
import threading
def Small(str):
    print("Thread name of Thread:",threading.current_thread().name)
    print("PID of Small Thread is:",os.getpid())
    small=0
    for letter in str:
        if letter.islower():
            small=small+1
    print("Number of Small Characters:",small)
def Capital(str):
    print("Thread name of Thread:", threading.current_thread().name)
    print("PID of Capital Thread is",os.getpid())
    capital = 0
    for letter in str:
        if letter.isupper():
            capital = capital + 1
    print("Number of Capital  Characters:", capital)
def Digit(str):
    print("Thread name of Thread:", threading.current_thread().name)
    print("PID of Digit Thread is:",os.getpid())
    digit=0
    for letter in str:
        if letter.isdigit():
            digit=digit+1
    print("Number of Digit:",digit)
if __name__=="__main__":
    str=input("Enter the Name:")
    thread1=threading.Thread(target=Small,args=(str,),name="SmallThread")
    thread2=threading.Thread(target=Capital,args=(str,),name="CapitalThread")
    thread3=threading.Thread(target=Digit,args=(str,),name="DigitThread")
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
