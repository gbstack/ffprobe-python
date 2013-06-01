=======
FFProbe
=======
A wrapper around the ffprobe command to extract metadata from media files.

Usage::

    #!/usr/bin/env python
    
    from ffprobe import FFProbe
    
    metadata=FFProbe("test-media-file.mov")
    
    for stream in metadata.streams:
    	if stream.isVideo():
    		print "Stream contains "+stream.frames()+" frames."
			
