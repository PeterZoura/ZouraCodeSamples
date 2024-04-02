import subprocess
import sys
import os

#To run this code put .wav files whose audio length is longer than 30 seconds in the same directory as this file then run this file (run: python3 wavToSmallerWavSplitter.py)
def convert2(inputFile):
    #Each input file needs it's own run of the ffmpeg program. The appropriate command is built with strings.
    cmd = ["ffmpeg"]
    cmd += ["-i", "{a}".format(a=os.path.join("output/", inputFile))]
    cmd += ["-f", "segment", "-segment_time", "30", "-c", "copy", "output/output30/{a}_%03d.wav".format(a=inputFile[:-4])]
    subprocess.run(cmd)

if __name__ == "__main__":
    fileList = []
    for file in os.listdir("./output"):
        if file.endswith(".wav"):
            fileList += [file]
    for file in fileList:
        convert2(file)

#"ffmpeg -i a1.mp3 -i a2.mp3 -map 0:a -ar 16000 a1.wav -map 1:a -ar 16000 a2.wav"
