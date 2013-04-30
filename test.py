#!/usr/bin/env python3.3

from konk import KonkParser
from konk.stdlib import *
import sys

def main():
	try:
		code = open(sys.argv[1])
	except:
		code = open('test.konk')

	parser = KonkParser()
	code = parser.parse(code)

	try:
		output = exec(code)
	except SyntaxError as e:
		lines = code.split('\n')
		for n, line in enumerate(lines):
			print('{}	{}'.format((n + 1), line))
			
		print('failed: {}'.format(e))
	except NameError as e:
		codefile = open('testoutput.py', 'w')
		codefile.write(code)
		codefile.close()
		code = open('testoutput.py').read()
		exec(code)
		os.unlink(os.path.join(os.path.dirname(os.path.realpath(__file__)), codefile.name))
	else:
		print('passed')

if __name__ == '__main__':
	main()
