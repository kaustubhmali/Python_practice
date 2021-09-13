import platform
import os
import site

print(os.name)
print(platform.system())
print(platform.release())


print(site.getsitepackages())