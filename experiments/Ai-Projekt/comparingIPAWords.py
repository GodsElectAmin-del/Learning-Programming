#declaring an variable so i can use it in the loop for the word and also to have something to comapre

compIPA = []

# getting every charkter in an IPA Word
for x in "ʊ̯fɡaːbə":
  compIPA.append(x) # storing my IPA letters seperatly

#print("All IPA letter ", compIPA)
#print("last value", compIPA[-1])

# comparing an IPA Word with IPA letters

IPAword = "ɔpɣaːvə"
for y in compIPA:
  if y in IPAword:
     print("this word is in the IPA word " + y)
  
#print (compIPA[2] in IPAword) # Das funktioniert, ich brauche nun logik die den [] bis zum Ende iteriert und Sachen einen Wert adiert

# einen while loop der eine variable eine Zahl bis zum Ende gehen lässt und jedesmal eine Zahl addiert