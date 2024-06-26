import subprocess
import sys
import os

#This was written for a UNIX system with ffmpeg installed
#in order to run you need to put .mp3 files in the same folder/directory as this file, then run this python file ( run this command: python3 mp3ToWavAudioConverter.py)
def convert1(inputFiles):
    #This cmd variable will hold the command to send to the unix terminal
    cmd = ["ffmpeg"]
    #For each input file we will add the necessary arguments to the unix command to run ffmpeg.
    for i in inputFiles:
        cmd += ["-i", "{a}.mp3".format(a=i[:-4])]
    x = 0
    for i in inputFiles:
        cmd += ["-map", "{index}:a".format(index=x), "-ac", "1", "-ar", "16000", "output/{a}.wav".format(a=i[:-4])]
        x+=1
    subprocess.run(cmd)

if __name__ == "__main__":
    fileList = []
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            fileList += [file]
    convert1(fileList)

#"ffmpeg -i a1.mp3 -i a2.mp3 -map 0:a -ar 16000 a1.wav -map 1:a -ar 16000 a2.wav"
