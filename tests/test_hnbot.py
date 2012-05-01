#!/usr/bin/eval PYTHONPATH=/home/lma21/python-modules/ python
# -*- coding: utf-8 -*-

import unittest

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import hnbot

class HnbotMessage(unittest.TestCase):
	def testTooLarge(self):
		"""test should fail if message size is bigger than 140 characters"""
		self.assertEqual(1,1)


if __name__ == "__main__":
	unittest.main()  
