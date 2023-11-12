from sly import Lexer
class CalcLexer(Lexer):
    literals={';'}
    ignore=' '
    tokens = {NUMBER,SER,PAR,END,ID}
   # ignore=' '
    ID=r'[a-zA-Z]'
    NUMBER=r'[0-9]+'
    def NUMBER(self,t):
        t.value=int(t.value)
        return t
    ID['ser']=SER
    ID['par']=PAR
    ID['end']=END
    #ID['if']=IF
lex=CalcLexer()
expr='ser 10 20 end'
for token in lex.tokenize(expr):
    print(f'value={token.value} type={token.type}')
        
