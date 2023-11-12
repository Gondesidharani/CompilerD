from cirlex import *
from sly import Parser
class Calcparser(Parser):
#       num=[]
    tokens=Calclexer.tokens
    literals=Calclexer.literals
    @_('exp2 ";" exp1')
    def exp1(self,value):
        pass
    @_('exp2 ";"')
    def exp1(self,value):
        pass
    @_('SER exp3')
    def exp2(self,value):
        return num[0]+num[1]
    @_('PAR exp3')
    def exp2(self,value):
        pass
    @_('NUMBER')
    def exp2(self,value):
        num=[]
        num.append(value[0])
        return num
    @_('exp2 exp3')
    def exp3(self,value):
        pass
    @_('END')
    def exp3(self,value):
        return value[0]
lex=Calclexer()
par=Calcparser()
expr='''SER 10 20 end'''
x=par.parse(lex.tokenize(expr))
print(x)

