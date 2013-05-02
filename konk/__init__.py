#!/usr/bin/env python3.3

# konkretno parser

import re, os, ast

try:
	import simplejson as json
except ImportError:
	import json

class BadInputException(TypeError):
	
	def __str__(self):
		return 'Input must be str or buffer'

class Konk:
	
	def __init__(self, konkcode):
		
		if hasattr(konkcode, 'read'):
			self._konkcode = konkcode.read()
		elif type(konkcode) is str:
			self._konkcode = konkcode
		else:
			raise BadInputException

		
		root_path = os.path.dirname(os.path.realpath(__file__))
		
		syntax = json.load(open(os.path.join(root_path, 'syntax.json')))
		
		self.syntax = {}
		
		for category in syntax:
			for key in syntax[category]:
				self.syntax[key] = syntax[category][key]

	
	def parse(self):
		'''Returns konkcode translated into Python WITHOUT any konk imports, which may not yield executable code.
		Use the process method to generate executabke python code'''
		
		konkcode = self._konkcode
		
		sorted_tokens = sorted(self.syntax.keys(), key=len, reverse=True)
		
		for token in sorted_tokens:
			konkcode = re.sub(r'(?<=[\s\(\)@]){token}(?=[\s\(\):])|^{token}(?=[\s\(\):])'.format(token=token), self.syntax[token], konkcode, flags=re.MULTILINE)
		
		return konkcode
	
	def process(self):
		'''Processes konkcode and returns something which should be executable in Python'''
		
		pythoncode = self.parse()
		
		# this'll do for now, will be rewritten with something a tad more intelligent later
		processed_code = 'from konk.stdlib import *\n\n' + pythoncode
		
		return processed_code
