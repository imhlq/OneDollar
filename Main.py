from Model import Room

## Parameter
Num_People = 100
Init_Money = 100
Ex_Money = 1
Game_Round = 10000
Save_Period = 5
##

myRoom = Room(Num_People, Init_Money, Ex_Money)
myRoom.goRun(Game_Round, Save_Period=Save_Period)
myRoom.save('./display/data.json')