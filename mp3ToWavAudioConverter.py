import subprocess
import sys
import os

def convert1(inputFiles):
    cmd = ["ffmpeg"]
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