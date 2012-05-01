#!/usr/bin/eval PYTHONPATH=/home/lma21/python-modules/ python
# -*- coding: utf-8 -*-

import sys
from utils import grabber 

def update_file(post):
	print "Updating handler with id:%d" % (post.get('id'))
	with open('.lastpost', 'w') as f:
		f.write(str(post.get('id')))

def get_post():
	with open('.lastpost', 'r') as f:
                postid = f.readline()
	return postid

def main():
        '''
        Main program
        '''
        post = grabber.get_last_post()
        if post == None:
                print("Error getting last post...")
                sys.exit(1)
	update_file(post)

if __name__=='__main__':
        main()

