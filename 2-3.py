from mcpi.minecraft import Minecraft
PY=Minecraft.create()
import random,time
while True:
    x,y,z=PY.player.getTilePos()
    color=random.randrange(0,16)
    PY.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(3)
    