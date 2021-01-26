from mcpi.minecraft import Minecraft
PY=Minecraft.create()
#print #印出 沒有回答
#input #印出 可以回答
x,y,z=PY.player.getTilePos()
answer=int(input('請問你右邊要放什麼方塊:'))
PY.setBlock(x+1,y,z,answer)
