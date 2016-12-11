import sys
import time
import simone_io as io

class Game:
    def __init__(self, game_mode):
        self.sequence = []
        self.hiscore = 0

        # Debug Mode
        if game_mode == 0:
            self.io = io.GPIO()
        # Raspberry Pi GPIO Mode
        elif game_mode == 1:
            self.io = io.Screen()
        else:
            print "Illegal Game Mode Provided. Use '0' for GPIO and '1' for debug"
            sys.exit(2) # 2 is the exit code for an invalid command line argument

    def _play_round(self):
        should_continue_round = True

        # Round Loop
        while should_continue_round:
            self._add_to_sequence() # Add another color to the sequence
            self._display_sequence() # Show the sequence to the player
            should_continue_round = self._validate_user_input() # See if the player matches the sequence
            time.sleep(0.5)

        # Endgame
        if self._should_display_hiscore():
            self._display_hiscore()
        else:
            self.io.blink_all()
        self._reset_round()

    def _add_to_sequence(self):
        self.sequence.append(self.io.choose_random_color())

    def _display_sequence(self):
        self.io.blink_sequence(self.sequence)

    def _validate_user_input(self):
        for color in self.sequence:
            # If the player enters the wrong color or they take too
            # long to enter a color, end the game
            if (color != self.io.wait_for_input()): # NOTE: In 'debug' mode, one cannot lose the game due to timeout
                return False

        return True

    def _should_display_hiscore(self):
        # The score is determined from how many colors
        # in the sequence the user has correctly matched,
        # which when the game ends, will be all except the
        # current color in the sequence
        return (len(self.sequence) - 1) > self.hiscore

    def _display_hiscore(self):
        # If a game is a hiscore, blink every color once,
        # then blink them all at once
        self.io.blink_sequence(self.io.colors)
        self.io.blink_all()

    def _reset_round(self):
        # The game is reset by emptying the sequence
        self.sequence = []

    def _shutdown(self):
        self.io.wait_for_input(-1) # Wait for input indefinitely
        self.start() # Once there's input, the game will start over

    def _should_start_next_round(self):
        # If there's input within 5 seconds of a round ending, start another round
        return self.io.wait_for_input(5) != ''

    def start(self):
        self._play_round()
        while self._should_start_next_round():
            self._play_round()
        self._shutdown()

    def quit(self):
        self.io.cleanup() # Cleanup any resources, like active GPIO pins

if __name__ == '__main__':
    if (len(sys.argv) <= 1 or not sys.argv[1].isdigit()):
        print 'No Game Mode Specified'
        print
        print 'Usage: python main.py game_mode'
        print
        print 'game_mode:'
        print '0: Raspberry Pi GPIO'
        print '1: Debug (Command-line)'
        sys.exit(2) # 2 is the exit code for an invalid command line argument

    game = Game(int(sys.argv[1])) # Make a game based on the game mode selected

    try:
        game.start()
    except KeyboardInterrupt: # Handle interrupting the game
        pass
    finally:
        game.quit()
