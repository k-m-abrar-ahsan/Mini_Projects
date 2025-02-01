import tkinter as tk
from tkinter import filedialog
import pygame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from mutagen.mp3 import MP3
import time
import threading

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.playing = False
        self.paused = False
        self.total_length = 0
        self.current_time = 0
        
        self.style = ttk.Style("darkly")
        
        self.current_song_label = ttk.Label(self.root, text="No song playing", bootstyle=INFO, wraplength=300)
        self.current_song_label.pack(pady=5)
        
        self.label = ttk.Label(self.root, text="No files selected", wraplength=300, bootstyle=INFO)
        self.label.pack(pady=5)
        
        self.select_button = ttk.Button(self.root, text="Select Music Files", command=self.load_music, bootstyle=PRIMARY)
        self.select_button.pack(pady=5)
        
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", self.play_selected)
        
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(pady=10)
        
        self.prev_button = ttk.Button(self.control_frame, text="⏮ Prev", command=self.prev_song, bootstyle=INFO)
        self.prev_button.grid(row=0, column=0, padx=5)
        
        self.play_button = ttk.Button(self.control_frame, text="▶ Play", command=self.play_music, bootstyle=SUCCESS)
        self.play_button.grid(row=0, column=1, padx=5)
        
        self.pause_button = ttk.Button(self.control_frame, text="⏸ Pause", command=self.pause_music, bootstyle=WARNING)
        self.pause_button.grid(row=0, column=2, padx=5)
        
        self.resume_button = ttk.Button(self.control_frame, text="▶ Resume", command=self.resume_music, bootstyle=INFO)
        self.resume_button.grid(row=0, column=3, padx=5)
        
        self.stop_button = ttk.Button(self.control_frame, text="⏹ Stop", command=self.stop_music, bootstyle=DANGER)
        self.stop_button.grid(row=0, column=4, padx=5)
        
        self.next_button = ttk.Button(self.control_frame, text="⏭ Next", command=self.next_song, bootstyle=INFO)
        self.next_button.grid(row=0, column=5, padx=5)
        
        self.progress = ttk.Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.scrub)
        self.progress.pack(pady=10, fill=tk.X)
        
        self.time_label = ttk.Label(self.root, text="00:00 / 00:00", bootstyle=SECONDARY)
        self.time_label.pack(pady=5)
        
        self.volume_label = ttk.Label(self.root, text="Volume", bootstyle=INFO)
        self.volume_label.pack()
        
        self.volume_slider = ttk.Scale(self.root, from_=0, to=1, orient=HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(0.5)
        self.volume_slider.pack(pady=5)
        
    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        if files:
            self.playlist = list(files)
            self.listbox.delete(0, tk.END)
            for file in self.playlist:
                self.listbox.insert(tk.END, file.split("/")[-1])
            self.label.config(text="Loaded multiple songs")
    
    def play_music(self):
        try:
            if self.playlist:
                pygame.mixer.music.load(self.playlist[self.current_index])
                pygame.mixer.music.play(start=self.current_time)
                self.playing = True
                self.paused = False
                self.current_song_label.config(text=f"Playing: {self.playlist[self.current_index].split('/')[-1]}")
                audio = MP3(self.playlist[self.current_index])
                self.total_length = audio.info.length
                threading.Thread(target=self.track_progress, daemon=True).start()
        except Exception as e:
            print(f"Error in play_music: {e}")  # Debugging line
    
    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True
    
    def resume_music(self):
        pygame.mixer.music.unpause()
        self.paused = False
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.progress.set(0)
        self.time_label.config(text="00:00 / 00:00")
    
    def prev_song(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.current_time = 0
            self.play_music()
    
    def next_song(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.current_time = 0
            self.play_music()
    
    def play_selected(self, event):
        if self.listbox.curselection():
            self.current_index = self.listbox.curselection()[0]
            self.current_time = 0
            self.play_music()
    
    def set_volume(self, val):
        pygame.mixer.music.set_volume(float(val))
    
    def track_progress(self):
        while self.playing and pygame.mixer.music.get_busy():
            if not self.paused:
                self.current_time += 1  # Manually track time instead of relying on get_pos()
                
                # Disconnect the scrub callback to avoid recursion
                self.progress.configure(command="")
                self.progress.set((self.current_time / self.total_length) * 100)
                self.progress.configure(command=self.scrub)  # Reconnect the callback

                self.time_label.config(
                    text=f"{time.strftime('%M:%S', time.gmtime(self.current_time))} / "
                        f"{time.strftime('%M:%S', time.gmtime(self.total_length))}"
                )
            time.sleep(1)

    
    def scrub(self, val):
        try:
            if self.playing and self.total_length > 0:
                new_time = (float(val) / 100) * self.total_length  # Convert progress bar value to time
                self.current_time = new_time  # Update internal time tracker

                # Use set_pos() for seamless seeking without stopping playback
                pygame.mixer.music.set_pos(self.current_time)

                # Temporarily disable progress bar updates to prevent conflicts
                self.progress.configure(command="")
                self.progress.set((self.current_time / self.total_length) * 100)
                self.progress.configure(command=self.scrub)

                # Update the time label without excessive redrawing
                self.time_label.config(
                    text=f"{time.strftime('%M:%S', time.gmtime(self.current_time))} / "
                        f"{time.strftime('%M:%S', time.gmtime(self.total_length))}"
                )

        except Exception as e:
            print(f"Error in scrub: {e}")  # Debugging line



if __name__ == "__main__":
    root = ttk.Window()
    root.style.theme_use("darkly")
    app = MusicPlayer(root)
    root.mainloop()