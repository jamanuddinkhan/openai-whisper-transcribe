import subprocess
import whisper
import ffmpeg
model = whisper.load_model('base')

video_in = 'sample.mp4'
audio_out = 'audio.mp3'

ffmpeg_cmd = f"ffmpeg -i {video_in} -vn -c:a libmp3lame -b:a 192k {audio_out}"

subprocess.run(["ffmpeg", "-i", video_in, "-vn", "-c:a", "libmp3lame", "-b:a", "192k", audio_out])

result = model.transcribe(audio_out)
print(result['text'])