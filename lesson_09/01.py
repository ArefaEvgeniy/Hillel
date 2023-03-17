from langdetect import detect
from langdetect import detect_langs

print(detect("Несе Галя воду, коромисло гнеться. Гусі мої гусі..."))
print(detect_langs("Несе Галя воду, коромисло гнеться. Гусі мої гусі..."))
