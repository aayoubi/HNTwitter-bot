#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import simplejson

def get_url():
	'''
	retrieves all posts from news.ycombinator.com in json format
	'''
	url='http://api.ihackernews.com/page'
	auth=''
	r = requests.get(url, auth=auth)
	print r.status_code
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
	if status==200: 
		posts=parse_json(content)
		return posts[0]
	return None


