import os
from moviepy import AudioFileClip

# === Set your folder path here ===
folder_path = "E"

# === Optional: create an output folder ===
output_folder = os.path.join(folder_path, "converted_mp3")
os.makedirs(output_folder, exist_ok=True)

# Loop through all .webm files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".webm"):
        webm_file = os.path.join(folder_path, filename)
        mp3_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")
        
        print(f"Converting: {filename} → {os.path.basename(mp3_file)}")
        try:
            audio_clip = AudioFileClip(webm_file)
            audio_clip.write_audiofile(mp3_file)
            audio_clip.close()
        except Exception as e:
            print(f"❌ Error converting {filename}: {e}")

print("✅ All done!")
