import os
import whisper

# Path for directory/file you want to transcribe
# Needs to be setup as an argument for CLI command
root = os.path.join(os.path.dirname(__file__), '..')
to_trans = os.path.join(root, 'assets')

try:
    os.mkdir(os.path.join(root, 'transcriptions'))
except OSError as error:
    print(error)
# Loading Whisper model
model = whisper.load_model("base")

# Iterate through files in to_trans folder
for dirpath, dirnames, filenames in os.walk(to_trans):
    for filename in filenames:
        # Needs support for more file types
        if filename.endswith(".mp3"):
            filepath = os.path.join(dirpath, filename)
            # Have verbose as a flag for the command
            result = model.transcribe(filepath, fp16=False)
            transcription = result['text']
            # Write transcription to text file
            filename_no_ext = os.path.splitext(filename)[0]
            with open(os.path.join(os.path.join(root, 'transcriptions'), filename_no_ext + '.txt'), 'w') as f:
                f.write(transcription)
