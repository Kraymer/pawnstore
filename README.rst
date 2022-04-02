pawnstore ♟
===========

Chess library to import your PGN games and run queries on them

 **\pɔːn\**

Example
-------

::

    import pawnstore as ps
    from pawnstore.models import Panwstore

    store = Pawnstore(chesscom=("neTinquietePas", "xxx"),
        lichess=("kraymer", "xxx"))
    store.filter(side=ps.side.WHITE, eco=ps.eco.C44, result=ps.result.WIN).order_by("date").limit(3)

