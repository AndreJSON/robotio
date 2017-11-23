'''
The generators I have here are shit,
but I didn't need anything better when I made this.
'''
import random

generators = []

def usernameGenerator():
	username = ""
	username += random.choice(alphabet)
	username += random.choice(alphabet)
	username += random.choice(alphabet)
	username += random.choice(listOfNames)
	username += random.choice(alphabet)
	return username

def emailGenerator():
	email = ""
	email += random.choice(listOfNames)
	email += "."
	email += random.choice(listOfWords)
	email += "@yahoo.com"
	return email

def fullNameGenerator():
	name = ""
	name += random.choice(listOfNames)
	name += " "
	name += random.choice(listOfLastnames)
	return name

def passwordGenerator():
	return "Secure123"

alphabet = "abcdefghijklmnopqrstuvwxyz"

listOfNames = [
	"adam", "john", "joe", "lisa", "dan", "dave", "douglas", "hubert", "jill"
	"abdallah", "allan", "ariko", "hassan", "aida", "elsa", "norton", "khan",
	"woody", "kimberly", "liam", "kourtney", "melinda", "max", "maxine", "bob"
]

listOfLastnames = [
	"kaspersky", "jensen", "khan", "muhammad", "talil", "thalia", "ghorak",
	"jibani", "popovic", "hendersen", "juhan", "jikar", "dawlat", "islam",
	"richer", "goldstein", "deutern", "goldglocken", "fassbender", "doe"
]

listOfWords = [
	"cat", "dog", "man", "horse", "dj", "pro", "wow", "pokemon", "swag", "cool",
	"dude", "pen", "seattle", "disney", "orlando", "island", "vacation", "ham",
	"966", "2001", "1984", "777", "871", "666", "888", "police", "fire", "hot"
]

generators.append(usernameGenerator)
generators.append(fullNameGenerator)
generators.append(emailGenerator)
generators.append(passwordGenerator)
generators.append(lambda: "ston")