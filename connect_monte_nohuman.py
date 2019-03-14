from playing.games.connect_four import ConnectFour
from playing.players.montecarlo import MonteCarlo



monte_player_one = MonteCarlo(True)
monte_player_two = MonteCarlo(False)

monte_player_two.assume(monte_player_one)
monte_player_one.assume(monte_player_two)

game = ConnectFour()
game.play(monte_player_one, monte_player_two)