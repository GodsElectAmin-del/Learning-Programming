#declaring an variable so i can use it in the loop for the word and also to have something to comapre

compIPA = []

# getting every charkter in an IPA Word
for x in "ʊ̯fɡaːbə":
  compIPA.append(x) # storing my IPA letters seperatly

#print("All IPA letter ", compIPA)
#print("last value", compIPA[-1])

# comparing an IPA Word with IPA letters
# TODO THE IPAWord is not one but is an Array of Words and we need step by step compare each
# TODO We need to add a ranking after each itteration / done
# Each word need to get there own scpre
score = 0
ipa_list = [
    "ˈɔpɣaːvə",
    "taːk",
    "ˈɔpdrɑxt",
    "klʏs",
    "kɑrˈʋɛi̯",
    "ˈtaːkˌstɛlɪŋ",
    "ˈuːfəŋə(n)",
    "proːˈbleːm",
    "ˈpʏzəl",
    "ˈyːtˌdɑːɣɪŋ",
    "plɪxt",
    "vərˈplɪxtɪŋ",
    "ˈmɪsi",
    "ʋɛrk",
    "ɔpˈdrɑxtjə",
]
# TODO figure out how i can change the IPA word in an usealble loop
for x in ipa_list:
    x = IPAword
    
IPAword = "ɔpɣaːvə"
for y in compIPA:
  if y in IPAword:
     print("this word is in the IPA word " + y)
     score += 1
print("the score is ", score)   
  
#print (compIPA[2] in IPAword) # Das funktioniert, ich brauche nun logik die den [] bis zum Ende iteriert und Sachen einen Wert adiert

# einen while loop der eine variable eine Zahl bis zum Ende gehen lässt und jedesmal eine Zahl addiert