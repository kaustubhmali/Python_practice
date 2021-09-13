import struct, platform

print(struct.calcsize("P") * 8)
print(platform.architecture()[0])