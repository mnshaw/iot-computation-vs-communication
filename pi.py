import speech_recognition as sr
import time
import os

time1 = time.time()

r = sr.Recognizer()

audioFile = sr.AudioFile(audioFilename)

with audioFile as source:
    audio = r.record(source)


time2 = time.time()
print("Transferred Audio File: ", time2-time1)

time.sleep(2)
recognized = r.recognize_sphinx(audio)

print(recognized)

f = open(resultsFilename, "w")
f.write(recognized)
f.close()
time.sleep(2)

time3 = time.time()
print("Finished Recognition: ", time3-time2)
