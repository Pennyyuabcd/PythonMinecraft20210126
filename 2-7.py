from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z=PY.player.getTilePos()
try:
    answer=int(input("請問你右邊要放什麼方塊:"))
    PY.setBlock(x+1,y,z,answer)
except:
    print('只能輸入數字!!!!!!')