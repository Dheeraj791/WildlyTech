import os
import sys
from pydub import AudioSegment

if len(sys.argv) != 3:
    print("Usage: python mp3_to_wav.py mp3_folder_path wav_folder_path")
    sys.exit(1)

mp3_folder_path = sys.argv[1]
wav_folder_path = sys.argv[2]

if not os.path.exists(mp3_folder_path):
    print(f"Error: {mp3_folder_path} does not exist.")
    sys.exit(1)

if not os.path.exists(wav_folder_path):
    os.makedirs(wav_folder_path)

for filename in os.listdir(mp3_folder_path):
    if filename.endswith(".mp3"):
        mp3_file_path = os.path.join(mp3_folder_path, filename)
        wav_file_path = os.path.join(wav_folder_path, filename[:-4] + ".wav")
        sound = AudioSegment.from_mp3(mp3_file_path)
        sound.export(wav_file_path, format="wav")

print("Conversion complete!")
