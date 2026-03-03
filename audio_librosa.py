import numpy as np
import librosa

class AudioFileLibrosa:
    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.samplerate = None

    def load(self):
        y, sr = librosa.load(self.path, sr=None, mono=True)
        self.data = y.astype(np.float32)
        self.samplerate = sr

    def get_duration(self):
        return len(self.data) / self.samplerate

    def get_rms(self):
        return np.sqrt(np.mean(self.data ** 2))

    def get_time_axis(self):
        return np.arange(len(self.data)) / self.samplerate

    def get_rms_over_time(self, window_size=1024):
        rms_values = []
        for i in range(0, len(self.data), window_size):
            window = self.data[i:i + window_size]
            if len(window) > 0:
                rms_values.append(np.sqrt(np.mean(window ** 2)))
        return np.array(rms_values)

    def compute_spectrogram(self):
        import matplotlib.mlab as mlab
        return mlab.specgram(self.data, Fs=self.samplerate)
