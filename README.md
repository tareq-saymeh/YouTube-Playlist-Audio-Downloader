
---

# 🎵 YouTube Playlist Audio Downloader & Converter

This Python project allows you to **download audio from YouTube playlists** and **convert `.webm` audio files into `.mp3` format** for easy listening on any device.

---

## 📁 Project Structure

```
📦 youtube-audio-downloader
├── main.py          # Downloads audio from a YouTube playlist
├── convert.py       # Converts downloaded .webm audio files to .mp3
└── README.md        # Project documentation
```

---

## 🚀 Features

- Download best-quality audio from YouTube playlists using `yt-dlp`
- Automatically handles `.webm` and `.m4a` formats
- Converts `.webm` audio files to `.mp3` using `moviepy`
- Saves files to a user-writable directory (default: `E:/` or `~/Downloads/youtube_audio`)
- Automatically installs missing dependencies (like `yt-dlp`)

---

## 🛠️ Requirements

- Python 3.6+
- Packages:
  - `yt-dlp`
  - `moviepy`

Install dependencies:

```bash
pip install yt-dlp moviepy
```

---

## 📥 How to Use

### Step 1: Download Playlist Audio

Run the downloader:

```bash
python main.py
```

Enter a valid YouTube playlist URL when prompted.  
Audio files will be saved as `.webm` or `.m4a` files in:

- `E:/` (if writable), or
- `~/Downloads/youtube_audio`

---

### Step 2: Convert to MP3

Once the playlist is downloaded, convert all `.webm` files to `.mp3`:

```bash
python convert.py
```

Converted `.mp3` files will be saved in a `converted_mp3` subfolder inside the audio directory.

---

## 📝 Notes

- `convert.py` only processes `.webm` files. If your audio is in `.m4a`, you can enhance the script to support it.
- This script assumes all downloads are stored in the same directory (`E:/` by default). You can change this path in the code (`folder_path`).

---

## 📌 Example

**Download:**
```
$ python main.py
Enter playlist URL: https://www.youtube.com/playlist?list=PLxxxx
```

**Convert:**
```
$ python convert.py
Converting: Song 1.webm → Song 1.mp3
Converting: Song 2.webm → Song 2.mp3
✅ All done!
```

---

## 📄 License

This project is open-source and free to use. Feel free to modify it for your needs.

---
