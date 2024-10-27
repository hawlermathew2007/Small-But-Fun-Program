from dataclasses import dataclass
from textblob import TextBlob

progressing = True

@dataclass
class Mood():
	emoji: str
	sentiment: float

def get_mood(input_text: str, threshold: float):
	sentiment = float(TextBlob(input_text).sentiment.polarity)

	friendlyThreshold = threshold
	hostileThreshold = -threshold

	if sentiment >= friendlyThreshold:
		return Mood('(0 v 0)', sentiment)

	elif sentiment <= friendlyThreshold:
		return Mood('(@ M @)', sentiment)
	
	else:
		return Mood('(0_ 0)', sentiment)


while progressing:
	playerText = input("Text: ")
	if playerText == "end":
		progressing= False
	mood = get_mood(playerText, threshold=0.3)
	print(mood.emoji, mood.sentiment)
