import time

def two_second_sleep(func):
	func()
	time.sleep(10)
	
