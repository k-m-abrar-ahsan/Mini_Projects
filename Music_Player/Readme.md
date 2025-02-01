# Music Player Application

## Overview
This is a simple yet feature-rich **Music Player** built with **Python** using:
- **Tkinter** for GUI
- **Pygame** for audio playback
- **Mutagen** for MP3 metadata extraction
- **Ttkbootstrap** for a modern, themed interface

The application allows users to play, pause, resume, and stop MP3 tracks, navigate through a playlist, and scrub through audio with smooth performance.

## Features
✅ Load multiple MP3 files into a playlist  
✅ Play, pause, resume, and stop music  
✅ Navigate between previous and next tracks  
✅ Smooth scrubbing through the timeline **without lag**  
✅ Adjust volume control  
✅ Display track progress and duration  
✅ Double-click to play a song from the playlist  

## Technologies Used
- **Python** (Core language)
- **Tkinter** (GUI framework)
- **Pygame** (Audio playback engine)
- **Mutagen** (Extracting metadata like duration)
- **Ttkbootstrap** (Modern UI styling)

## Installation & Usage

### **Prerequisites**
Ensure Python and the necessary dependencies are installed.

```sh
pip install pygame mutagen ttkbootstrap
```

### **Running the Application**
Run the script using:

```sh
python music_player.py
```

## Code Structure
- **`MusicPlayer` Class**: Manages the entire music player functionality
- **Core Methods:**
  - `load_music()` → Opens a file dialog to load MP3 files
  - `play_music()` → Plays the selected song
  - `pause_music()` → Pauses the current song
  - `resume_music()` → Resumes playback
  - `stop_music()` → Stops the song and resets progress
  - `prev_song()` → Plays the previous track in the playlist
  - `next_song()` → Plays the next track in the playlist
  - `play_selected(event)` → Plays a song from the listbox
  - `set_volume(val)` → Adjusts the volume level
  - `track_progress()` → Updates progress bar & timestamp
  - `scrub_start(val)` → Handles scrubbing without lag
  - `scrub_end(event)` → Smoothly seeks within the track

## Known Issues
- None (Optimized for smooth performance) 🎵

## Future Enhancements
🔹 **Save & Load Playlists**  
🔹 **Add Shuffle & Repeat Features**  
🔹 **Display Album Art & Song Metadata**  
🔹 **Support for More Audio Formats**  
🔹 **Improve UI with Custom Themes & Animations**  

## License
This project is **open-source** and licensed under the **MIT License**.

## Contributions
Contributions are **welcome**! Feel free to **submit pull requests** or **open issues** on GitHub.

Happy coding! 🎶🚀

