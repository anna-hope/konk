#!/usr/bin/env python3.3

from konk import Konk

import sys

def main():
	try:
		konkfile = open(sys.argv[1])
	except:
		konkfile = open('test.konk')

	konk = Konk(konkfile)
	pythoncode = konk.process()

	try:
		compiled = compile(pythoncode, '<string>', 'exec')
	except (SyntaxError, TypeError) as e:
		lines = pythoncode.split('\n')

		for n, line in enumerate(lines):
			print('{}	{}'.format((n + 1), line))

		print('failed: {}'.format(e))
	else:
		print('passed')

if __name__ == '__main__':
	main()
