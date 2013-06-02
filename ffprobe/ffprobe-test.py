#!/usr/bin/python

from ffprobe import FFProbe

m=FFProbe("../structured_data/EDLs/0001T_pull/0001T_PULL.mov")
for s in m.streams:
	if s.isVideo():
		framerate=s.frames()/s.durationSeconds()
		print framerate
		print s.frameSize()
	print s.durationSeconds()
	print s.frames()
	print s.isVideo()