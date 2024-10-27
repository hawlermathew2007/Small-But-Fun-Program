# input, 1, 2, 4, 4
import pyttsx3

engine = pyttsx3.init()
def drawcow(pos, symbol):
	cow = {"ear": "{}   ^__^".format(symbol),
		"eyes": "{}  (OO)\\_________".format(symbol, symbol),
		"mouth": "(__)\\         )\\/\\",
		"milk": "| |----W  |",
		"legs": "| |     | |"}

	spaces = [""," ","    ","        ","        "]
	ispace = "  "
	for i in range(pos):
		ispace += " "

	i = 0
	for key, value in cow.items():
		print(ispace + spaces[i] + value)
		i += 1

	engine.say(general)
	engine.runAndWait()

ask = input("cowthink or cowsay?:")

if "cowsay" in ask:
	general = input("cowsay: ")
	thing1,thing2 = "<", ">"
	symp = "\\"
else:
	general = input("cowthink: ")
	thing1,thing2 = "(", ")"
	symp = "O"

ftext = " __"
ltext = " --"
for i in range(len(general)):
	ftext += "_"
	ltext += "-"

print(ftext)
print(f"{thing1} {general} {thing2}")
print(ltext)

drawcow(int(len(general)/2), f"{symp}")