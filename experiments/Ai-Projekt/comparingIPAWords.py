#declaring an variable so i can use it in the loop for the word and also to have something to comapre

compIPA = []

# getting every charkter in an IPA Word
for x in "ʊ̯fɡaːbə":
  compIPA.append(x) # storing my IPA letters seperatly

print("All IPA letter ", compIPA)
print("last value", compIPA[-1])

