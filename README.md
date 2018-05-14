It is a small prototype for Mitmproxy **Commands language**.
It isn't inteded to be used for any reason except **Commands language** testing.

### How to use it

`python3.6 main.py [-h] [-p PATH | -c COMMAND] [-q]`

`-c --command` - specify a single command to parse.

`-p --path` - specify the file with commands to parse.

`-q --quiet` - disable tokens list logging.

You can also just run it `python3.6 main.py` and input commands on your own:
```
>>> "~h google.com" | replay.client
LexToken(QUOTED_STR,'"~h google.com"',1,0)
LexToken(WHITESPACE,' ',1,15)
LexToken(PIPE,'|',1,16)
LexToken(WHITESPACE,' ',1,17)
LexToken(COMMAND,'replay.client',1,18)

>>> client.replay(view.select("~h google.com"))
LexToken(COMMAND,'client.replay',1,0)
LexToken(LPAREN,'(',1,13)
LexToken(COMMAND,'view.select',1,14)
LexToken(LPAREN,'(',1,25)
LexToken(QUOTED_STR,'"~h google.com"',1,26)
LexToken(RPAREN,')',1,41)
LexToken(RPAREN,')',1,42)

>>> ^CExiting...
```
