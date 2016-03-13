from __future__ import print_function

import os
from ffprobe3 import FFProbe
from ffprobe3.exceptions import FFProbeError

test_dir = os.path.dirname(os.path.abspath(__file__))

test_videos = [
    os.path.join(test_dir, './data/SampleVideo_720x480_5mb.mp4'),
    os.path.join(test_dir, './data/SampleVideo_1280x720_1mb.mp4'),
    os.path.join(test_dir, './data/SampleVideo_360x240_50mb.mp4'),
    os.path.join(test_dir, './data/SampleVideo_1280x720_50mb.mp4'),
]

for test_video in test_videos:
    media = FFProbe(test_video)
    print('File:', test_video)
    print('\tStreams:', len(media.streams))
    for index, stream in enumerate(media.streams, 1):
        print('\tStream: ', index)
        try:
            if stream.is_video():
                frame_rate = stream.frames() / stream.duration_seconds()
                print('\t\tFrame Rate:', frame_rate)
                print('\t\tFrame Size:', stream.frame_size())
            print('\t\tDuration:', stream.duration_seconds())
            print('\t\tFrames:', stream.frames())
            print('\t\tIs video:', stream.is_video())
        except FFProbeError as e:
            print(e)
        except Exception as e:
            print(e)
