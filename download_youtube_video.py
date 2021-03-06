#!/usr/bin/env python

import urllib
import argparse
import os
import subprocess
import sys


#Script Info goes here.
__info__ = {
    'title': "Download Youtube video",
    'description': "Download Youtube video",
    'url': "http://github.com/TonkWorks/download_a_youtube_video/archive/master.zip",
    'author': "Kevin Dagostino",
    'input': [
    {
        'label': 'Youtube URL',
        'type': 'text',
        'map': 'youtube_url',
    }
    ]

}


#And the actual script.
def script():
    parser=argparse.ArgumentParser()
    parser.add_argument('--youtube_url')
    args=parser.parse_args()

    print("ARGS:")
    print(args)

    video_format = "mp4"
    root_path = os.path.dirname(os.path.realpath(__file__))

    command = ''
    if sys.platform == 'win32':
        #Windows only
        youtube_dl_exe_path = os.path.join(root_path, "youtube-dl.exe")
        command = "\"" + youtube_dl_exe_path + "\" {0} -f {1}".format(args.youtube_url, video_format)
    else:
        raise("Not implmented for max/linux yet")
        #command = "youtube-dl {0} -f {1}".format(site_url, video_format)

    print(command)
    p =subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()

    # if audio_format:
    #     #Get all mp4 files in bin.
    #     for f in os.listdir(os.getcwd()):
    #         if '.mp4' in f:
    #             fileName, fileExtension = os.path.splitext(f) 
    #             audio_input = AudioSegment.from_file(f, 'mp4')
    #             output_file_name = str(fileName + '.' + audio_format)
    #             audio_input.export(output_file_name, format=audio_format)

    #             print(output_file_name)

if __name__ == '__main__':
    script()


