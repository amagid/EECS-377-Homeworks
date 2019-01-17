import pigpio
from itertools import chain
from time import sleep

G = 13
R = 19
B = 26

def loop(pi):
	resetLEDs(pi)
	sleep(1)
	for pin in [R, G, B]:
		flashLED(pi, pin)

	for x in chain(range(0, 255), reversed(range(0, 254))):
		pi.set_PWM_dutycycle(R, x)
		pi.set_PWM_dutycycle(G, x)
		pi.set_PWM_dutycycle(B, x)
		sleep(0.5 / 256)

	loop(pi)


def resetLEDs(pi):
	pi.write(R, 0)
	pi.write(G, 0)
	pi.write(B, 0)
	pi.set_PWM_dutycycle(R, 0)
	pi.set_PWM_dutycycle(G, 0)
	pi.set_PWM_dutycycle(B, 0)


def flashLED(pi, pin):
	for x in range(0, 255):
		pi.set_PWM_dutycycle(pin, x)
		sleep(0.5 / 256)
	for x in reversed(range(0, 254)):
		pi.set_PWM_dutycycle(pin, x)
		sleep(0.5 / 256)

pi = pigpio.pi()
loop(pi)
