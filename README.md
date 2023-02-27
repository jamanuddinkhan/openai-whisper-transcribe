# Transcribe your video file using open AI whisper

To begin, the first requirement is to have Python 3.10 installed on your system. Once you have that, you can easily install the Open AI whisper package by following these simple steps. Additionally, you will also need FFmpeg.

Next, we need to call whisper to load the model, which will initiate a download process. After that, we can specify the video and audio files we want to transcribe. These files should be accessible on your machine, and the video file must exist. In my case, I have the video file available in the specified location.

The first step in the transcription process is to convert the video file into an MP3 format. Then, the transcription process will commence, which may take a considerable amount of time depending on the size of your video. FFmpeg will run during this process.

And there you have it, our transcription is complete! The process is straightforward, easily accessible, and provides a robust transcription, as demonstrated above.

#(On Linux)

# Step 1: System update
sudo apt update && sudo apt upgrade

# Step 2: Install Python 3
sudo apt install python3

# Step 3: Install pip
sudo apt install python3-pip

# Step 4: Install open AI whisper
pip install openai-whisper


# Step 5: Install ffmpeg
sudo apt install ffmpeg

## Step 6: run the following command
python main.py
