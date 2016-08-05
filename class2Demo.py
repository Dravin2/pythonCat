class Human(object):
    laugh='hahahahha'
    name=''

    def __init__(self,more_words):
        self.name=more_words
        print 'hi,',more_words

    def show_name(self):
        print self.name

    def show_laugh(self):
        print self.laugh

    def show_10th(self):
        for i in range(10):
            self.show_laugh()

zry=Human('zry')
zry.show_name()
zry.show_10th()



#print help(Human)

#print dir(Human)
#print dir(list)
