# K�da valsts nol�ma p�riet uz jaunu naudas sist�mu.
#  Vecaj� sist�m� bija tr�s naudas vien�bas: d�lderis, grasis, sant�ms
# . Naudas v�rt�bas nor�d�tas zem�k.
# 1 d�lderis = 37 gra�i
# 1 grasis = 162 sant�mi
# Jaunaj� naudas sist�m� paliek tikai sant�mi un d�lderi. 
# Sant�ms saglab� savu v�rt�bu, bet 1 d�lderis b�s vien�ds ar 100 sant�miem.
#  Izveidot programmu, kas p�rveidotu vec�s sist�mas naudu uz jaunu.
#  Lietot�jam prasa ievad�t vec�s sist�mas d�lderus, gra�us un sant�mus.
# Tiek apr��in�ts jaun�s sist�mas d�lderu un gra�u daudzums.
#  Rezult�ts tiek par�d�ts konsol�.

dald=int(input("dālderi:"))
gras=int(input("graši"))
cents=int(input("santīmi"))

cents=cents+gras*162+dald*37*162
dald2=cents//100
cents2=cents-dald2*100
print()