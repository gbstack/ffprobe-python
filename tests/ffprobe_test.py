from __future__ import print_function

import os
from ffprobe import FFProbe
from ffprobe.exceptions import FFProbeError
from ffprobe.ffprobe import FFStream

test_dir = os.path.dirname(os.path.abspath(__file__))

test_videos = [
    os.path.join(test_dir, './data/SampleVideo_720x480_5mb.mp4'),
    os.path.join(test_dir, './data/SampleVideo_1280x720_1mb.mp4'),
]

# Taken from https://bitmovin.com/mpeg-dash-hls-examples-sample-streams
test_streams = [
    'https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8',
    'https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8'
]

def test_video ():
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

def test_stream ():
    for test_stream in test_streams:
        media = FFProbe(test_stream)
        print('File:', test_stream)
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

def test_ffstream_ignores_multiline_side_data ():
    stream = FFStream([
        'index=0\n',
        'codec_type=video\n',
        'avg_frame_rate=24/1\n',
        'displaymatrix=\n',
        '00000000:            0       65536           0\n',
        '00000001:       -65536           0           0\n',
        '\n',
        'rotation=-90\n',
    ])

    assert stream.index == '0'
    assert stream.codec_type == 'video'
    assert stream.displaymatrix == ''
    assert stream.rotation == '-90'
    assert stream.framerate == 24
