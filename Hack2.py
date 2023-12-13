import os, sys
os.system("git pull")
try:
    __import__("Crack").Menu().menu()
except Exception as e:
    exit(str(e))
