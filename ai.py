import pyttsx3  as pt
import speech_recognition as sr 
# cmd=''
# listener=sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print("listenning...")
#         voice=listener.listen(source)
#         cmd=listener.recognize_google(voice)
#         print(cmd)
#         engine = pt.init()
#         engine.say(cmd)
#         engine.runAndWait()
# except:
#     pass

engine = pt.init()
engine.say("She can still come downstairs with assistance but she's very weak. Any assistance you could give the police will be greatly appreciated. Employees are being offered assistance in finding new jobs. We shall offer you assistance with legal expenses up to $5,000.")
engine.runAndWait()

