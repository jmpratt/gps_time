from L76GNSV4 import L76GNSS
from pytrack import Pytrack
from machine import RTC
from time import sleep, time #for sleep in seconds


def get_time():
    try:
        py = Pytrack()
        l76 = L76GNSS(py, timeout=120)
        timeout = time() + 30 #timeout in 30 seconds from now


        while timeout  > time(): # try until timeout
            date_time=l76.getUTCDateTime()  # get time from L76

            # 2080 is default year returned by L76 when no GPS signal detected
            if date_time[:4] != '2080': # prevents default value from L76 for date_time
                break
            sleep(2)  # wait before checking L76 time again
        else:
            date_time = '2000-01-01T00:00:00+00:00' # set to a vale if timeout occurs
            print('GPS time not found.  Setting clock to 01/01/2000')
        print(date_time)
        rtc = RTC()  # create real time clock
        #  init RTC with GPS UTC date & time
        rtc.init((int(date_time[0:4]),int(date_time[5:7]),int(date_time[8:10]),int(date_time[11:13]),int(date_time[14:16])))

    except:
        print('Unable to set time.')

if __name__ == "__main__":
    get_time()
