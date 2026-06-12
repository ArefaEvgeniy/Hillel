answer = "y"
while answer != "y" or answer != "yes" or answer != "т" or answer != "так":
    ...
    answer = input("Do you want to continue? ('y' or 'yes' / 'т' або 'так') ").lower()


while True:
    ...
    answer = input("Do you want to continue? ('y' or 'yes' / 'т' або 'так') ").lower()
    if answer not in ("y", "yes", "т", "так"):
        break
