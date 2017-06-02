def main():
    restart = 1
    while restart == 1:
        game()
        restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")

    print "Thanks for playing!"
