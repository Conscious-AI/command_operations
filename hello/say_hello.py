import random as rand
from utils import TTS

l1 = ["Hello.", "Hi.", "Hey!", "Hi there!", "Hey there!", "Yo!", "Howdy!"]
l2 = ["", "How are you?", "How it's going?", "What's going on?", "How have you been?", "What's up?", "Sup?"]
l3 = ["", "Nice to hear you again!", "Good to hear you again!"]

# Can be implemented later
# l4 = ["", "It's been a while!", "Long time no see!"]

def main():
    tts = TTS()
    choice1 = rand.choice(l1)
    choice2 = rand.choice(l2)
    choice3 = rand.choice(l3)
    tts.speak(f"{choice1} {choice2} {choice3}")