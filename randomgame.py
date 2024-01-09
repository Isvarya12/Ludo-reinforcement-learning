import cv2
import ludopy
import numpy as np

g = ludopy.Game()
there_is_a_winner = False

while not there_is_a_winner:
    (dice, move_pieces, player_pieces, enemy_pieces, player_is_a_winner, there_is_a_winner), player_i = g.get_observation()

    if len(move_pieces):
        piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
    else:
        piece_to_move = -1

    _, _, _, _, _, there_is_a_winner = g.answer_observation(piece_to_move)
board = g.render_environment()
cv2.namedWindow("Ludo Board", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Ludo Board", 900, 700)
cv2.imshow("Ludo Board", board)
cv2.waitKey(0)
                
