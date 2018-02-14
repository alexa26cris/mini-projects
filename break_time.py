import webbrowser   #module importing
import time

counter = 0
while (counter <3):
    time.sleep(3)   #time in seconds
    webbrowser.open("https://www.youtube.com/watch?v=mWRsgZuwf_8")  #opens the webbrowser
    counter = counter + 1
