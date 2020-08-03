import os
import random
from django.core.files import images
from plugin import plugin
from PIL import Image



@plugin("twentyone")
def monkey(jarvis, s):
	blackjackDeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

	def deal(blackjackDeck):
		hand = []
		for i in range(2):
			random.shuffle(blackjackDeck)
			face = blackjackDeck.pop()
			if face == 11:
				 face = "J"
			if face == 12:
				 face = "Q"
			if face == 13:
				 face = "K"
			if face == 14:
				 face = "A"
			hand.append(face)
		return hand

	def startOver():
		again = input("Would you like to play again.  Please Type (Y/N)").lower()
		if again == "y":
			dealerCard = []
			playerHand = []
			blackjackDeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
			game()
		else:
			print("Bye!")
			exit()

	def total(hand):
		total = 0
		for face in hand:
			if face == "J" or face == "Q" or face == "K":
				total += 10
			elif face == "A":
				if total >= 11:
					total += 1
				else:
					total += 11
			else:
				total += face
		return total

	def hit(hand):
		face = blackjackDeck.pop()
		if face == 11:
			 face = "J"
		if face == 12:
			 face = "Q"
		if face == 13:
			 face = "K"
		if face == 14:
			 face = "A"
		hand.append(face)
		return hand

	def clear():
		if os.name == 'nt':
			os.system('CLS')
		if os.name == 'posix':
			os.system('clear')

	def printOutGame(dealerCard, playerHand):
		clear()
		print("The dealer has a " + str(dealerCard) + " for a total of " + str(total(dealerCard)))
		print("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))

	def blackjack(dealerCard, playerHand):
		if total(playerHand) == 21:
			printOutGame(dealerCard, playerHand)
			print("You got a Blackjack!\n")
			startOver()
		elif total(dealerCard) == 21:
			printOutGame(dealerCard, playerHand)
			print("You lost, the dealer has a blackjack\n")
			startOver()

	def score(dealerCard, playerHand):
		if total(playerHand) == 21:
			printOutGame(dealerCard, playerHand)
			print("You got a Blackjack!\n")
		elif total(dealerCard) == 21:
			printOutGame(dealerCard, playerHand)
			print("You lost, the dealer has a blackjack\n\n")
		elif total(playerHand) > 21:
			printOutGame(dealerCard, playerHand)
			print("You busted. You lost.\n")
		elif total(dealerCard) > 21:
			printOutGame(dealerCard, playerHand)
			print("The Dealer Busted! You win!\n")
		elif total(playerHand) < total(dealerCard):
			printOutGame(dealerCard, playerHand)
		elif total(playerHand) > total(dealerCard):
			printOutGame(dealerCard, playerHand)
			print("Your score is the highest you win! You win\n")

	def game():
		choice = 0
		clear()
		print("Hey Welcome to BlackJack!!!\n")
		dealerCard = deal(blackjackDeck)
		playerHand = deal(blackjackDeck)
		while choice != "q":
			print("Dealer has a  " + str(dealerCard[0]))
			print("You have a " + str(playerHand) + " for a score of " + str(total(playerHand)))
			blackjack(dealerCard, playerHand)
			choice = input("Do you want to continue [H] is Hit, [S] is stay, or [Q] is quit: ").lower()
			clear()
			if choice == "h":
				hit(playerHand)
				while total(dealerCard) < 17:
					hit(dealerCard)
				score(dealerCard, playerHand)
				startOver()
			elif choice == "s":
				while total(dealerCard) < 17:
					hit(dealerCard)
				score(dealerCard, playerHand)
				startOver()
			elif choice == "q":
				print("Bye!")
				exit()
	game()
