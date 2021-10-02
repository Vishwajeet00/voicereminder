import time
from plyer import notification
import pyttsx3
time.sleep(3)
s=pyttsx3.init()
s.say(" good morning ")
notification.notify(title="good morning",
      message="it's time to go ",
      timeout =5)
s.runAndWait()
   