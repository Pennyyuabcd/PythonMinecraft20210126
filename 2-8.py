from mcpi.minecraft import Minecraft
PY=Minecraft.create()
userName = input("請輸入姓名:")
message = input("請輸入發言:")
PY.postToChat("<"+userName+">"+message)

