from playing.games.connect_four import ConnectFour
from playing.players.montecarlo import MonteCarlo
from playing.players.human import HumanPlayer


human_player = HumanPlayer(True)
monte_player = MonteCarlo(False)

monte_player.assume(human_player)
human_player.assume(monte_player)

game = ConnectFour()
game.play(human_player, monte_player)