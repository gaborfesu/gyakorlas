#szoveg="proba szoveg"
szoveg=input("Írjon be egy szöveget: ")
print(ord('A'))
print(ord('a'))
print()
kodolt=""
for i in range(0, len(szoveg)):
	kodolt+=str(ord(szoveg[i]))
print(kodolt)