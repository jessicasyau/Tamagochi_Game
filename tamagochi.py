import random

class Pet:
    """A text-based tamagochi digital pet"""
    
    #Class variables
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['mama']

    #constructor function to initialize the pet's name, assign random integers
    #for hunger and boredome, and assign sounds to the sounds list
    def __init__(self, name):
        self.name = name
        self.hunger = random.randrange(0, self.hunger_threshold)
        self.boredom = random.randrange(0,self.boredom_threshold)
        self.sounds = self.sounds
    
    #simulates time passing, so hunger and boredom are both increased
    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    #defines the mood of the pet based on its stats
    def mood(self):
        if self.hunger <=self.hunger_threshold and self.boredom <=self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    #default print statement that shows the pet's name, mood, and stats
    def __str__(self):
        return "I'm {name}, and I feel {mood}. \nHunger: {hunger} | Boredom: {boredom} | Sounds: {sounds}".format(name=self.name, mood = self.mood(), hunger=self.hunger, boredom=self.boredom, sounds=self.sounds)

    #teach the pet a new sound and reduce boredom
    def teach(self, word):
        if word in self.sounds:
            print("I already know that sound")
        else:
            self.sounds.append(word)
            self.boredom = max(0, self.boredom - self.boredom_decrement)

    #interact with the pet to reduce boredom
    def hi(self):
        print(self.sounds[random.randrange(0,len(self.sounds))])
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    #feed the pet to reduce hunger
    def feed(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

"""Game Interface"""
import sys
sys.setrecursionlimit(60000)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()



play()
