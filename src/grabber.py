import requests
import simplejson

import datetime

def get_url():
	'''
	retrieves all posts from news.ycombinator.com in json format
	'''
	url='http://api.ihackernews.com/page'
	r = requests.get(url)
	print "Status: %d, %s" % (r.status_code, str(datetime.datetime.now()))
	return r.status_code, r.content

def parse_json(content):
	'''
	parse json data
	return dict to all posts
	'''
	result = simplejson.loads(content)
	return result['items']

def get_last_post():
	'''
	returns last post on news.ycombinator.com
	'''
	status, content = get_url()
	if status == 200: 
		posts=parse_json(content)
		return posts[0]
	return None


