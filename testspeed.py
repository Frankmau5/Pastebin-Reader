import time
import AppBackend


def testNormal():
    l = AppBackend.AppLogic()
    start_time = time.time()
    l.GetAllData()
    duration = time.time() - start_time
    print(f"Downloaded Done in {duration} seconds")


def testSpeed():
    l = AppBackend.AppLogic()
    start_time = time.time()
    l.Run()
    duration = time.time() - start_time
    print(f"Downloaded Done in {duration} seconds")

if __name__ == "__main__":
    testNormal()
    testSpeed()