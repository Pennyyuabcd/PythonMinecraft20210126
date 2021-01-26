from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z = PY.player.getTilePos()
PY.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python")
