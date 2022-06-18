# pawnstore ♟

> **/pɔːnstɔʁ/** :
>
>    *n.* chess library to import your PGN games in a local database
>  
>    Portmanteau word from :
>    1. *pawns*: defined by Philidor as *\"The soul of chess\"*
>    2. *datastore*: repository for persistently storing and managing collections of data

## Features

-   centralized access to your online and OTB chess games
-   chess.com and lichess.org importers
-   user-centric data representation to facilitate extraction of your
    own statistics

## Example

    >>> import pawnstore as ps
    >>> from pawnstore.models import Panwstore
    >>>
    >>> store = Pawnstore(chesscom=("neTinquietePas", "xxx"),
        lichess=("kraymer", "xxx"))
    >>> for game in store.filter(white=True).limit(3):
        print(game)
    neTinquietePas x rms1952
    neTinquietePas x AnselmoBarrena
    neTinquietePas x samisamuel

