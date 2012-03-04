#!/usr/bin/eval PYTHONPATH=/home/lma21/python-modules/ python
# -*- coding: utf-8 -*-

#python import
import twitter 
import time
import sys
from xml.etree import ElementTree

#local import
import bitly
from grabber import get_last_post

doc = ElementTree.parse('twitter-auth.xml')
try:
        c_key = doc.find('ConsumerKey').text
        c_secret = doc.find('ConsumerSecret').text
        a_key = doc.find('AccessKey').text
        a_secret = doc.find('AccessSecret').text
except:
        print "Error in XML file: twitter-auth.xml. Tag not found"

API = twitter.Api(consumer_key=c_key,
                  consumer_secret=c_secret,
                  access_token_key=a_key,
                  access_token_secret=a_secret)

doc = ElementTree.parse('bitly-auth.xml')
try:
        login= doc.find('Login').text
        apikey= doc.find('Apikey').text
except:
        print "Error in XML file bitly-auth.xml. Tag not found"

BAPI= bitly.Api(login=login,
		apikey=apikey)

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
	print "Message to post: %s" % (message)
	print ""
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
	print "Shortening URL: %s" % (url)
	short_url = BAPI.shorten(url)
	return short_url

def update_file_post(post):
        with open('.lastpost', 'w') as f:
                f.write(str(post.get('id')))

def get_file_post():
        with open('.lastpost', 'r') as f:
                postid = f.readline()
        return postid

def main():
	'''
	Main program 
	'''
	post_count=0
	while True:
		try:
			current_post_id = int(get_file_post())
		except ValueError:
			print "Error in .lastpost"
			sys.exit(1)
		last_post = get_last_post()
		if last_post == None:
			time.sleep(60)
			continue
		if last_post.get('id') == current_post_id:
			time.sleep(60)
			continue
		print "Compared current post with id: %d to previous id: %d. Posting message."  % (current_post_id, last_post.get('id'))
		message = compose_message(last_post)
		result = post_message(message, last_post.get('title'))
		update_file_post(last_post)
		if result:
			print "Posted successfully!"

if __name__=='__main__':
	main()

