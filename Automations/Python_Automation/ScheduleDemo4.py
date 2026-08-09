import schedule
import time
import datetime
import psutil


def Display():
    print("Jay Ganesh...",datetime.datetime.now())
    print("RAM Usage : ",psutil.cpu_percent)
    print("no of cpu cores : ",psutil.cpu_count)

def main():
    print("Automation Script Started")

    schedule.every(10).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End of Automation script")

if __name__ == "__main__":
    main()