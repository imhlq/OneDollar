from Model import Room

## Parameter
Num_People = 100
Init_Money = 100
Ex_Money = 1
Game_Round = 10000
##

myRoom = Room(Num_People, Init_Money, Ex_Money)
myRoom.goRun(Game_Round)
myRoom.save()