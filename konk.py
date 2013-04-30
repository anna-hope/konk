#!/usr/bin/env python3.3

# konkretno parser

import re, os, sys, pprint

try:
	import simplejson as json
except ImportError:
	import json

class KonkParser:

	def __init__(self):
		root_path = os.path.dirname(os.path.realpath(__file__))

		syntax = json.load(open(os.path.join(root_path, 'syntax.json')))

		self.syntax = {}

		for category in syntax:
			for key in syntax[category]:
				self.syntax[key] = syntax[category][key]

	def parse(self, konkcode):
		'Parser'
		assert type(konkcode) is str, 'konkcode must be str'

		sorted_keywords = sorted(self.syntax.keys(), key=len, reverse=True)

		for keyword in sorted_keywords:
			konkcode = re.sub(r'(?<=[\s\(\)]){}(?=[\s\(\):])|^{}(?=[\s\(\):])'.format(keyword, keyword), self.syntax[keyword], konkcode, flags=re.MULTILINE)

		pythoncode = konkcode

		return pythoncode

class stdfuncs():
	pass