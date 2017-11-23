import time
import json
import sys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from generators import generators

def main():
	global generators
	m = PyMouse()
	k = PyKeyboard()
	actions = json.load(open("actions.json"))
	while True:
		for a in actions:
			if a["action"] == "sleep":
				time.sleep(a["duration"])
			elif a["action"] == "click":
				m.click(a["position"][0], a["position"][1], 1)
			elif a["action"] == "write":
				s = generators[a["generator"]]()
				for c in s:
					if c == "@":  # Work around for fault in library.
						k.press_key(k.altgr_key)
						k.tap_key("2")
						k.release_key(k.altgr_key)
					else:
						k.tap_key(c)
			else:
				raise Exception("Unexpected action.")
		if len(sys.argv) < 2:
			break

if __name__ == "__main__":
	main()
