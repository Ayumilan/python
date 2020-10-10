import os
import pyttsx3

print("Welcome to the menu driven program, where you chat with it to open the required applications what you want, if it is not able to perform the task then we will update in the next version")
pyttsx3.speak("welcome to the menu driven program, where you chat with it to open the required applications what you want, if it is not able to perform the task then we will update in the next version")

while True:
      print("chat with me with your requirements : " , end='')
      pyttsx3.speak("chat with me with your requirements ")
      p = input()
      p=p.lower()

   if (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("google" in p) or ("chrome" in p) or("browser" in p)):
      pyttsx3.speak("opening chrome")
      os.system("chrome")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("notepad" in p) or ("editor" in p)):
      pyttsx3.speak("opening notepad")
      os.system("notepad")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p)or("open" in p)) and ("player" in p) and (("media" in p) or("video" in p)):
      pyttsx3.speak("opening windows media player")
      os.system("wmplayer")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and ("codeblocks" in p):
      pyttsx3.speak("opening codeblocks")
      os.system("codeblocks")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("calculator" in p)or("calc" in p)):
      pyttsx3.speak("opening calculator")
      os.system("calc")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("settings" in p) or ("settings" in p)):
      pyttsx3.speak("opening settings")
      os.system("start ms-settings:")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("paint" in p) or ("paint3d" in p)):
      pyttsx3.speak("opening paint")
      os.system("start ms-paint:")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and ("control panel" in p):
      pyttsx3.speak("opening control panel")
      os.system("control panel")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("webwhatsapp" in p) or ("whatsapp" in p) or ("what's app " in p)):
      pyttsx3.speak("opening whatsapp")
      os.system("chrome web.whatsapp.com")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and (("flipkart" in p)or("shopping" in p)):
      pyttsx3.speak("opening flipkart")
      os.system("chrome flipkart.com")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and ("twitter" in p):
      pyttsx3.speak("opening twitter")
      os.system("chrome twitter.com")
   elif (("do not" not in p) and ("dont" not in p) and ("don't" not in p)and ("never" not in p)and ("not" not in p)) and (("show" in p) or ("dispaly" in p) or("run" in p) or ("execute" in p ) or ("launch" in p) or("open" in p)) and ("date" in p):
      pyttsx3.speak("displaying date")
      os.system("date")
   elif ("exit" in p) or ("quit" in p):
      break
   else:
      print("we will update it in next version.")
      pyttsx3.speak("we will update it in next version. if you want to exit ,type exit or quit")
