from langdetect import detect, detect_langs

print(detect("War doesn't show who's right, just who's left."))
print(detect("Ein, zwei, drei, vier"))

print(detect_langs("Otec matka syn."))
print(detect_langs("Ein, zwei, drei, vier"))
