import random
import pygame
import os
from pygame.rect import Rect
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")
FPS = 60
VEL = 7 #Velocity of how face card is drawn
PLAYER_FONT = pygame.font.SysFont('comicsans', 40)
CARD_WIDTH, CARD_HEIGHT = 100, 150

Ace_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', 'AceOfSpades.png'))
Ace_Of_Spades = pygame.transform.scale(Ace_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
King_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', 'KingOfSpades.png'))
King_Of_Spades = pygame.transform.scale(King_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
Jack_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', 'JackOfSpades.png'))
Jack_Of_Spades = pygame.transform.scale(Jack_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
Six_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', '6OfSpades.png'))
Six_Of_Spades = pygame.transform.scale(Six_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
Five_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', '5OfSpades.png'))
Five_Of_Spades = pygame.transform.scale(Five_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
Three_Of_Spades_Image = pygame.image.load(os.path.join('BlackJackAssets', '3OfSpades.png'))
Three_Of_Spades = pygame.transform.scale(Three_Of_Spades_Image, (CARD_WIDTH, CARD_HEIGHT))
Deck_Image = pygame.image.load(os.path.join('BlackJackAssets', 'Deck.png'))
Deck = pygame.transform.scale(Deck_Image, (CARD_WIDTH, CARD_HEIGHT))


def draw_window(dealer_new_card, player_new_card):
  WIN.fill((250, 250, 250))
  WIN.blit(Ace_Of_Spades, (350, 350))
  WIN.blit(King_Of_Spades, (425, 350))
  WIN.blit(Jack_Of_Spades, (425, 0))
  WIN.blit(Six_Of_Spades, (350, 0))
  WIN.blit(Five_Of_Spades, (dealer_new_card.x, dealer_new_card.y))
  WIN.blit(Three_Of_Spades, (player_new_card.x, player_new_card.y))
  WIN.blit(Deck, (200, 200))
  player_text = PLAYER_FONT.render("Players Hand: ", 1, (255, 0, 0))
  dealer_text = PLAYER_FONT.render("Dealers Hand: ", 1, (255, 0, 0))
  WIN.blit(player_text, (10, 370))
  WIN.blit(dealer_text, (10, 10))

  pygame.display.update()

def dealer_draw_card(card):
  if card.x != 500:
    card.x += 5
  if card.y != 0:
    card.y -= 5
  #Keep adding each value as long as it doesnt hit final x/y
  #I think this keeps looping even when done, could be a problem

def player_draw_card(card):
  while card.x != 500 or card.y != HEIGHT-150:
    if card.x != 500:
      card.x += 5
    if card.y != HEIGHT-150:
      card.y += 5
  print("Done")
  print(card.x, card.y)

def main():
  pos = 0, 0
  newcard = pygame.Rect(200, 200, CARD_WIDTH, CARD_HEIGHT)
  deck_top_card = pygame.Rect(200, 200, CARD_WIDTH, CARD_HEIGHT)
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get(): #Gets a list of all different events occurring
        if event.type == pygame.QUIT: #if quit stop running
            run = False
            exit() #Ends entire code
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
  

    if deck_top_card.collidepoint(pos):
      player_draw_card(deck_top_card)
    dealer_draw_card(newcard)
    #player_draw_card(deck_top_card)
    draw_window(newcard, deck_top_card)
    #print(deck_top_card.x, deck_top_card.y)

  pygame.quit()

if __name__ == "__main__":
    main()   

#Regular code
def facecards(newlistval):
  if newlistval == 1:
    newlistval = 'A'
  elif newlistval == 11:
    newlistval = 'J'
  elif newlistval == 12:
    newlistval = 'Q'
  elif newlistval == 13:
    newlistval = 'K'
  return newlistval

def unfacecards(newlistvalue):
  if newlistvalue == 'A':
    #PROBLEM, ONE OR ELEVEN????
    newlistvalue = 11
  elif newlistvalue == 'J':
    newlistvalue = 10
  elif newlistvalue == 'Q':
    newlistvalue = 10
  elif newlistvalue == 'K':
    newlistvalue = 10
  return int(newlistvalue)

def playervsdealer(player, dealer, i):
  if(player > 21):
    return('-----------Player Bust!, Dealer Wins Round ' + str(i) + '! -----------')
  elif(dealer > 21):
    return('-----------Dealer Bust!, Player Wins Round ' + str(i) + '! -----------')
  if(dealer > player and dealer <= 21):
    return('-----------Dealer Wins Round ' + str(i) + '! -----------')
  elif(player > dealer and player <= 21):
    return('-----------Player Wins Round ' + str(i) + '! -----------') 
  elif(player == dealer):
    return('-----------Push! -----------')

def hitfunc(hand, dictionary):
  h1 = facecards(random.randint(1, 13)) 
  count = 0
  send = 0
  countme = 0
  for key in dictionary.keys():
    countme += newdict[key]
  if(countme == 0):
    print('No more cards! Choose stand')
    return hand
  for key in newdict.keys(): #Players Hand 1
    if key == str(h1):
      if(newdict[key] != 0):
        print('New Card: ' + str([key]))
        hand += int(unfacecards(key))
        newdict[key] -= 1
        break
      else: 
        while(count == 0): 
          #generate new randint
          print('NewCard already at 0!')
          h1 = random.randint(1, 13)
          h1 = facecards(h1)
          for hkeys in newdict.keys():
            if hkeys == str(h1) and newdict[hkeys] != 0:
              count = 1
              print('Success with: ' + str(h1))
              print('New Card: ' + str([hkeys]))
              hand += int(unfacecards(hkeys))
              newdict[hkeys] -= 1
              send = 1
              break
        if(send == 1):
          break
  return hand

def cardcountcheck(dictionary):
  countme = 0
  for key in dictionary.keys():
    countme += newdict[key]
  return countme

newdict = {'A': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4, 'J': 4, 'Q': 4, 'K': 4}

decks = 1
p1 = facecards(random.randint(1, 13))
d1 = facecards(random.randint(1, 13))
p2 = facecards(random.randint(1, 13))
d2 = facecards(random.randint(1, 13))

dealer = 0
player = 0

#Testing material
 #newdict['5'] = 0
 #d1 = 5
 #newdict['6'] = 0
 #p1 = 6

#IDEAS TO IMPLEMENT
  #for i in range(0, 52*deck) - theory

  #Could make a list A through King, and pop the 0's
  # So we don't have to randint 1-13 until hit

  #Balance, Along with Double

print('Enter your name: ', end='')
name = input()
print('Welcome To The Casino ' + name + ', Have Fun Losing!')

#0, cards left? while there's at least 4 cards left
# Set a check at end of loop to see if theres at least 4
# Set a way to make sure you can't hit on Nothing
# Like, No cards left! Force Stand-

for i in range(0, 10): 
  print('')
  print('')

  check = cardcountcheck(newdict)
  if check < 4:
    print('out of cards!')
    break
  #Check % 4 maybe to see how many times you can hit?
  #------------------------------------------------ cont


  count = 0
  send = 0
  for key in newdict.keys(): #Dealer Hand 1
    if key == str(d1): #if key is Ace
      #print('d1 curr is = ' + str(d1))
      if(newdict[key] != 0):
        #print('Success with: ' + str(d1))
        print('Dealer First Card: ' + str([key]))
        dealer += int(unfacecards(key))
        #print(newdict[key])
        newdict[key] -= 1
        #print('NewValue D1: ' + str(newdict[key]))
        break
      else: 
        while(count == 0): #while Ace is = 0
          #generate new randint
          print('d1 hit 0!')
          d1 = random.randint(1, 13)
          d1 = facecards(d1)
          #print('new d1: ' + str(d1))
          #reset key for loop
          for keys in newdict.keys():
            if keys == str(d1) and newdict[keys] != 0:
              count = 1
              print('Success with: ' + str(d1))
              print('Dealer First Card: ' + str([keys]))
              dealer += int(unfacecards(keys))
              newdict[keys] -= 1
              #print('NewValue D1: ' + str(newdict[keys]))
              send = 1
              break
        if(send == 1):
          break

  print('')
  print('')

  count = 0
  send = 0
  for key in newdict.keys(): #Player Hand 1
    if key == str(p1): #if key is Ace
      #print('p1 curr is = ' + str(p1))
      if(newdict[key] != 0):
        #print('Success with: ' + str(p1))
        print('Player First Card: ' + str([key]))
        player += int(unfacecards(key))
        newdict[key] -= 1
        #print('NewValue P1: ' + str(newdict[key]))
        break
      else: 
        while(count == 0): #while Ace is = 0
          #generate new randint
          print('p1 hit 0!')
          p1 = random.randint(1, 13)
          p1 = facecards(p1)
          print('new p1: ' + str(p1))
          #reset key for loop
          for keys in newdict.keys():
            if keys == str(p1) and newdict[keys] != 0:
              count = 1
              print('Success with: ' + str(p1))
              print('Player First Card: ' + str([keys]))
              player += unfacecards(keys)
              #print(newdict[keys])
              newdict[keys] -= 1
              #print('NewValue P1: ' + str(newdict[keys]))
              send = 1
              break
        if(send == 1):
          break

  print('')
  print('')

  count = 0
  send = 0
  for key in newdict.keys(): #Dealer Hand 2
    if key == str(d2):
      #print('d2 curr is = ' + str(d2))
      if(newdict[key] != 0):
        #print('Success with: ' + str(d2))
        print('Dealer Second Card: ' + str([key]))
        dealer += unfacecards(key)
        #print(newdict[key])
        newdict[key] -= 1
        #print('NewValue ' + key + ': ' + str(newdict[key]))
        break
      else: 
        while(count == 0): #while Ace is = 0
          #generate new randint
          print('d2 hit 0!')
          d2 = random.randint(1, 13)
          d2 = facecards(d2)
          print('new d2: ' + str(d2))
          #reset key for loop
          for keyz in newdict.keys():
            if keyz == str(d2) and newdict[keyz] != 0:
              count = 1
              print('Success with: ' + str(d2))
              print('Dealer Second Card: ' + str([keyz]))
              dealer += unfacecards(keyz)
              newdict[keyz] -= 1
              #print('NewValue ' + keyz + ': ' + str(newdict[keyz]))
              send = 1
              break
        if(send == 1):
          break

  print('')
  print('')

  count = 0
  send = 0
  for key in newdict.keys(): #Player Hand 2
    if key == str(p2):
      #print('p2 curr is = ' + str(p2))
      if(newdict[key] != 0):
        #print('Success with: ' + str(p2))
        print('Player Second Card: ' + str([key]))
        player += unfacecards(key)
        #print(newdict[key])
        newdict[key] -= 1
        #print('NewValue ' + key + ': ' + str(newdict[key]))
        break
      else: 
        while(count == 0): #while Ace is = 0
          #generate new randint
          print('p2 hit 0!')
          p2 = random.randint(1, 13)
          p2 = facecards(p2)
          print('new p1: ' + str(p2))
          #reset key for loop
          for keyzz in newdict.keys():
            if keyzz == str(p2) and newdict[keyzz] != 0:
              count = 1
              print('Success with: ' + str(p2))
              print('Player Second Card: ' + str([keyzz]))
              player += unfacecards(keyzz)
              newdict[keyzz] -= 1
              #print('NewValue ' + keyzz + ': ' + str(newdict[keyzz]))
              send = 1
              break
        if(send == 1):
          break


  print('')
  print('')

  print('Dealer has: ' + str(dealer))
  print('Player has: ' + str(player))

  print('Would you like to hit or stand? h/s')
  standhit = input()
  if standhit == 'quit' or standhit == 'exit':
    exit()

#--------------------Hit/Stand-----------------------
  if(standhit == 's'): #Player chooses to stand
    while(dealer < 17):
      print('dealer hits')
      #dealer needs over 17
      if (cardcountcheck(newdict) > 1):
        print('cards left: ', cardcountcheck(newdict))
        dealer = hitfunc(dealer, newdict) #for examp sake
        print('Dealer now has: ' + str(dealer))
      else:
        break
    print(playervsdealer(player, dealer, i))
  else: #player hit, change to elif later for split/double
    #insert hit, function with dict maybe
    player = hitfunc(player, newdict)
    if(player > 21):
      print('Player now has: ' + str(player))
      print(playervsdealer(player, dealer, i))
    else:
      print('Player now has: ' + str(player))
      while(player <= 21):
        print('Hit again? Y/N: ')
        answer = input()
        if (answer == 'quit' or answer == 'exit'):
          exit()
        if(answer == 'N'):
          while(dealer < 17):
            print('dealer hits')
            #dealer needs over 17
            dealer = hitfunc(dealer, newdict) #for examp sake
            print('Dealer now has: ' + str(dealer))
          print(playervsdealer(player, dealer, i))
          #Pass to playvsdealer
          break
        elif(answer == 'Y'):
          player = hitfunc(player, newdict)
          #player hit
          print('Player now has: ' + str(player))
          if(player > 21):
            print(playervsdealer(player, dealer, i))
    


  #Reset, make reset func? naaa
  p1 = facecards(random.randint(1, 13))
  d1 = facecards(random.randint(1, 13))
  p2 = facecards(random.randint(1, 13))
  d2 = facecards(random.randint(1, 13))

  dealer = 0
  player = 0


  print('')

  print (newdict)
