from mcpi.minecraft import Minecraft
PY=Minecraft.create()
while True:

    x,y,z=PY.player.getTilePos()
    block1=PY.getBlock(x,y-1,z)
    block2=PY.getBlock(x+1,y-1,z)
    block3=PY.getBlock(x-1,y-1,z)
    block4=PY.getBlock(x,y-1,z+1)
    block5=PY.getBlock(x,y-1,z-1)
    if block1 == 8 or block1==9 or block2 == 8 or block2 == 9\
    or block3 == 8 or block3 == 9 or block4 == 8 or block4 ==9\
    or block5 == 8 or block5 == 9:
        PY.setBlock(x,y-1,z,79)
        PY.setBlock(x,y-1,z+1,79)
        PY.setBlock(x,y-1,z-1,79)
        PY.setBlock(x-1,y-1,z,79)
        PY.setBlock(x+1,y+1,z,79)
    
    