import os
import unittest
import datetime

from pawnstore.lichess import LICHESS

GAME_LICHESS_DATA = {
    "id": "fqqEk7fv",
    "rated": True,
    "variant": "standard",
    "speed": "blitz",
    "perf": "blitz",
    "createdAt": datetime.datetime(
        2022, 6, 26, 11, 42, 53, 48000, tzinfo=datetime.timezone.utc
    ),
    "lastMoveAt": datetime.datetime(
        2022, 6, 26, 11, 52, 54, 287000, tzinfo=datetime.timezone.utc
    ),
    "status": "outoftime",
    "players": {
        "white": {
            "user": {"name": "kraymer", "id": "kraymer"},
            "rating": 1422,
            "ratingDiff": 24,
            "analysis": {"inaccuracy": 7, "mistake": 1, "blunder": 1, "acpl": 73},
        },
        "black": {
            "user": {"name": "Drobinshtern", "id": "drobinshtern"},
            "rating": 1421,
            "ratingDiff": -5,
            "analysis": {"inaccuracy": 6, "mistake": 1, "blunder": 1, "acpl": 73},
        },
    },
    "winner": "white",
    "opening": {
        "eco": "B21",
        "name": "Sicilian Defense: Smith-Morra Gambit Declined, Alapin Formation",
        "ply": 6,
    },
    "moves": "e4 c5 d4 cxd4 c3 Nf6 Bd3 Nc6 cxd4 Nxd4 Be3 Nc6 Qb3 b6 Ne2 e5",
    "analysis": [],
    "clock": {"initial": 300, "increment": 3, "totalTime": 420},
}


GAME_LICHESS_USER_CENTRIC_DATA = {
    "variant": "standard",
    "speed": "blitz",
    "timestamp": datetime.datetime(
        2022, 6, 26, 11, 42, 53, 48000, tzinfo=datetime.timezone.utc
    ),
    "result": "W",
    "moves": "e4 c5 d4 cxd4 c3 Nf6 Bd3 Nc6 cxd4 Nxd4 Be3 Nc6 Qb3 b6 Ne2 e5",
    "analysis": [],
    "pgn": None,
    "slug": "https://lichess.org/fqqEk7fv",
    "eco": "B21",
    "eco_name": "Sicilian Defense: Smith-Morra Gambit Declined, Alapin Formation",
    "white": True,
    "elo": 1422,
    "opp_name": "drobinshtern",
    "opp_elo": 1421,
    "website": "lichess.org",
    "user": "kraymer",
    "termination": "timeout",
    "time_control": "5+3",
}


class TestLichess(unittest.TestCase):
    def test_user_centric(self):
        res = LICHESS.user_centric(GAME_LICHESS_DATA, "kraymer")

        # locale timezone can alter the data
        res.pop("timestamp")
        GAME_LICHESS_USER_CENTRIC_DATA.pop("timestamp")

        assert res == GAME_LICHESS_USER_CENTRIC_DATA

    def test_user_centric_invalid_data(self):
        GAME_LICHESS_DATA.pop("opening")
        res = LICHESS.user_centric(GAME_LICHESS_DATA, "kraymer")

        assert res is None
