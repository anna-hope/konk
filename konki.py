#!/usr/bin/env python3.3

from konk import Konk
from code import InteractiveConsole

class KonkInteractiveConsole(InteractiveConsole):

	def push(self, line):
		pythonline = Konk(line).parse()
		try:
			super().push(pythonline)
		except SyntaxError:
			print("Факап, чувак: {}".format(line))
		except NameError:
			print("О чем ты, бро?")

def main():
	konki = KonkInteractiveConsole()
	# dirty, very dirty
	konki.push('from konk.stdlib import *')
	konki.interact('Конкретно Интерактивная Консоль v 0.11')

if __name__ == '__main__':
	main()