import sounddevice
from scipy.io.wavfile import write

#sample_rate
fs=44100

try:
    second = int(input("Enter the recording time in second :"))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()  # Or provide a way to retry

print("Recording....\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("My Recording.wav", fs,record_voice)
print("Recording is done Please check you folder to listening recording")