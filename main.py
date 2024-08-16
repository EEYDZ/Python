import scipy
import wavio
import sounddevice

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


f = 44100

dur = 10

recording = sd.rec(int(dur * f), samplerate=f, channels=2)

sd.wait()

write("recording1.wav",f,recording)

wv.write("recording2.wav",recording,f,sampwidth=2)