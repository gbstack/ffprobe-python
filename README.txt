=======
FFProbe
=======
A wrapper around the ffprobe command to extract metadata from media files.

Usage::

    #!/usr/bin/env python
    
    from ffprobe3 import FFProbe
    
    metadata=FFProbe('test-media-file.mov')
    
    for stream in metadata.streams:
        if stream.is_video():
            print('Stream contains {} frames.'.format(stream.frames()))
