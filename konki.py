#!/usr/bin/env python3.3

from konk import Konk
from code import InteractiveConsole

class KonkInteractiveConsole(InteractiveConsole):

	def push(self, line):
		line = Konk(line).parse()
		super().push(line)

def main():
	konki = KonkInteractiveConsole()
	# dirty, very dirty
	konki.push('from konk.stdlib import *')
	konki.interact('Конкретно Интерактивная Консоль v 0.11')

if __name__ == '__main__':
	main()