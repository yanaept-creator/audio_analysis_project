import numpy as np
import librosa

class AudioFileLibrosa:
    def __init__(self, path: str):
        #atrybuty
        self.path = path              #path: str → sciezka do pliku audio (typ str)
        self.data = None              #data:  dane audio (probki)
        self.samplerate = None        #czestotliwosc probkowania (Hz)

    def load(self):
        y, sr = librosa.load(self.path, sr=None, mono=True)
        self.data = y.astype(np.float32)  #Zmieniamy typ danych na float32 (standard w przetwarzaniu audio)
        self.samplerate = sr

    def get_duration(self):
        return len(self.data) / self.samplerate

    def get_rms(self):
        rms_all=np.sqrt(np.mean(self.data ** 2))
        print(f'RMS: {rms_all}') # Liczy RMS (Root Mean Square)
        return rms_all

    def get_time_axis(self):            #zamienia probki na chwile czasowe w [sek]
        return np.arange(len(self.data)) / self.samplerate

    def get_rms_over_time(self, window_size=1024):  #Liczy RMS w oknach czasowych o dlugosci 1024 probki 2^10
        print("Okno czasowe:", window_size)
        rms_values = []
        k=0                                             #licznik okien
        for i in range(0, len(self.data), window_size):  #co 1024 próbki
            k=k+1
            window = self.data[i:i + window_size]
            if len(window) > 0:
                rms_values.append(np.sqrt(np.mean(window ** 2))) #liczy RMS w oknach czasowych i dodaje do
        print(f'Liczba okien czasowych: {k}')
        # for i, value in enumerate(rms_values):
        #     print(f"RMS okno {i}: {value}")
        return np.array(rms_values)     #zwraca tablice wartosci RMS w czasie

    def compute_spectrogram(self): #tworzy spektogram czyli wykres koloru na podstawie czestotliwosci i czasu)
        import matplotlib.mlab as mlab
        return mlab.specgram(self.data, Fs=self.samplerate)


#Test Back-End
if __name__ == "__main__":
    audio = AudioFileLibrosa("test.wav")
    audio.load()
    print(f'Test klasy AudioFileLibrosa na pliku: {audio.path}')
    print(f'Czas trwania pliku: {audio.get_duration()} s')
    audio.get_rms()
    print(f'Liczba probek: {len(audio.data)}')
    audio.get_rms_over_time()


