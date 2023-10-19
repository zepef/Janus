import os
import subprocess

def transcribe_wav_to_text(wav_filepath, txt_filepath):
    """Transcribe a WAV file to text using Whisper ASR."""
    command = [
        'whisper',
        '--model', 'large-v2',  # Choose an appropriate model: base, medium, large, etc.
        '--device', 'cuda',     # Choose an appropriate device: cpu or cuda
        wav_filepath
    ]

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)
    transcription = result.stdout.decode('utf-8')

    # Write the transcription to a text file
    with open(txt_filepath, 'w') as file:
        file.write(transcription)

def main():
    # Path to source WAV files and destination for text files
    source_directory = 'Documents/Audios/wav'
    destination_directory = 'Documents/Texts'

    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List all WAV files in the source directory
    files = [f for f in os.listdir(source_directory) if f.endswith('.wav')]

    for f in files:
        wav_filepath = os.path.join(source_directory, f)
        # Replace the '.wav' extension with '.txt' for the output file
        txt_filename = f'{os.path.splitext(f)[0]}.txt'
        txt_filepath = os.path.join(destination_directory, txt_filename)

        transcribe_wav_to_text(wav_filepath, txt_filepath)
        print(f"Transcribed {wav_filepath} to {txt_filepath}")

if __name__ == '__main__':
    main()
