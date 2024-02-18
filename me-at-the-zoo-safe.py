import webbrowser, time, os
def shutdown():
    os.system("shutdown /s /t 30")
    zooopen()
    

def zooopen():
    webbrowser.open ("https://www.youtube.com/watch?v=jNQXAC9IVRw")
    zooopen()

shutdown()