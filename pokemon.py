"""
Terminal Game
"""
import atexit
import json
import numpy as np
import sys
import time

def printf(s):
	#Print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

def y_or_n(choice):
	if choice.lower().strip() == "y" or "yes":
		return True
	else:
		return False

def exit_handler():
  # exit handler so that user doesnt abruptly exit the game (we can add a function that saved user's progress here)
  print('My application is ending!')

atexit.register(exit_handler)

def game_save(Trainer):
  # to be completed
  with open("savefile.txt", "w") as save:
    save.write()




#-------------------------------------------------------


class Trainer:
  def __init__(self, name: str, money: int, pokemon: dict, location: str):
    self.name = name
    self.money = money
    self.pokemon = pokemon
    self.location = location

  def current_location(self):
    return f"You are currently in {self.location}"

  def __str__(self):
    return f"Pkmn Trainer {self.name}'s Trainer Card'\nStats:\nPokemon: {self.pokemon}\nMoney: {self.money}"

  def CapturePokemon(self):
    global capture
    capture=True

class PokemonFather:
  def __init__(self,names, types, moves,EVs,health="========================"):
    self.name=name
    self.moves=moves
    self.attack=EVs["ATTACK"]
    self.defense=EVs["DEFENSE"]
    self.bars=20 #Amount of health bars

  def fight(self, pokemon2):
    #This allow 2 pokemons fight each other
    #Print fight information
    print("-------POKEMON BATTLE-------")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK/", self.attack)
    print("DEFENSE/", self.defense)
    print("LVL/", 3*(1+np.mean([self.attack, self.defense])))
    print("\nVS")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK/", Pokemon2.attack)
    print("DEFENSE/", Pokemon2.defense)
    print("LVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))
    print("\nVS")

    time.sleep(2)

    #Consider type advantages
    version=["Fire", "Water", "Grass"]
    for i,k in enumerate(version):
      if self.type == k:
        #Both are the same type
        if Pokemon2.type == k:
          string_1_attack = "It's not very effective..."
          string_2_attack = "It's not very effective..."
        #Pokemon2 is STRONG against pokemon1
        if Pokemon2.types == version[(i+1)%3]:
          Pokemon.attack *= 2
          Pokemon2.defense *= 2
          self.attack /= 2
          self.defense /= 2
          string_1_attack= "It's not very effective..."
          string_2_attack= "It's very effective!"
        #Pokemon 2 is WEAK against Pokemon 1
        if Pokemon2.types == version[(i+2)%3]:
            self.attack*=2
            self.defense*=2
            Pokemon2.attack/=2
            Pokemon2.defense/=2
            string_1_attack="It's very effective!"
            string_2_attack="It's not very effective..."
    while (self.bars>0) and (Pokemon2>0):
        #Print the health of each pokemon
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

        print(f"Go {self.name}!")
        for i,x in enumerate(self.moves):
            print("f{i+1}.", x)
        index=int(input("Pick a move: "))
        printf(f"{self.name} used {moves[index-1]}!")
        time.sleep(1)
        printf(string_1_attack)

        #Determine damage
        Pokemon2.bars-= self.attack
        Pokemon2.health=""

        #Add back bars plus give a defense boost
        for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
            Pokemon2.health+="="
        time.sleep(1)
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
        time.sleep(.5)

        #Check if the pokemon has fainted
        if Pokemon2.bars<=0:
            printf("\n...", Pokemon2.name + " fainted")
            break
#----------------------------------If Pokemon2's hasn't fainted, then it's Pokemon2's turn-------------------------
        print(f"Go {Pokemon2.name}!")
        for i,x in enumerate(Pokemon2.moves):
            print("f{i+1}.", x)
        index=int(input("Pick a move: "))
        printf(f"{Pokemon2.name} used {moves[index-1]}!")
        time.sleep(1)
        printf(string_2_attack)

        #Determine damage
        self.bars-= Pokemon2.attack
        self.health=""

        #Add back bars plus give a defense boost
        for j in range(int(self.bars+.1*self.defense)):
            Pokemon2.health+="="
        time.sleep(1)
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
        time.sleep(.5)

        #Check if the pokemon has fainted
        if self.bars<=0:
            printf("\n...", self.name + " fainted")
            break
    money=np.random.choice(5000)
    printf(f"Opponent paid you {money}.")



  def PokemonState(self):
    print("Your pokemon has: ", self.hp, "\nYour pokemon has: ", self.exp, "\nYour pokemon has: ", self.speed, "speed", "\nYour pokemon has: ", self.attack, "attack", "\nYour pokemon has: ", self.defense, "defense")


#-----------------------------------------------------------------------------------------------------------

#----------Story-----------
printf(
  "???: Hello there! Welcome to the world of POKEMON! My name is OAK!"
  "\nOAK: People call me the POKEMON PROF!"
  "\nOAK: This world is inhabited by creatures called POKEMON! For some people, POKEMON are pets. Others use them for fights. Myself...\nI study POKEMON as a profession."
  "\nOAK: First, what is your name?"
)
player = Trainer(input("\nEnter your name:\t"),0,{},"Pallet Town")

choice = input(f"Right! So your name is {player.name}![Y/n]\t")
if not y_or_n(choice):
	player.name = input("Enter your name:\t")
	printf(f"Right so your name is {player.name}!")

printf(
	"""OAK: This is my grandson. He's been your rival since you were a baby.
	...Erm, what is his name again?"""
)

rival = Trainer(input("\nEnter your rival's name:\t"),0,{},player.location)
choice = input(f"That's right! I remember now! His name is {player.name}![Y/n]\t")

if not y_or_n(choice):
	rival.name = input("Enter your rival's name:\t")
	printf(f"That's right! I remember now! His name is {player.name}!")

printf("OAK: Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!")

printf("Scene: You are in your bedroom now. You go downstairs to find your mother watching a program on T.V.")
choice = input("Do you talk to her?[y/n]\t")

if y_or_n(choice):
	printf(
	"""Mother: Right. All boys leave home some day. It said so on TV.
	PROF.OAK, next door, is looking for you."""
	)
else:
	printf("Your mother calls your name.\nMother: PROF.OAK, next door, is looking for you.")

printf(
"""You step outside the house and see explore your hometown.
You look at the boundless blue sky above you, while the sweet scent of oddish in the forests reminds you of the amazing journey you're about to embark on!
'There's no place like Pallet Town', you say as you run towards Prof. Oak's Lab"""
)
