#!/usr/bin/eval PYTHONPATH=/home/lma21/python-modules/ python
# -*- coding: utf-8 -*-

#python import
import twitter 
import time
import sys

#local import
import bitly
from grabber import get_last_post

API = twitter.Api(consumer_key='XXX',
                  consumer_secret='XXX',
                  access_token_key='XXX',
                  access_token_secret='XXX')

BAPI= bitly.Api(login='XXX',
		apikey='XXX')

def compose_message(post):
	'''
	compose bot tweet
	'''
	url = shorten_url(post.get('url'))
	message="%s [%s] - %s: %s" % (post.get('title'), post.get('points'), post.get('postedAgo'), url)
	return message

def post_message(message, title):
	'''
	post tweet if length is correct
	'''
	if len(message) > 141:
		print("Message is too long...")
		return False
	else:
		API.PostUpdate(message)
		print("Message with title %s and length: %d posted." % (title, len(message)))
		return True

def shorten_url(url):
	'''
	shorten url using bit.ly's api
	'''
	short_url = BAPI.shorten(url)
	return short_url

def main():
	'''
	Main program 
	'''
	post_count=0
	current = get_last_post()
	if current == None:
		print("Error getting last post...")
		sys.exit(1)
	message = compose_message(current)
        result = post_message(message, current.get('title'))
	while True:
		last_post = get_last_post()
		if last_post == None:
			time.sleep(60)
			continue
		if last_post.get('id') == current.get('id'):
			time.sleep(60)
			continue
		current = last_post
		message = compose_message(last_post)
		result = post_message(message, last_post.get('title'))
		if result:
			post_count+=1

if __name__=='__main__':
	main()

