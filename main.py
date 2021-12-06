#Istediğin süre kadar konuşmanı kayıt alan ve speechrecord.text'e yazdıran program.
#Pyaudio gerekli bazen hata veriyor, "pip install pipwin" yaptıktan sonta "pip install pyaudio" yapabilirsiniz
#A program that records your speech for as long as you want and writes it to speechrecord.text.
#"pip install pyaudio" sometime gives error, you can "pipwin install pipwin" then "pip install pyaudio" and you won't get error



import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic)
    selected_duration = int(input("ne kadar süre: "))
    data = r.record(mic, duration=selected_duration)
    text = r.recognize_google(data, language= "tr-TR")
    f = open("speechrecords.txt", "a")
    f.write(f"\n{text}\n")
    f.close()
