import random
import os

pwin = 0
dwin = 0

def calc_hand(hand):
    sum = 0

    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']

    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum

def determineEnd(win, message):
    global pwin, dwin
    
    if win == True:
        pwin += 1
    elif win == False:
        dwin += 1

    print('==================================')
    print(message)
    print('----------------------------------')
    print('Your score: {}'.format(pwin))
    print('Dealer score: {}'.format(dwin))
    print('==================================')

    print('')

    choice = input('[1] to play, [2] to stop: ')
    if choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        if dwin > pwin:
            print('See you next time, suuuucker!')
        else:
            print('You beat the dealer. Well, maybe you should try to beat me instead next time.')
        print('')
        quit()

while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

    random.shuffle(cards)

    dealer = []
    player = []

    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    standing = False
    first_hand = True

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing:
            print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]'.format(dealer[0]))

        print('Your Cards: [{}] ({})'.format(']['.join(player), player_score))
        print('')

        if standing:
            if dealer_score > 21:
                pwin += 1
                determineEnd(True, 'Dealer busted, you win!')
            elif player_score == dealer_score:
                determineEnd(None, 'Push, nobody wins or loses.')
            elif player_score > dealer_score:
                determineEnd(True, 'You beat the dealer, you win!')
            else:
                determineEnd(False, 'You lose :(')
            
            break

        if first_hand and player_score == 21:
            determineEnd(True, 'Blackjack! Nice')
            break

        first_hand = False

        if player_score > 21:
            determineEnd(False, 'You busted!')
            break

        if player_score == 21:
            standing = True
        else:
            print('What would you like to do?')
            print(' [1] Hit')
            print(' [2] Stand')

            print('')
            choice = input('Your choice: ')
            print('')

            if choice == '1':
                player.append(cards.pop())
            elif choice == '2':
                standing = True
                while calc_hand(dealer) <= 16:
                    dealer.append(cards.pop())


