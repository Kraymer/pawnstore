from copy import deepcopy
import datetime as dt
import os
import unittest

from pawnstore import models
from pawnstore.services import insert_game

GAME_DATA = {
    "slug": "https://www.chess.com/game/live/48973761729",
    "pgn": '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2022.06.14"]\n[Round "-"]\n[White "JohnDoe"]\n[Black "NeTinquietePas"]\n[Result "1-0"]\n[CurrentPosition "r1b1k1nr/pp2pp1p/2qp2p1/1B1N4/1P2P3/2Q5/P4PPP/2B1K2R b Kkq -"]\n[Timezone "UTC"]\n[ECO "B22"]\n[ECOUrl "https://www.chess.com/openings/Sicilian-Defense-Alapin-Variation-2...Nc6-3.Nf3"]\n[UTCDate "2022.06.14"]\n[UTCTime "19:24:41"]\n[WhiteElo "1316"]\n[BlackElo "1217"]\n[TimeControl "300+5"]\n[Termination "Frederic65400 won by resignation"]\n[StartTime "19:24:41"]\n[EndDate "2022.06.14"]\n[EndTime "19:31:09"]\n[Link "https://www.chess.com/game/live/48973761729"]\n\n1. e4 {[%clk 0:05:05]} 1... c5 {[%clk 0:04:59.3]} 2. Nf3 {[%clk 0:05:08.1]} 2... Nc6 {[%clk 0:05:00.1]} 3. c3 {[%clk 0:05:11.9]} 3... g6 {[%clk 0:05:03.8]} 4. d4 {[%clk 0:05:13.2]} 4... cxd4 {[%clk 0:05:03.7]} 5. cxd4 {[%clk 0:05:18.1]} 5... Bg7 {[%clk 0:05:04.4]} 6. Nc3 {[%clk 0:05:22.1]} 6... d6 {[%clk 0:04:52.9]} 7. Bc4 {[%clk 0:05:23]} 7... Qb6 {[%clk 0:04:45.1]} 8. b3 {[%clk 0:04:38]} 8... Nxd4 {[%clk 0:04:19]} 9. Nxd4 {[%clk 0:04:27.7]} 9... Bxd4 {[%clk 0:04:23.9]} 10. Nd5 {[%clk 0:04:12.6]} 10... Qc5 {[%clk 0:02:50.3]} 11. Qd3 {[%clk 0:03:56.1]} 11... Bxa1 {[%clk 0:02:23.5]} 12. b4 {[%clk 0:03:52.6]} 12... Qc6 {[%clk 0:02:13.5]} 13. Bb5 {[%clk 0:03:53.1]} 13... Bc3+ {[%clk 0:02:13.2]} 14. Qxc3 {[%clk 0:03:45.6]} 1-0\n',
    "website": "chess.com",
    "speed": "bullet",
    "white": False,
    "eco": "B22",
    "eco_name": "Sicilian Defense Alapin Variation",
    "elo": "1217",
    "opp_name": "JohnDoe",
    "opp_elo": "1316",
    "time_control": "5+5",
    "user": "netinquietepas",
    "accuracy": 48.13,
    "moves": "e4 c5 Nf3 Nc6 c3 g6 d4 cxd4 cxd4 Bg7 Nc3 d6 Bc4 Qb6 b3 Nxd4 Nxd4 Bxd4 Nd5 Qc5 Qd3 Bxa1 b4 Qc6 Bb5 Bc3+ Qxc3",
    "timestamp": dt.datetime(2022, 6, 14, 21, 31, 9),
    "result": "L",
    "termination": "resigned",
}


class TestServices(unittest.TestCase):
    def test_insert_game_no_data(self):
        res = insert_game(None)
        assert res == False

    def test_insert_game_incomplete_data(self):
        data = deepcopy(GAME_DATA)
        data.pop("slug")
        res = insert_game(data)
        assert res == False

    def test_insert_game_success(self):
        res = insert_game(GAME_DATA)
        assert res == True
