"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit
import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"
        self.fail("Hello, World!")

    def test_minimax(self):
        
        player1 = game_agent.MinimaxPlayer()
        player2 = game_agent.AlphaBetaPlayer()
        the_board = isolation.Board(player1, player2)
        assert (the_board.get_legal_moves() is not None), "Legal moves is not blank"

    def test_alphabeta_no_forfeit(self):
        player1 = game_agent.AlphaBetaPlayer()
        player2 = game_agent.MinimaxPlayer()
        the_board = isolation.Board(player1, player2)
        move_history = []

        time_millis = lambda: 1000 * timeit.default_timer()
        time_limit = 150.

        while True:

            legal_player_moves = the_board.get_legal_moves()
            game_copy = the_board.copy()

            move_start = time_millis()
            time_left = lambda : time_limit - (time_millis() - move_start)
            curr_move = the_board._active_player.get_move(game_copy, time_left)
            move_end = time_left()

            if curr_move is None:
                curr_move = the_board.NOT_MOVED

            if move_end < 0:
                print(the_board._inactive_player, move_history, "timeout")
                break

            if curr_move not in legal_player_moves:
                if len(legal_player_moves) > 0:
                    print(the_board._inactive_player, move_history, "forfeit")
                    break
                print(the_board._inactive_player, move_history, "illegal move")
                break

            move_history.append(list(curr_move))

            the_board.apply_move(curr_move)




if __name__ == '__main__':
    unittest.main()
