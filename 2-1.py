from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z=PY.player.getTilePos()
PY.setBlock(x,y,z+1,7)
PY.setBlock(x,y,z-1,7)
PY.setBlock(x-1,y,z,7)
PY.setBlock(x+1,y,z,7)
PY.setBlock(x+1,y,z+1,7)
PY.setBlock(x-1,y,z+1,7)
PY.setBlock(x+1,y,z-1,7)
PY.setBlock(x-1,y,z-1,7)

