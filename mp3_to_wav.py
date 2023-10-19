import os
import subprocess

def convert_mp3_to_wav(mp3_filepath, wav_filepath):
    """Convert an MP3 file to WAV format using ffmpeg."""
    command = [
        'ffmpeg',
        '-i', mp3_filepath,
        '-acodec', 'pcm_s16le',   # Set audio codec to pcm_s16le for WAV format
        '-ac', '1',               # Set audio channels to mono
        '-ar', '16000',           # Set audio rate to 16000 Hz
        wav_filepath
    ]
    subprocess.run(command, check=True)

def main():
    # Path to source MP3 files and destination for WAV files
    source_directory = 'Documents/Audios/mp3'
    destination_directory = 'Documents/Audios/wav'

    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List all MP3 files in the source directory
    files = [f for f in os.listdir(source_directory) if f.endswith('.mp3')]

    for f in files:
        mp3_filepath = os.path.join(source_directory, f)
        # Replace the '.mp3' extension with '.wav' for the output file
        wav_filename = f'{os.path.splitext(f)[0]}.wav'
        wav_filepath = os.path.join(destination_directory, wav_filename)

        convert_mp3_to_wav(mp3_filepath, wav_filepath)
        print(f"Converted {mp3_filepath} to {wav_filepath}")

if __name__ == '__main__':
    main()
