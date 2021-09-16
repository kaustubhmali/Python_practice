import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("34.py")))
print("Created: %s" % time.ctime(os.path.getctime("34.py")))
