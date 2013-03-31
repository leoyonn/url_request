# -*- coding: utf-8 -*-
#!/usr/bin/python
# author: leo
# data: 2012-09-25

import urllib, urllib2, sys, os, simplejson

# base url, rsz should less than 8.
RSZ = 8
BASE_URL = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&rsz=" + str(RSZ)\
			+ '&imgsz=small|medium|large|xlarge|xxlarge|huge'

IMG_URLS_FILE = None
IMG_PATH = "."

# parse image list from google-image
def parse_image_list(results):
	if not results.has_key('responseData') or not results['responseData'].has_key('results'):
		return 0
	count = 0
	for r in results['responseData']['results']:
		img = '\t'.join([r['url'], r['width'] + 'x' + r['height'],
					 r['titleNoFormatting'], r['contentNoFormatting']])
		IMG_URLS_FILE.write(img + '\n')
		print '  | got ' + img
		count += 1
	IMG_URLS_FILE.flush()
	return count

# get query from google. num round up to RSZ's multiple
def get_images_list(query, num):
	print '>> getting [' + query + '](count: ' + str(num) + ')...',
	start = 0
	while start < num:
		url = BASE_URL + '&q=' + urllib.quote(query) + "&start=" + str(start)
		request = urllib2.Request(url, None, {'Referer': 'http://fanfan.youdao.com'})
		response = urllib2.urlopen(request)
		results = simplejson.load(response)
		if parse_image_list(results) < RSZ:
			print 'no more results for [' + query + ']...'
			break;
		start = start + RSZ
		print '|got [' + str(start) + ']...'

#get_images_list("毛血旺", 10)

USAGE = '>> usage: gicrawler <dish-list-file> <count-to-get> <image-save-path>'

def main():
	print USAGE
	if len(sys.argv) != 4:
		return
	dish_list_file = sys.argv[1]
	count = int(sys.argv[2])
	global IMG_URLS_FILE
	IMG_URLS_FILE = open(sys.argv[3] + "/image_urls.list", 'w')
	if not os.path.isfile(dish_list_file):
		print 'file not exists... ' + USAGE
		return
	dish_list = open(dish_list_file).readlines()
	for dish in dish_list:
		get_images_list(dish, count)

main()
