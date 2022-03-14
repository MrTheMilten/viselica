import random as rd
class viselica:
    def __init__(self,tries=10):
        dictionari=['корова','слон','собака']
        self.word=rd.choice(dictionari)
        self.tries=tries
        self.game()

    def game(self):
        gues="_"*len(self.word)
        while self.tries!=0:
            print(gues)
            letter=str(input('Введите букву:'))
            if letter in list(self.word):
                for i in range (len(self.word)):
                    if letter==self.word[i]:
                        gues=gues[:i]+letter+gues[i+1:]
                if gues==self.word:
                    print("слово:"+self.word)
                    break
                print('попытки:'+str(self.tries))
            else:
                self.tries-=1
                print('попытки:'+str(self.tries))
        if self.tries==0: 
            print("проигрышь")
        else:
            print('победа')

if __name__=="__main__":
    viselica()

