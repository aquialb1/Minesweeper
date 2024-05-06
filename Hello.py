from datetime import datetime

def Hello():
    time = datetime.now()
    current_time = time.strftime('%H:%M:%S')

    print("Hello Albert, the time is:",current_time)

if __name__ == '__main__':
    Hello()