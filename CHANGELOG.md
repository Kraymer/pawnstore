# CHANGELOG



## v0.2.1 (2023-08-31)

### Fix

* fix: add user-agent ([`f2881bd`](https://github.com/Kraymer/pawnstore/commit/f2881bdb1c965f118537aeeba1e1fe88f0560868))

### Refactor

* refactor: remove pysqlite3 dep ([`0bbace6`](https://github.com/Kraymer/pawnstore/commit/0bbace6de2852808ebc98aa2d4a663e52574d2fc))

* refactor: move imports ([`248a930`](https://github.com/Kraymer/pawnstore/commit/248a9303dec9a9c822a48ad0851c02fa6eb409eb))


## v0.2.0 (2022-09-05)

### Ci

* ci: add python-semantic-release.yml (#9) ([`0d517ce`](https://github.com/Kraymer/pawnstore/commit/0d517ce09e9b3603392bbd1b3066ee549eb9ab21))

### Documentation

* docs: update README.md example code ([`c6bc6f7`](https://github.com/Kraymer/pawnstore/commit/c6bc6f74ee620ef1aa7107e5054cc63205845f25))

### Feature

* feat: increase import limit tenfold ([`6a2aeed`](https://github.com/Kraymer/pawnstore/commit/6a2aeedeae3b9538d8624d49a0c437dc9efd9bb8))

* feat: add Game.as_dict() method ([`b789150`](https://github.com/Kraymer/pawnstore/commit/b7891504841a9b579c8c87b64c51e4110d9e0203))

* feat: add codecov and build workflows ([`95c18d1`](https://github.com/Kraymer/pawnstore/commit/95c18d18e5cae693d2f86923a07c351143f40c93))

### Fix

* fix: catch &amp; skip error when importing non games ([`1addea2`](https://github.com/Kraymer/pawnstore/commit/1addea230ed14cbf2be15079063286f55d0341a8))

* fix(tests): remove timestamp from user centric data (#5) ([`eb054d5`](https://github.com/Kraymer/pawnstore/commit/eb054d50601bf452dabfd8e5d73447d46c316aad))

### Refactor

* refactor: convert README.rst to markdown format (#3) ([`e052b9f`](https://github.com/Kraymer/pawnstore/commit/e052b9f60eb28fb973bb33e5f98168414e273c5a))

### Test

* test: add test_services (#2)

Use in memory sqlite database for tests ([`dc1ef3c`](https://github.com/Kraymer/pawnstore/commit/dc1ef3c72f66aaf009b47088b3bca2abfdc472ff))

### Unknown

* setup: fix setup.py ([`ee599f7`](https://github.com/Kraymer/pawnstore/commit/ee599f7f89c6fb517102bf86e59f5e63d7fd1b00))

* tests: add test_lichess.py file (#7) ([`d07eb65`](https://github.com/Kraymer/pawnstore/commit/d07eb6596acc1bf06590bfa41f91279951bfaa84))

* tests: add test_chesscom.py file ([`e75effe`](https://github.com/Kraymer/pawnstore/commit/e75effe84546b106fee642d7b169d0543c2c22ac))

* Update README.md: add badges ([`e8642e8`](https://github.com/Kraymer/pawnstore/commit/e8642e83f78bf3b3b5069e2aefc2847db6ee7c7c))

* Update README.md ([`56339f6`](https://github.com/Kraymer/pawnstore/commit/56339f6e36c6181297600efc000ef3601d8be56c))

* Merge pull request #1 from Kraymer/pytest

feat: add codecov and build workflows ([`d8004bc`](https://github.com/Kraymer/pawnstore/commit/d8004bcc90817583858c9a935114a4806c1a717a))


## v0.1.1 (2022-05-22)

### Fix

* fix: description on pypi ([`774a23d`](https://github.com/Kraymer/pawnstore/commit/774a23d9f9f09d983f64d64f9ee5f2dc68700543))

* fix: topic classifier ([`7aee17a`](https://github.com/Kraymer/pawnstore/commit/7aee17a4ce8b1ae07e750190b8c97eaebdc4334c))


## v0.1.0 (2022-05-22)

### Documentation

* docs: update README.rst ([`d0121de`](https://github.com/Kraymer/pawnstore/commit/d0121ded8984c95e9a25adc203ff5ababd5e5baf))

### Feature

* feat: add setup.py ([`2371676`](https://github.com/Kraymer/pawnstore/commit/23716764c852c9086a9778e4160c078c96662782))

* feat: initial version with chess.com and lichess importers ([`a04a730`](https://github.com/Kraymer/pawnstore/commit/a04a730badef51da850d5bf8132cee7b200ee274))

* feat: add .gitignore, pre-commit-config and requirements.txt ([`9327b4f`](https://github.com/Kraymer/pawnstore/commit/9327b4f46b1963b878137fab2a4e6bd8b2f761cd))

### Fix

* fix: return games of given users only ([`df9f54f`](https://github.com/Kraymer/pawnstore/commit/df9f54fc3ed7a9ea9a8dcb40c3bb0bef66057ec3))

* fix: chess.com time control setting ([`8c9f8dc`](https://github.com/Kraymer/pawnstore/commit/8c9f8dca2001890d44e80da55f9170277072b527))

* fix: remove unnecessary calls to lichess api ([`801ad1a`](https://github.com/Kraymer/pawnstore/commit/801ad1a054b32819edfe9a767820538db3eeecf1))

* fix: make LICHESS_API_TOKEN env var definition optional ([`b14451e`](https://github.com/Kraymer/pawnstore/commit/b14451e347ddc62c432662f54f45c342d244c01d))

* fix: add missing &#34;full&#34; parameter ([`2805ead`](https://github.com/Kraymer/pawnstore/commit/2805eadd4d575c64a681f4b55c423a196383c8ab))

### Unknown

* setup: semantic-release config ([`b699ddd`](https://github.com/Kraymer/pawnstore/commit/b699ddd605b5bf07414e755f9cbcaa1c5e5e7588))

* setup: add python-publish.yml ([`2e8d6c4`](https://github.com/Kraymer/pawnstore/commit/2e8d6c4f91754b5a5b72aa571ba9fa7fef0243b2))

* Update README.rst ([`32a2283`](https://github.com/Kraymer/pawnstore/commit/32a228395c321654a5008002951d85229e9a84ab))

* Update README.rst ([`e10417f`](https://github.com/Kraymer/pawnstore/commit/e10417f2f6eac82a8157373156f0e3e2eec9e199))

* Update README.rst ([`fc7530c`](https://github.com/Kraymer/pawnstore/commit/fc7530c81b268bbc56857bd2526f83db557e1c8c))

* Update README.rst ([`e857529`](https://github.com/Kraymer/pawnstore/commit/e85752954e874be800e848607225dd8fffd64a34))

* Update and rename README.md to README.rst ([`b8cd5b6`](https://github.com/Kraymer/pawnstore/commit/b8cd5b6cda17622f07cbdecadedae775ba84901d))

* Initial commit ([`b6da289`](https://github.com/Kraymer/pawnstore/commit/b6da2891f3222d91c2b5636365f3eae9d42e66c0))
