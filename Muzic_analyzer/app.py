import librosa

# Funkcja pobierania audio
def load_audio(path):
    y, sr = librosa.load(path)   # y — dane audio, sr — Hz
    return y, sr

# Podaj ścieżkę do swojego pliku
audio_path = "samples/song.wav"   # Fail powinien znajdować się w folder samples

# Instalujemy audio
y, sr = load_audio(audio_path)

# Wyjście informacji
print("Audio zainstalowano!")
print("Liczba próbek:", len(y))
print("Hz:", sr)