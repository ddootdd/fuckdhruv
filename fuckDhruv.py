import random
import math


# ToDo: Grammar lolz
# meme generator
def fuckDhruv():
  adjectives = ["fucking", "goddamn", "lameass", "motherfucking", "uncoordinated", "weak", "smelly", "fecal", "ass-licking", "slimy", "useless", "contaminated", "irrelevant", "biohazardous", "cancerous", "herpetic", "spineless", "fascist", "diseased", "infected", "contagious", "disease-causing", "donkey-fucking"]
  nouns = ["fuccboi", "asshat", "shitstick", "asshole", "chode", "loser", "lameboi", "chodesicle", "bloodclot", "feces", "chode-muncher", "chode-rooster", "fuckbucket", "dickshaft", "cum guzzler", "ball fondler", "piss drinker", "herpes", "ostrich", "Republican", "bacteria", "donkey-fucker"]
  name = str(raw_input('What is your name?'))

  if name == 'Dhruv' or name == 'dhruv':
    for i in range(1,15):
      print "fuck Dhruv, he is a " + adjectives[int(random.uniform(0, len(adjectives)))] + " " + nouns[int(random.uniform(0, len(nouns)))]
  else:
    print "Hi " + name + "! You look wonderful today."
fuckDhruv()
