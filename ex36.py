from sys import exit

def dead(why):
	print why, "Good job!"
	exit(0)

def lion_room():
	print "You find a lion in the middle of a giant room."
	print "The lion stares at you. You think it'll probably start run to you soon."
	print "You only hava an apple and a knife. What do you do?"

	next = raw_input("> ")

	if "apple" in next:
		dead("Lions don't like apples. The lion ignores the apple and eats you while you're still alive.")
	elif "knife" in next:
		dead("Good try but the lion is stronger than you and it kills you easily.")
	elif "run away" in next:
		choose_door()
	else:
		dead("Please, learn to write good English. Now your ignorance will kill you because the lion catchs you and eats you while you are thinking how to write well.")


def choose_door():
	print "There are two options:"
	print "On the left, there's a wooden door."
	print "On the right, there's an abyss."
	print "What do you want to do? Hurry up, the lion is coming!"

	next = raw_input("> ")

	if "left" in next:
		print "You go to another dimension"
	if "right" in next:
		dead("You fall into the bottomless abyss. After a thousand years falling you die by boredom.")


def start():
	lion_room()

start()