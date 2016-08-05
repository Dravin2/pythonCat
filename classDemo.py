class Bird(object):
    have_feather=True
    way_of_reproduction='egg'
    def move(self,dx,dy):
        pos=[0,0]
        pos[0]=pos[0]+dx
        pos[1]=pos[1]+dy
        return pos

class Chicken(Bird):
    way_of_move="walk"
    possible_in_KFC=True

class Oriole(Bird):
    way_of_move='fly'
    possible_in_KFC=False


summer=Bird()
print summer.way_of_reproduction
print summer.move(5,8)


summer_c=Chicken()
print summer_c.way_of_reproduction
print summer_c.have_feather
print summer_c.way_of_move
print summer_c.possible_in_KFC



