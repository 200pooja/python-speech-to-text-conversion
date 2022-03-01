import speech_recognition as sr  
r = sr.Recognizer()  
with sr.Microphone() as source:  
    print("recite the shloka :")  
    audio = r.listen(source)  
    try:  
        text = r.recognize_google(audio)  
        print("You recited : {}".format(text))  
         
          
    except:  
        print("Sorry could not recognize what you said TRY AGAIN !!")
        