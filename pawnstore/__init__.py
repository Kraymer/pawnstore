import logging
from .models import Game

from pawnstore.chesscom import CHESSCOM
from pawnstore.lichess import LICHESS

__app__ = "pawnstore"
logger = logging.getLogger(__name__)


def pawnstore(chesscom=None, lichess=None, full=False):
    if chesscom:
        CHESSCOM.sync(chesscom, full)

    if lichess:
        LICHESS.sync(lichess)

    return Game.select().order_by(Game.timestamp)
