import os
import ffmpeg
from os.path import join, getsize
from util.db import *

def find_something():

    rootfolder = input("folder path: ")
    
    print(" Scanning... ")

    for root, dirs, files in os.walk(rootfolder):
        
        for name in files:
                
                if(name.split('.').pop() == 'mp4'):
                    video = os.path.join(root, name)
                    
                    metadata = ffmpeg.probe(video)

                    for stream in metadata['streams']:

                        if (stream['codec_type'] == 'video'):
                            codec = stream['codec_name']
                            bit_rate = stream['bit_rate']

                        elif(stream['codec_type'] == 'audio'):

                            audio_codec = stream['codec_name']
                            audio_bitrate = stream['bit_rate']

                    if(codec == 'h264'):

                        out = os.path.join(root, "h265_" + name)
                        tasklist.append({
                         "name":name,
                         "path":video,
                         "out":out,
                         "bit_rate":bit_rate,
                         "audio_codec":audio_codec,
                         "audio_bitrate":audio_bitrate,
                         "status": False
                        })
    print(" [ OK ] ")
    db_save(tasklist)
    return tasklist