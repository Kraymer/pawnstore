pawnstore ♟
===========

    **/pɔːnstɔʁ/** :
 
    | chess library to import your PGN games and run queries on them
    |
    | Portmanteau word from : 
    | 1. *pawns*: defined by Philidor as *"The soul of chess"* 
    | 2. *datastore*: repository for persistently storing and managing collections of data

Example
-------

::

    import pawnstore as ps
    from pawnstore.models import Panwstore

    store = Pawnstore(chesscom=("neTinquietePas", "xxx"),
        lichess=("kraymer", "xxx"))
    store.filter(side=ps.side.WHITE, eco=ps.eco.C44, result=ps.result.WIN).order_by("date").limit(3)

