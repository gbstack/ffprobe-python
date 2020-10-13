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


class FFProbeTest(unittest.TestCase):
    def test_video(self):
        for video in test_videos:
            media = FFProbe(video)
            print('File:', video)
            print('\tFormat:', media.format.format_name, "(", media.format.format_long_name, ")")
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
                    self.fail()
                except Exception as e:
                    print(e)
                    self.fail()


if __name__ == '__main__':
    unittest.main()
