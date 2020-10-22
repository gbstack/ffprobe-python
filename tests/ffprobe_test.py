from __future__ import print_function

import unittest
import os
from ffprobe import FFProbe
from ffprobe.exceptions import FFProbeError

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


class FFProbeTest(unittest.TestCase):
    def test_video(self):
        for test_video in test_videos:
            try:
                media = FFProbe(test_video)
                self.assertIsNotNone(media)
                print('File:', test_video)
                print_ffprobe(media)
            except FFProbeError as e:
                raise e
            except Exception as e:
                raise e

    def test_stream(self):
        for test_stream in test_streams:
            try:
                media = FFProbe(test_stream)
                self.assertIsNotNone(media)
                print('Stream URL:', test_stream)
                print_ffprobe(media)
            except FFProbeError as e:
                raise e
            except Exception as e:
                raise e


def print_ffprobe(media: FFProbe):
    print('\tFormat:', media.format.format_name, "(", media.format.format_long_name, ")")
    print('\tStreams:', len(media.streams))
    for index, stream in enumerate(media.streams, 1):
        print('\tStream: ', index)
        print('\t\tCodec:', stream.codec_description())
        if stream.is_video():
            print('\t\tFrame Rate:', stream.frame_rate())
            print('\t\tFrame Size:', stream.frame_size())
        print('\t\tDuration:', stream.duration_seconds())
        print('\t\tFrames:', stream.frames())
        print('\t\tIs video:', stream.is_video())


if __name__ == '__main__':
    unittest.main()
