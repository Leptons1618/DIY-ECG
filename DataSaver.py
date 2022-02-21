import sounddevice as sd
import wave as wv

fs = 44100
seconds = 60
wavFile = wv.open('sound.wav','w')
wavFile.setnchannels(1)
wavFile.setsampwidth(2)
wavFile.setframerate(fs)
myRec = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
wavFile.writeframesraw(myRec)
sd.wait()
wavFile.close()
