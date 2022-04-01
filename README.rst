pawnstore ♟
===========

Chess library to import your PGN games and run queries on them

 **\pɔːn\**

Example
-------

::

    from pawnstore.constants import WHITE

    store = Pawnstore(chesscom=("neTinquietePas", "xxx"),
        lichess=("kraymer", "xxx"))
    store.filter(side=WHITE, eco="
