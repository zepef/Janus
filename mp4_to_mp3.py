import os
import subprocess

def convert_mp4_to_mp3(mp4_filepath, mp3_filepath):
    """Convert an MP4 file to MP3 format using ffmpeg."""
    command = [
        'ffmpeg',
        '-i', mp4_filepath,
        '-q:a', '0',  # best audio quality
        '-map', 'a',
        mp3_filepath
    ]
    subprocess.run(command, check=True)

def main():
    # Path to source MP4 files and destination for MP3 files
    source_directory = 'Documents\Videos'
    destination_directory = 'Documents\Audios'

    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List all MP4 files in the source directory
    files = [f for f in os.listdir(source_directory) if f.endswith('.mp4')]

    for f in files:
        mp4_filepath = os.path.join(source_directory, f)
        # Replace the '.mp4' extension with '.mp3' for the output file
        mp3_filename = f'{os.path.splitext(f)[0]}.mp3'
        mp3_filepath = os.path.join(destination_directory, mp3_filename)

        convert_mp4_to_mp3(mp4_filepath, mp3_filepath)
        print(f"Converted {mp4_filepath} to {mp3_filepath}")

if __name__ == '__main__':
    main()
