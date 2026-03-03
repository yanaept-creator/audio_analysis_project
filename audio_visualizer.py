import matplotlib.pyplot as plt

class AudioVisualizer:
    def __init__(self, audio_file):
        self.audio = audio_file

    def plot_waveform(self):
        time_axis = self.audio.get_time_axis()

        plt.figure(figsize=(10,4))
        plt.plot(time_axis, self.audio.data)
        plt.title("Waveform")
        plt.xlabel("Czas [s]")
        plt.ylabel("Amplituda")
        plt.grid()
        plt.show()

    def plot_rms(self):
        rms_values = self.audio.get_rms_over_time()
        plt.figure(figsize=(10,4))
        plt.plot(rms_values)
        plt.title("RMS w czasie")
        plt.xlabel("Okno czasowe")
        plt.ylabel("RMS")
        plt.grid()
        plt.show()

    def plot_spectrogram(self):
        plt.figure(figsize=(10,4))
        plt.specgram(self.audio.data, Fs=self.audio.samplerate)
        plt.title("Spektrogram (FFT)")
        plt.xlabel("Czas")
        plt.ylabel("Częstotliwość")
        plt.colorbar()
        plt.show()
