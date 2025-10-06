During my internship with Glendor ([click here](https://glendor.com/)) I needed to input 19 mp3 files into three or four different AI transcribers.\
The audio files ranged from 1 to 18 minutes long and some of the AI models required inputs of only 60 or 30 seconds.\
I wrote these two programs to do to things:\
  1) convert the audio from mp3 to 24 000 Hz wav format. Some of the AI models required this because they were trained on this format\
  2) Split the files into 60 second chunks, and also split the files into 30 second chunks Because the models had different audio length requirements.

The code uses FFMPEG to manipulate the audio by first reading the directory to detect the audio files, then constructing a bash command that will run FFMPEG according to the audio processing needs, then it runs the bash command in a subprocess, which calls FFMPEG to do the audio processing.

