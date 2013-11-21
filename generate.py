#!/usr/bin/env python2.7.3
# -*- coding: UTF-8 -*-
"""
Author: Ethan Joachim Eldridge
Website: ejehardenberg.github.io
Contact me through my github.

Generates a bunch of data for _data.json to show performance degradation
"""

import json
import string
import random

def gen_string(size=160, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + ' '):
	return ''.join(random.choice(chars) for x in range(size))

def make_paragraphs(num=3):
	return '\r\n'.join(gen_string() for x in range(num))

def make_keys(num=5):
	return '::'.join(gen_string(size=10) for x in range(num)).split('::')


def make_obj():
	obj = {}
	keys = make_keys(random.choice([4,6,8]))
	for key in keys:
		obj[key] = make_paragraphs(random.choice([3,8,4,6,1]))
	return obj

def create_list(num=50000):
	objList = {}
	for i in range(num):
		objList[gen_string(chars=string.ascii_uppercase)] = (make_obj())
	return objList
	
def make__data():
	f = open('_data.json','w')
	f.write(json.dumps(create_list(), indent=4, sort_keys=True))
	f.close()

if __name__ == "__main__":
	make__data()