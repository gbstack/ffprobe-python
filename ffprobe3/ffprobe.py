"""
Python wrapper for ffprobe command line tool. ffprobe must exist in the path.
"""
import os
import pipes
import platform
import re
import subprocess

from ffprobe3.exceptions import FFProbeError


class FFProbe:
    """
    FFProbe wraps the ffprobe command and pulls the data into an object form::
        metadata=FFProbe('multimedia-file.mov')
    """

    def __init__(self, video_file):
        self.video_file = video_file
        try:
            with open(os.devnull, 'w') as tempf:
                subprocess.check_call(["ffprobe", "-h"], stdout=tempf, stderr=tempf)
        except:
            raise IOError('ffprobe not found.')
        if os.path.isfile(video_file):
            if str(platform.system()) == 'Windows':
                cmd = ["ffprobe", "-show_streams", self.video_file]
            else:
                cmd = ["ffprobe -show_streams " + pipes.quote(self.video_file)]

            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            self.format = None
            self.created = None
            self.duration = None
            self.start = None
            self.bitrate = None
            self.streams = []
            self.video = []
            self.audio = []
            data_lines = []
            for a in iter(p.stdout.readline, b''):
                a = a.decode('UTF-8')
                if re.match(r'\[STREAM\]', a):
                    data_lines = []
                elif re.match(r'\[/STREAM\]', a):
                    self.streams.append(FFStream(data_lines))
                    data_lines = []
                else:
                    data_lines.append(a)
            for a in iter(p.stderr.readline, b''):
                a = a.decode('UTF-8')
                if re.match(r'\[STREAM\]', a):
                    data_lines = []
                elif re.match(r'\[/STREAM\]', a):
                    self.streams.append(FFStream(data_lines))
                    data_lines = []
                else:
                    data_lines.append(a)
            p.stdout.close()
            p.stderr.close()
            for a in self.streams:
                if a.is_audio():
                    self.audio.append(a)
                if a.is_video():
                    self.video.append(a)
        else:
            raise IOError('No such media file ' + video_file)


class FFStream:
    """
    An object representation of an individual stream in a multimedia file.
    """

    def __init__(self, data_lines):
        for a in data_lines:
            (key, val) = a.strip().split('=')
            self.__dict__[key] = val

    def is_audio(self):
        """
        Is this stream labelled as an audio stream?
        """
        val = False
        if self.__dict__['codec_type']:
            if str(self.__dict__['codec_type']) == 'audio':
                val = True
        return val

    def is_video(self):
        """
        Is the stream labelled as a video stream.
        """
        val = False
        if self.__dict__['codec_type']:
            if self.__dict__['codec_type'] == 'video':
                val = True
        return val

    def is_subtitle(self):
        """
        Is the stream labelled as a subtitle stream.
        """
        val = False
        if self.__dict__['codec_type']:
            if self.__dict__['codec_type'] == 'subtitle':
                val = True
        return val

    def frame_size(self):
        """
        Returns the pixel frame size as an integer tuple (width,height) if the stream is a video stream.
        Returns None if it is not a video stream.
        """
        size = None
        if self.is_video():
            width = self.__dict__['width']
            height = self.__dict__['height']
            if width and height:
                try:
                    size = (int(width), int(height))
                except ValueError:
                    raise FFProbeError("None integer size %s:%s" % (width, height))

        return size

    def pixel_format(self):
        """
        Returns a string representing the pixel format of the video stream. e.g. yuv420p.
        Returns none is it is not a video stream.
        """
        f = None
        if self.is_video():
            if self.__dict__['pix_fmt']:
                f = self.__dict__['pix_fmt']
        return f

    def frames(self):
        """
        Returns the length of a video stream in frames. Returns 0 if not a video stream.
        """
        frame_count = 0
        if self.is_video() or self.is_audio():
            if self.__dict__['nb_frames']:
                try:
                    frame_count = int(self.__dict__['nb_frames'])
                except ValueError:
                    raise FFProbeError('None integer frame count')
        return frame_count

    def duration_seconds(self):
        """
        Returns the runtime duration of the video stream as a floating point number of seconds.
        Returns 0.0 if not a video stream.
        """
        duration = 0.0
        if self.is_video() or self.is_audio():
            if self.__dict__['duration']:
                try:
                    duration = float(self.__dict__['duration'])
                except ValueError:
                    raise FFProbeError('None numeric duration')
        return duration

    def language(self):
        """
        Returns language tag of stream. e.g. eng
        """
        lang = None
        if self.__dict__['TAG:language']:
            lang = self.__dict__['TAG:language']
        return lang

    def codec(self):
        """
        Returns a string representation of the stream codec.
        """
        codec_name = None
        if self.__dict__['codec_name']:
            codec_name = self.__dict__['codec_name']
        return codec_name

    def codec_description(self):
        """
        Returns a long representation of the stream codec.
        """
        codec_d = None
        if self.__dict__['codec_long_name']:
            codec_d = self.__dict__['codec_long_name']
        return codec_d

    def codec_tag(self):
        """
        Returns a short representative tag of the stream codec.
        """
        codec_t = None
        if self.__dict__['codec_tag_string']:
            codec_t = self.__dict__['codec_tag_string']
        return codec_t

    def bit_rate(self):
        """
        Returns bit_rate as an integer in bps
        """
        b = 0
        if self.__dict__['bit_rate']:
            try:
                b = int(self.__dict__['bit_rate'])
            except ValueError:
                raise FFProbeError('None integer bit_rate')
        return b
