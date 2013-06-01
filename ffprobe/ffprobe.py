#!/usr/bin/python
# Filename: ffprobe.py

version='0.1'

import subprocess
import re
import sys
import os

class FFProbe:
	def __init__(self,video_file):
		self.video_file=video_file
		p = subprocess.check_output(["ffprobe","-show_streams",self.video_file],stderr=subprocess.PIPE,shell=True)
		self.format=None
		self.created=None
		self.duration=None
		self.start=None
		self.bitrate=None
		self.streams=[]
		self.video=[]
		self.audio=[]
		datalines=[]
		for a in str(p.decode(sys.stdout.encoding)).split('\n'):
			if re.match('\[STREAM\]',a):
				datalines=[]
			elif re.match('\[\/STREAM\]',a):
				self.streams.append(FFStream(datalines))
				datalines=[]
			else:
				datalines.append(a)
		for a in self.streams:
			if a.isAudio():
				self.audio.append(a)
			if a.isVideo():
				self.video.append(a)
class FFStream:
	def __init__(self,datalines):
		for a in datalines:
			(key,val)=a.strip().split('=')
			self.__dict__[key]=val
	def isAudio(self):
		val=False
		if self.__dict__['codec_type']:
			if str(self.__dict__['codec_type']) == 'audio':
				val=True
		return val
	def isVideo(self):
		val=False
		if self.__dict__['codec_type']:
			if self.codec_type == 'video':
				val=True
		return val
	def isSubtitle(self):
		val=False
		if self.__dict__['codec_type']:
			if str(self.codec_type)=='subtitle':
				val=True
		return val
	def frameSize(self):
		size=(0,0)
		if self.isVideo():
			if self.__dict__['width'] and self.__dict__['height']:
				size=(int(self.__dict__['width']),int(self.__dict__['height']))
		return size
	def pixelFormat(self):
		f=None
		if self.isVideo():
			if self.__dict__['pix_fmt']:
				f=self.__dict__['pix_fmt']
		return f
	def frames(self):
		f=0
		if self.isVideo() or self.isAudio():
			if self.__dict__['nb_frames']:
				f=int(self.__dict__['nb_frames'])
		return f
	def durationSeconds(self):
		f=0.0
		if self.isVideo() or self.isAudio():
			if self.__dict__['duration']:
				f=float(self.__dict__['duration'])
		return f		
	def language(self):
		lang=None
		if self.__dict__['TAG:language']:
			lang=self.__dict__['TAG:language']
		return lang
		
class VideoStream:
	def __init__(self,probe_line):
		pass
class AudioStream:
	def __init__(self,probe_line):
		pass
			
if __name__ == '__main__':
	print "Module ffprobe"
