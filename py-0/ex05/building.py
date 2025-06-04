from sys import argv

def assert_error(msg: str) -> None:
	print("Assertion Error:", msg)
	exit(1)

def check_argv(argv: list[str]) -> None:
	size = len(argv)
	if size > 2:
		assert_error("more than one argument is provided")

def print_bank(bank: dict) -> None:
	print(f"The text contains {bank["total"]} characters:")
	for key, value in bank.items():
		if key != "total":
			print(f"{value} {key}")

def main() -> None:
	mystr = ""
	bank = {
		"total": 0,
		"upper letters": 0,
		"lower letters": 0,
		"punctuation marks": 0,
		"spaces": 0,
		"digits": 0,
	}

	check_argv(argv)

	if len(argv) == 1:
		while mystr == "":
			mystr = input("What is the text to count?\n")
	else:
		mystr = argv[1]
	
	bank["total"] = len(mystr)
	for ch in mystr:
		bank["upper letters"] += ch.isupper()
		bank["lower letters"] += ch.islower()
		bank["punctuation marks"] += ch.isprintable() and not ch.isspace() and not ch.isalnum()
		bank["spaces"] += ch.isspace()
		bank["digits"] += ch.isnumeric()
	
	print_bank(bank)

if __name__ == "__main__":
	main()
