print("Hello World!")

## before implimenting Ai Models i need to impliment a grading logic
## as a basis we try to make a logical grading for folowing words
## Niederlädnsich: opgave — ˈɔpɣaːvə // [ˈaʊ̯fɡaːbə]
## TODO exert a single phonetic letter from an words

## ɔpɣaːvə
## the problem is that some have an think right next to them, 
##my solution extract the letters starting from right and when an extra think is 
## founr that mean take that plus the following letter

for n in "aʊ̯fɡaːbə": # Also ich kann jetzt alle printen aber es fehlt die Logik
    print(n)

txt = "aʊ̯fɡaːbə"
print("ː" in txt)

txt = "aʊ̯fɡaːbə"
print("ʊ̯" in txt)
"""
# Alle möglichen Sonderfälle
#  ͡, ͜, ː, ˑ, ˈ, ˌ, ʰ, ʱ, ʲ, ʷ, ʳ, ʴ, ʵ, ʶ, ʸ, ʼ, ̀, ́, ̂, ̃, ̄, ̆, ̇, ̈, ̊, ̋, ̌, ̍, ̎, ̥, ̬, ̩, ̯, ̞, ̝, ̟, ̠, ̘, ̙, ̺, ̻, ̼, ̤, ̰, ̚, ̪, ̴, ̵

So wee need to loop through an word and have an if statement that looks for those letters
"""