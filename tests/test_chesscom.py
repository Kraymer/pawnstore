import os
import unittest
import datetime

from pawnstore.chesscom import CHESSCOM

GAME_CHESSCOM_DATA = {
    "url": "https://www.chess.com/game/live/49888733221",
    "pgn": '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2022.06.25"]\n[Round "-"]\n[White "carlosmolina123"]\n[Black "NeTinquietePas"]\n[Result "0-1"]\n[CurrentPosition "8/p6p/2pRN3/7k/2P3p1/6PK/r6P/8 w - -"]\n[Timezone "UTC"]\n[ECO "B31"]\n[ECOUrl "https://www.chess.com/openings/Sicilian-Defense-Nyezhmetdinov-Rossolimo-Fianchetto-Variation-4.Bxc6"]\n[UTCDate "2022.06.25"]\n[UTCTime "09:32:42"]\n[WhiteElo "1160"]\n[BlackElo "1240"]\n[TimeControl "300+5"]\n[Termination "NeTinquietePas won by checkmate"]\n[StartTime "09:32:42"]\n[EndDate "2022.06.25"]\n[EndTime "09:43:55"]\n[Link "https://www.chess.com/game/live/49888733221"]\n\n1. e4 {[%clk 0:05:03.6]}} 0-1\n',
    "time_control": "300+5",
    "end_time": 1656150235,
    "rated": True,
    "accuracies": {"white": 74.59, "black": 73.09},
    "tcn": "mCYIgv5QfH2UHQXQlBIBvB0KBv92eg!TcM7PvK8!blTCKAPBMuBJnvClAl45kAJKfeKYow2jabj2uD5bdbYPgoPbeb98lC8Sb52V56!2DV2V6Y1LCISmogmiYZiagoaiogiagoaioxUMZRVNISMEvELE",
    "uuid": "bf38162e-f469-11ec-8e7a-78ac4409ff3c",
    "initial_setup": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "fen": "8/p6p/2pRN3/7k/2P3p1/6PK/r6P/8 w - -",
    "time_class": "blitz",
    "rules": "chess",
    "white": {
        "rating": 1160,
        "result": "checkmated",
        "@id": "https://api.chess.com/pub/player/carlosmolina123",
        "username": "carlosmolina123",
        "uuid": "bbba3c20-e22a-11e7-805a-000000000000",
    },
    "black": {
        "rating": 1240,
        "result": "win",
        "@id": "https://api.chess.com/pub/player/netinquietepas",
        "username": "NeTinquietePas",
        "uuid": "eb201f0a-1380-11ea-ad89-575be077b8a4",
    },
}

GAME_CHESSCOM_USER_CENTRIC_DATA = {
    "slug": "https://www.chess.com/game/live/49888733221",
    "pgn": '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2022.06.25"]\n[Round "-"]\n[White "carlosmolina123"]\n[Black "NeTinquietePas"]\n[Result "0-1"]\n[CurrentPosition "8/p6p/2pRN3/7k/2P3p1/6PK/r6P/8 w - -"]\n[Timezone "UTC"]\n[ECO "B31"]\n[ECOUrl "https://www.chess.com/openings/Sicilian-Defense-Nyezhmetdinov-Rossolimo-Fianchetto-Variation-4.Bxc6"]\n[UTCDate "2022.06.25"]\n[UTCTime "09:32:42"]\n[WhiteElo "1160"]\n[BlackElo "1240"]\n[TimeControl "300+5"]\n[Termination "NeTinquietePas won by checkmate"]\n[StartTime "09:32:42"]\n[EndDate "2022.06.25"]\n[EndTime "09:43:55"]\n[Link "https://www.chess.com/game/live/49888733221"]\n\n1. e4 {[%clk 0:05:03.6]}} 0-1\n',
    "website": "chess.com",
    "speed": "bullet",
    "white": False,
    "eco": "B31",
    "eco_name": "Sicilian Defense Nyezhmetdinov Rossolimo Fianchetto Variation",
    "elo": "1240",
    "opp_name": "carlosmolina123",
    "opp_elo": "1160",
    "time_control": "5+5",
    "user": "NeTinquietePas",
    "accuracy": 73.09,
    "moves": "e4",
    "timestamp": datetime.datetime(2022, 6, 25, 11, 43, 55),
    "result": "W",
    "termination": "checkmated",
}


class TestChesscom(unittest.TestCase):
    def test_user_centric(self):
        res = CHESSCOM.user_centric(GAME_CHESSCOM_DATA, "NeTinquietePas")
        assert res == GAME_CHESSCOM_USER_CENTRIC_DATA
