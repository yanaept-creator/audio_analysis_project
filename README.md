# audio_analysis_project
Opis projektu:

Projekt jest prostą aplikacją desktopową w Pythonie do analizy sygnałów audio z wykorzystaniem bibliotek Tkinter, Librosa, NumPy, Matplotlib oraz SoundDevice.

Jego głównym celem jest umożliwienie użytkownikowi wczytania pliku dźwiękowego (np. WAV lub MP3), przeanalizowania go oraz wizualizacji podstawowych parametrów sygnału w czytelnej formie graficznej.
Aplikacja pozwala wyświetlić:
- przebieg czasowy sygnału (waveform),
- zmianę energii sygnału w czasie (RMS),
- spektrogram przedstawiający rozkład częstotliwości w funkcji czasu.

Dodatkowo program oblicza i wypisuje w terminalu podstawowe parametry pliku, takie jak czas trwania, liczba próbek, częstotliwość próbkowania oraz wartość RMS, a także umożliwia odtwarzanie dźwięku i zapisywanie wygenerowanych wykresów do plików graficznych.



1. plik audio_librosa.py - wczytanie i analiza pliku audio (np. wav) przy uzyciu biblioteki librosa i numpy
klasa: AudioFileLibrosa
metody: load - wczytanie danych z pliku audio (próbki, czestotliwośc)
        duration -oblicza dlugosc pliku w sekundach czas= liczba_próbek / próbki_na_sekundę
        get_rms - Liczy RMS (Root Mean Square) miara energii sygnału
        get_time_axis - Tworzy oś czasu do wykresu,
                        poprzez zamianę probek na sekundy .np. [0, 1, 2, 3, ..., N]/Hz = czas
        get_rms_over_time - Liczy RMS w małych oknach czasowych windowsize =1024
        compute_spectrogram - tworzy spektogram czyli wykres koloru na podstawie czestotliwosci i czasu
2. plik main.py - plik główny programu wykorzystujący biblioteke tkinter do tworzenia GUI.
            Wykorzystuje wszystkie metody z klasy AudioApp
3. plik gui_app.py - pozwala użytkownikowi wybierać pliki i wyświetlać wykres
klasa AudioApp: definiuje wszystkie widżety GUI: przyciski, pola tekstowe, wykresy, funkcje do interakcji z użytkownikiem.
konstruktor : __init__(self, root)   - Inicjalizuje aplikację GUI, tworzy układ okna, przyciski oraz obszar wykresu i przygotowuje zmienne do obsługi audio oraz odtwarzania.
metody: load_audio(self)-otwiera okno wyboru pliku, wczytuje plik audio, wyświetla jego podstawowe parametry w terminalu i czyści obszar wykresu.
        show_waveform(self) - rysuje przebieg czasowy sygnału (amplituda w funkcji czasu) na obszarze wykresu w GUI.
        show_rms(self)  -oblicza i wyświetla wykres RMS sygnału w funkcji kolejnych okien czasowych.
        show_spectrogram(self) -generuje i wyświetla spektrogram sygnału pokazujący rozkład częstotliwości w czasie.
        toggle_play(self) - przełącza stan odtwarzania audio między startem a zatrzymaniem, zarządzając wątkiem odtwarzającym.
        play_audio(self) - odtwarza sygnał audio w osobnym wątku i monitoruje jego stan do momentu zakończenia lub zatrzymania.
        save_current_plot(self) - otwiera okno zapisu i zapisuje aktualnie wyświetlany wykres do pliku graficznego (PNG/JPG/PDF).
        quit_program(self) -bezpiecznie zatrzymuje odtwarzanie, zamyka zasoby audio oraz kończy działanie całej aplikacji.


