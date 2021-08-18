import random
from time import sleep

import librosa
import sounddevice as sd

tone1 = librosa.tone(880, sr=22050, length=1000)


audio, sr = librosa.load('kick10.wav')
audio2, sr2 = librosa.load('snare10.wav')
# sd.play(audio, sr)
tone2 = librosa.tone(440, sr=22050, length=1000)
# tone3 = librosa.tone(220, sr=22050, length=1000)

# import pyaudio
# import wave
cSuvDiv=0

SuvDivBas=0
SuvDivCla=0
Seed=random.random()
# Seed=0.5162471699862949
print(Seed)


def generarRitmo(seed):
    random.seed(seed)
    cSuvDiv=random.choice([3,4])
    SuvDivBas=random.choice([4])
    return cSuvDiv,SuvDivBas

cSuvDiv,SuvDivBas=generarRitmo(Seed)
print(cSuvDiv)
print(SuvDivBas)

dos=[]
tres=[3]
def crearClave(cSuvDiv):
    # random.seed(random)
    SuvDivCla=random.choice([cSuvDiv,cSuvDiv*2,cSuvDiv*4])
    for i in range(9):
        if sum(dos)<SuvDivCla:
            temp=random.randint(2, 3)
            if sum(dos)+temp<=SuvDivCla:
                dos.append(temp)
        else:
            break
    print(SuvDivCla)
    print(dos)
    return dos
div=crearClave(cSuvDiv)
print(div)
desg=[]
for i in div:
    if i==2:
        desg.append(1)
        desg.append(random.randint(2, 3))
    if i==3:
        desg.append(1)
        desg.append(random.randint(2, 3))
        desg.append(random.randint(2, 3))
print(desg+desg)
desg=desg+desg
bpm=200

# import simpleaudio as sa

# filename = 'kick10.wav'
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done()

import winsound

# filename = 'snare10.wav'
# winsound.PlaySound(filename, winsound.SND_FILENAME)

from playsound import playsound
# playsound('snare10.wav')
time = (60 / bpm - 0.1)
# print(time)
# sleep(time)
# playsound('snare10.wav',)

for i in desg:
    if i==1:
        # playsound('kick10.wav',)
        filename = 'kick18.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        filename = 'hihat4.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        # sd.play(audio, sr)
        # sd.play(tone1, 22050)
        sleep(time)
    if i==2:
        # playsound('snare10.wav')
        # sd.play(audio2, sr2)
        # sd.play(tone2, 22050)
        filename = 'sound1.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        sleep(time)
    if i==3:
        sleep(time)
1212312
1234567


print(desg)
# asd
