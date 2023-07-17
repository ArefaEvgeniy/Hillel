from datetime import datetime
import os
from langdetect import detect_langs


print(datetime.now())
print(os.getcwd())

print(detect_langs("Це Евген, привіт"))
