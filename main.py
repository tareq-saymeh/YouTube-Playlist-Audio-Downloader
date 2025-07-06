import os
import sys
import yt_dlp
from moviepy import AudioFileClip


def download_playlist(playlist_url):
    # Use a valid output path that exists
    if os.path.exists('E:/') and os.access('E:/', os.W_OK):
        output_path = 'E'
    else:
        output_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'youtube_audio')
    
    ydl_opts = {
        'format': 'bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'ignoreerrors': True,
        'no_warnings': True,
    }
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"\nDownload complete! Files saved to: {output_path}")
        print("Note: Files are in .webm or .m4a format")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    
    print("YouTube Playlist Audio Downloader")
    print("--------------------------------")
    playlist_url = input("Enter playlist URL: ")
    
    if not playlist_url.startswith(('https://www.youtube.com/', 'https://youtube.com/')):
        print("Please enter a valid YouTube playlist URL")
        sys.exit(1)
    
    download_playlist(playlist_url)
    