from decorators import two_second_sleep
from timeout_decorator import timeout

@two_second_sleep
@timeout(1)
def test():
	print("Testing 2 decorators")
