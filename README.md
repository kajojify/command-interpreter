It is a small prototype for Mitmproxy **Commands language**.
It isn't inteded to be used for any reason except **Commands language** testing.

### How to use it

`python3.6 main.py [-h] [-p PATH | -c COMMAND] [-q | -t]`

`-c --command` - specify a single command to parse.

`-p --path` - specify the file with commands to parse.

`-q --quiet` - disable tokens list logging.

`-t --tranquil` - disable commands execution.


You can also just run it `python3.6 main.py` and input commands on your own:
```
kajoj@kajoj:~/PARSER/mitminterpreter$ python3.6 main.py 
>>> [a.sum(1 2 [10 20 30] 3) 100 200 a.sum([100 100 100])] | a.sum 114 27
LexToken(LBRACE,'[',1,0)
LexToken(COMMAND,'a.sum',1,1)
LexToken(LPAREN,'(',1,6)
LexToken(PLAIN_STR,'1',1,7)
LexToken(PLAIN_STR,'2',1,9)
LexToken(LBRACE,'[',1,11)
LexToken(PLAIN_STR,'10',1,12)
LexToken(PLAIN_STR,'20',1,15)
LexToken(PLAIN_STR,'30',1,18)
LexToken(RBRACE,']',1,20)
LexToken(PLAIN_STR,'3',1,22)
LexToken(RPAREN,')',1,23)
LexToken(PLAIN_STR,'100',1,25)
LexToken(PLAIN_STR,'200',1,29)
LexToken(COMMAND,'a.sum',1,33)
LexToken(LPAREN,'(',1,38)
LexToken(LBRACE,'[',1,39)
LexToken(PLAIN_STR,'100',1,40)
LexToken(PLAIN_STR,'100',1,44)
LexToken(PLAIN_STR,'100',1,48)
LexToken(RBRACE,']',1,51)
LexToken(RPAREN,')',1,52)
LexToken(RBRACE,']',1,53)
LexToken(PIPE,'|',1,55)
LexToken(COMMAND,'a.sum',1,57)
LexToken(PLAIN_STR,'114',1,63)
LexToken(PLAIN_STR,'27',1,67)

807
>>> 
```
