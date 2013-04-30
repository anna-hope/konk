#!/usr/bin/env python3.3

from konk import KonkParser
import sys

def main():
	try:
		code = open(sys.argv[1]).read()
	except:
		code = open('test.konk').read()

	parser = KonkParser()
	code = parser.parse(code)

	try:
		exec(code)
	except SyntaxError as e:
		lines = code.split('\n')
		for n, line in enumerate(lines):
			print('{}	{}'.format((n + 1), line))
			
		print('failed: {}'.format(e))
	except NameError as e:
		print('parsing passed, but the code could not be executed: {}:\n'.format(e))
		print(code)
	else:
		print('passed')

if __name__ == '__main__':
	main()
