from experta import * 

class MyFact(Fact) :
    pass

class ChoosePlayerKE(KnowledgeEngine):
    
    @Rule(MyFact(position='Forward'))
    def forward(self) :
        print('Your Player Is A Forward')
    
    @Rule(MyFact(position='Defender'))
    def defender(self) :
        print('Your Player Is A Defender')
        
    @Rule(MyFact(position='Midfilder'))
    def mid(self) :
        print('Your Player Is A Midfilder')
        
    @Rule(MyFact(position='GoalKeeper'))
    def goal(self) :
        print('Your Player Is A GoalKeeper')
        
    @Rule(MyFact(status='Sub'))
    def sub(self) :
        print('Your Player Is A Sub')
        
    @Rule(MyFact(status='line-up'))
    def sub(self) :
        print('Your Player Is One Of The Main 11 Player')
        
    @Rule(AND(MyFact(position = 'forward'), MyFact(status = 'goat')))
    def messi(self) :
        print('The Player Is Messi')
        
    @Rule(AND(MyFact(position = 'defender'), MyFact(status = 'skills')))
    def balde(self) :
        print('The Player Is Balde')
        
    @Rule(AND(MyFact(position = 'forward'), MyFact(status = 'speed')))
    def saka(self) :
        print('The Player Is Saka')
        
    @Rule(AND(MyFact(position = 'forward'), MyFact(status = 'brazilian')))
    def marte(self) :
        print('The Player Is Martinelli')
        
    @Rule(AND(MyFact(position = 'defender'), MyFact(status = 'big')))
    def araujo(self) :
        print('The Player Is Araujo')
        
    @Rule(AND(MyFact(position = 'midfilder'), NOT(MyFact(status = 'attack'))))
    def buski(self) :
        print('The Player Is Buski')
        
    @Rule(MyFact(status = 'old') | MyFact(status = 'captain'))
    def messi_buski(self) :
        print('The Player Is Buski or Messi')
        
    @Rule(AND(MyFact(position = 'midfilder'), MyFact(status = 'attack')))
    def de(self) :
        print('The Player Is De Jong')
        
    @Rule(AND(MyFact(position = 'goalkeeper'), MyFact(status = 'sub')))
    def penia(self) :
        print('The Player Is Penia')
        
    @Rule(AND(MyFact(position = 'goalkeeper'), NOT(MyFact(status = 'sub'))))
    def ter(self) :
        print('The Player Is Ter Stiegn')


engine = ChoosePlayerKE()
engine.reset()
engine.declare(MyFact(position = 'midfilder'))
engine.run()