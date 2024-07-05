from datetime import datetime

def Hello():
    time = datetime.now()
    current_time = time.strftime('%H:%M:%S')
    
    name = input("What is your name?: ")

    print("Hello",name,"the time is:",current_time)

if __name__ == '__main__':
    Hello()