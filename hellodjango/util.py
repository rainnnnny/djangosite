#coding:utf-8

import threading #for: class Timer,


class timer(threading.Timer):

	def clear(self):
		self.function = None
		self.args = None
		self.kwargs = None

class Timer():

	def __init__(self, interval, function, repeats=0, args=None, kwargs=None):
		self.interval = interval
		self.function = function
		self.repeats = repeats + 1
		self.args = args if args is not None else []
		self.kwargs = kwargs if kwargs is not None else {}

		self.oTimer = timer(self.interval, self._func)
		self.oTimer.start()

	def _func(self):
		self.function(*self.args, **self.kwargs)
		self.repeats -= 1

		if self.repeats <= 0:
			self.Stop()
		else:
			self.oTimer = timer(self.interval, self._func)
			self.oTimer.start()

	def Stop(self):
		self.oTimer.cancel()
		self.Clear()

	def StopOnly(self):
		self.oTimer.cancel()

	def Clear(self):
		self.oTimer.clear()
		self.function = None
		self.args = None
		self.kwargs = None
