
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ThursdayDungeon 

import sys, re, json 
import cStringIO 
import gzip, zlib 

def response(context, flow): 
	gfile = gzip.GzipFile(fileobj=cStringIO.StringIO(flow.response.content)) 
	if 'sneak_dungeon&' in flow.request.path: 
		data = json.loads(gfile.read()) 
		if data['res'] == 0: 
			dung = re.search('&dung=([0-9]+)&', flow.request.path) 
			floor = re.search('&floor=([0-9]+)&', flow.request.path) 
			print "Length"
			print "Length of the string: ", len(data['e']);
			print "!!"
			
			if dung.group(1) == '309':
				if len(data['e']) == 313:
					content = '{"res":99}' 
					print "Dungeon is ",dung.group(1);
					print "Length"
					print "Length of the string: ", len(data['e']);
					print "!!"
					s = cStringIO.StringIO() 
					gf = gzip.GzipFile(fileobj=s, mode='wb') 
					gf.write(content) 
					gf.close() 
					flow.response.content = s.getvalue() 
