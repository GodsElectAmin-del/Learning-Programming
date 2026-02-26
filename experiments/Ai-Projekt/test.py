print("Hello World!")

## before implimenting Ai Models i need to impliment a grading logic
## as a basis we try to make a logical grading for folowing words
## Niederlädnsich: opgave — ˈɔpɣaːvə // [ˈaʊ̯fɡaːbə]
## TODO exert a single phonetic letter from an words

## ɔpɣaːvə
## the problem is that some have an think right next to them, 
##my solution extract the letters starting from right and when an extra think is 
## founr that mean take that plus the following letter



n = "aʊ̯fɡaːbə"
for n in reversed(n): # Das itteriert durch den String
    if n == "ː":
        print("we found a weard Charakter!")
    print(n)

#test U+0250–U+02AF
if '\ CA 92' < '\ CA 95': 
    print("This shit works!")
    # I might just use this instead, i just nead to check if my letters are in the intervall 
    # of the Base IPA letters if not we should just skip left and if that word is in that we combine them

'''
txt = "aʊ̯fɡaːbə"
print("ʊ̯" in txt)

txt = "aʊ̯fɡaːbə"
print("ʊ̯" in txt)
"""
# Alle möglichen Sonderfälle
#  ͡, ͜, ː, ˑ, ˈ, ˌ, ʰ, ʱ, ʲ, ʷ, ʳ, ʴ, ʵ, ʶ, ʸ, ʼ, ̀, ́, ̂, ̃, ̄, ̆, ̇, ̈, ̊, ̋, ̌, ̍, ̎, ̥, ̬, ̩, ̯, ̞, ̝, ̟, ̠, ̘, ̙, ̺, ̻, ̼, ̤, ̰, ̚, ̪, ̴, ̵

So wee need to loop through an word and have an if statement that looks for those letters
"""

# Idee, ich ittereiere durch den String und habe alle Zeichen
# Ich bedebke diese Sonderzeichen und kriere Logik um sie richtig herausuzufiltern
# Ich suche jedes dieser herausgefundene Wörter in derm Wort der anderen Sprache 
#ICh gebe jedesmal wenn der Buchstabe gefunden wurde ein eine 1 zum score, der der am Ende den höchsten Score hat wird ausgewählt

'''
# I figured out that 