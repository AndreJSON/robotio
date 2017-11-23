import time
import json
import keyboard as k
from pymouse import PyMouse

prevTime = time.time()

def main():
	actions = []
	genCount = 0
	m = PyMouse()
	while True:
		if k.is_pressed('q'):
			actions.append(createSleepAction())
			actions.append(createClickAction(m.position()))
		elif k.is_pressed('w'):
			actions.append(createSleepAction())
			actions.append(createWriteAction(genCount))
			genCount += 1
		elif k.is_pressed('e'):
			f = open("actions.json", "w")
			f.write(json.dumps(actions, indent=3))
			f.close()
			break
		else:
			time.sleep(0.01)

def createClickAction(position):
	return {'action':'click', 'position': position}

def createWriteAction(genCount):
	return {'action':'write', 'generator': genCount}

def createSleepAction():
	global prevTime
	action = {'action':'sleep', 'duration': time.time() - prevTime}
	prevTime = time.time()
	time.sleep(0.4)
	return action

if __name__ == "__main__":
	main()
