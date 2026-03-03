import tkinter as tk
from tkinter import filedialog, messagebox
from audio_librosa import AudioFileLibrosa
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sounddevice as sd
import threading
import time
import sys
import os



class AudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosta analiza dźwięku")
        self.audio = None
        self.play_thread = None
        self.stop_playback = False
        self.stream = None

        # ------------------- GUI -------------------
        self.left_frame = tk.Frame(root, width=250)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Przyciski
        self.load_btn = tk.Button(self.left_frame, text="Wczytaj audio", width=25, command=self.load_audio)
        self.load_btn.pack(pady=5)

        self.waveform_btn = tk.Button(self.left_frame, text="Waveform", width=25, command=self.show_waveform)
        self.waveform_btn.pack(pady=5)

        self.rms_btn = tk.Button(self.left_frame, text="RMS", width=25, command=self.show_rms)
        self.rms_btn.pack(pady=5)

        self.spec_btn = tk.Button(self.left_frame, text="Spektrogram", width=25, command=self.show_spectrogram)
        self.spec_btn.pack(pady=5)

        self.play_btn = tk.Button(self.left_frame, text="Odtwórz", width=25, command=self.toggle_play)
        self.play_btn.pack(pady=10)

        self.quit_btn = tk.Button(self.left_frame, text="Zakończ program", width=25, command=self.quit_program)
        self.quit_btn.pack(pady=10)

        # Wykresy
        self.fig, self.ax = plt.subplots(figsize=(6,4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    # ------------------- audio -------------------
    def load_audio(self):
        filepath = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.mp3")])
        if filepath:
            try:
                self.audio = AudioFileLibrosa(filepath)
                self.audio.load()
                self.ax.clear()
                self.canvas.draw()
                messagebox.showinfo("Sukces", f"Wczytano plik: {filepath}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku.\n{e}")

    # ------------------- wykresy -------------------
    def show_waveform(self):
        if self.audio:
            self.ax.clear()
            self.ax.plot(self.audio.get_time_axis(), self.audio.data, color="blue")
            self.ax.set_title("Waveform")
            self.ax.set_xlabel("Czas [s]")
            self.ax.set_ylabel("Amplituda")
            self.ax.grid(True)
            self.canvas.draw()
        else:
            messagebox.showwarning("Brak pliku", "Najpierw wczytaj plik audio.")

    def show_rms(self):
        if self.audio:
            self.ax.clear()
            rms = self.audio.get_rms_over_time()
            self.ax.plot(rms, color="green")
            self.ax.set_title("RMS w czasie")
            self.ax.set_xlabel("Okno")
            self.ax.set_ylabel("RMS")
            self.ax.grid(True)
            self.canvas.draw()
        else:
            messagebox.showwarning("Brak pliku", "Najpierw wczytaj plik audio.")

    def show_spectrogram(self):
        if self.audio:
            self.ax.clear()
            self.ax.specgram(self.audio.data, Fs=self.audio.samplerate)
            self.ax.set_title("Spektrogram")
            self.ax.set_xlabel("Czas [s]")
            self.ax.set_ylabel("Częstotliwość [Hz]")
            self.canvas.draw()
        else:
            messagebox.showwarning("Brak pliku", "Najpierw wczytaj plik audio.")

    # ------------------- odtwarzanie -------------------
    def toggle_play(self):
        if self.audio is None:
            messagebox.showwarning("Brak pliku", "Najpierw wczytaj plik audio.")
            return

        if self.play_thread and self.play_thread.is_alive():
            self.stop_playback = True
            self.play_btn.config(text="Odtwórz")
        else:
            self.stop_playback = False
            self.play_thread = threading.Thread(target=self.play_audio)
            self.play_thread.start()
            self.play_btn.config(text="Stop")

    def play_audio(self):
        sd.stop()
        sd.play(self.audio.data, samplerate=self.audio.samplerate)
        try:
            while sd.get_stream().active and not self.stop_playback:
                time.sleep(0.1)
        except Exception:
            pass
        sd.stop()

        # Zabezpieczenie przy zamknięciu okna
        try:
            self.play_btn.config(text="Odtwórz")
        except tk.TclError:
            pass

    # ------------------- zakończenie -------------------

    def quit_program(self):
        # zatrzymaj odtwarzanie
        self.stop_playback = True
        sd.stop()

        # zamknij stream jeśli istnieje
        if hasattr(self, 'stream') and self.stream is not None:
            try:
                self.stream.stop()
                self.stream.close()
            except Exception:
                pass

        # zamknij okno Tkinter
        self.root.destroy()

        # zakończ cały program natychmiast
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)





