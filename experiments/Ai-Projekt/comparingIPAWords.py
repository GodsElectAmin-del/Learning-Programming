#declaring an variable so i can use it in the loop for the word and also to have something to comapre

compIPA = []

# getting every charkter in an IPA Word
for x in "ʊ̯fɡaːbə":
  compIPA.append(x) # storing my IPA letters seperatly



# TODO THE IPAWord is not one but is an Array of Words and we need step by step compare each
# TODO We need to add a ranking after each itteration / done
# TODO Each word need to get there own scpre
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




# TODO figure out how i can change the IPA word in an usealble loop / done
#we need to store an score for each word

# IPAword = "ɔpɣaːvə"
for z in ipa_list:
  for y in compIPA:
    if y in z:
     print("this word is in the IPA word " + y)
     score += 1
  print("the score is ", score) 
  score = 0
print("the score is ", score)   
  