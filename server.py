import speech_recognition as sr
import time
import os

time1 = time.time()

rpi = "pi@raspberrypi.local"

path = "AudioFiles/Large/OSR_us_000_0036_8k.wav"
audioFilename = "OSR_us_000_0036_8k.wav"
resultsFilename = "OSR_us_000_0036_8k.txt"

os.system('scp %s:%s ~/Desktop/' % (rpi, path))

r = sr.Recognizer()

# print("loading audio file")
# harvard = sr.AudioFile('harvard.wav')
audioFile = sr.AudioFile(audioFilename)

with audioFile as source:
    audio = r.record(source)


time2 = time.time()
print("Transferred Audio File: ", time2-time1)

time.sleep(2)
# print("running speech recognition")
recognized = r.recognize_sphinx(audio)

print(recognized)

f = open(resultsFilename, "w")
f.write(recognized)
f.close()
time.sleep(2)

time3 = time.time()
print("Finished Recognition: ", time3-time2)

os.system('scp %s %s:' % (resultsFilename, rpi))

time4 = time.time()
print("Transferred Results: ", time4-time3)

