"""Chess library to import your PGN games in a local database"""

import logging
from .models import Game


__version__ = "0.2.2"

logger = logging.getLogger(__name__)


def pawnstore(chesscom=None, lichess=None, full=False):
    from pawnstore.chesscom import CHESSCOM
    from pawnstore.lichess import LICHESS

    if chesscom:
        CHESSCOM.sync(chesscom, full)

    if lichess:
        LICHESS.sync(lichess, full)

    return (
        Game.select()
        .where(
            ((Game.user == chesscom) & (Game.website == CHESSCOM.name))
            | ((Game.user == lichess) & (Game.website == LICHESS.name))
        )
        .order_by(Game.timestamp)
    )
