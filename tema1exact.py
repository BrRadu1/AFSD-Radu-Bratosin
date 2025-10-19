stire = ("Jaf ca în filme la muzeul Luvru. Hoții au reușit să! fugă. cu mai multe? bijuterii ")
mid = len(stire)//2
primajum = stire[:mid]
adouajum = stire[mid:]
primajum = primajum.upper()
primajum = primajum.strip()
adouajum = adouajum[:: -1]
adouajum = adouajum[0].upper() + adouajum[1:]
adouajum = adouajum.replace(".", "")
adouajum = adouajum.replace(",", "")
adouajum = adouajum.replace("!", "")
adouajum = adouajum.replace("?", "")
textfinal = primajum + adouajum
print(textfinal)