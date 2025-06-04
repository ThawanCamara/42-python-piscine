from sys import argv

def assert_error(msg: str) -> None:
	print("Assertion Error:", msg)
	exit(1)

def check_argv(argv: list[str]) -> None:
	if len(argv) > 2:
		assert_error("more than one argument is provided")
	try:
		if len(argv) > 1:
			l = int(argv[1])
	except:
		assert_error("argument is not an integer")

check_argv(argv)
if int(argv[1]) % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")