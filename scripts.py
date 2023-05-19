import os
import sys
from pydub import AudioSegment

def convert_to_wav(mp3_folder, wav_folder):
    # Check if the output folder exists, create it if not
    if not os.path.exists(wav_folder):
        os.makedirs(wav_folder)

    # Convert each MP3 file to WAV format
    for filename in os.listdir(mp3_folder):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(mp3_folder, filename)
            wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + '.wav')
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format='wav')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mp3_folder> <wav_folder>")
    else:
        mp3_folder = sys.argv[1]
        wav_folder = sys.argv[2]
        convert_to_wav(mp3_folder, wav_folder)
