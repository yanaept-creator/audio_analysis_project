import tkinter as tk
from gui_app import AudioApp

root = tk.Tk()  #tworzy główne okno aplikacji, zmienna root przechowuje to okno, w którym będą wszystkie widżety (przyciski, wykresy, suwaki).
app = AudioApp(root) #obiekt klasy AudioApp
root.geometry("1200x550") # rozmiar okna giu
root.mainloop()  #uruchamia pętlę zdarzeń, dzięki której aplikacja reaguje na kliknięcia przycisków, wpisywanie tekstu, rysowanie wykresów itp.


