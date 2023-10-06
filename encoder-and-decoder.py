import colorama

print("1. Encode")
print("2. Decode")

def decode():
	phrase = input("Text to decode >>> ")
	phrase = phrase.replace("\\","0")
	tmplist = []
	for item in phrase.split("0"):
		if item:
			tmplist.append("0" + item)
	for i in range(len(tmplist)):
		print(chr(int(tmplist[i], 16)), end="")

def encode():
	phrase  = input("Text to encode >>> ")
	for i in range(len(phrase)):
		ascii = (int(ord(phrase[i])))
		hhex = hex(ascii)
		byte = hhex.replace("0","\\")
		print(byte, end="")

while True:
	userinput = input("\nConsole >>> ")
	try:
		if userinput == "1":
			encode()
		elif userinput == "2":
			decode()
		elif userinput == "exit":
			exit()
		else:
			print(colorama.Fore.WHITE + colorama.Back.RED + "Command Not valid" + colorama.Style.RESET_ALL)
	except:
		print(colorama.Fore.WHITE + colorama.Back.RED + "Something went wrong" + colorama.Style.RESET_ALL)
