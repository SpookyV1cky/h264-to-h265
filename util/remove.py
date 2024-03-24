import os
import ffmpeg
import sys
import time
from util.db import db_save
from os.path import join, getsize

def delete_all():

    rootfolder = input("folder path: ")
    print(" Scanning... ")

    for root, dirs, files in os.walk(rootfolder):
        
        for name in files:
                
                if(name.split('.').pop() == 'mp4'):
                    video = os.path.join(root, name)
                    
                    metadata = ffmpeg.probe(video)
                    codec = metadata['streams'][0]['codec_name']
                    
                    if(codec == 'h264'):
                        print("Deleting " + name + "...")
                        os.remove(video)
                    else:
                        print("ignoring " + name + " [NOT H.264] " + codec)
    
    print("[ See you later :3 ]")

def delete_complete(tasklist):
    
    for task in tasklist:
        if(task['status'] == True):
            try:
                print("Deleting " + task['name'] + "...")
                os.remove(task['path'])
            except:
                time.sleep(0.5)
                print(' \n UnU Bye Bye </3 ')
                break
    tasklist = []
    db_save(tasklist)            