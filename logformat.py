from functools import wraps


def logformat(fmt):
	def logged(func):
		#Wraps around a function to put logging around it
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(fmt.format(func=func))
			return func(*args, **kwargs)

		return wrapper
	return logged


def logmethods(cls):
	for key, value in list(vars(cls).items()):
		if callable(value):
			#decorates methods if they are callable
			setattr(cls, key, logged(value))
	return cls


logged = logformat('Calling {func.__name__}')  # sets main log message
