import html
import unicodedata

# source IPA (HTML-escaped) for component extraction
compIPA = "zɔ.nənˌbʏ.mə"
# compIPA = list(unicodedata.normalize("NFD", html.unescape(source_escaped)))

# GPT output (HTML-escaped IPA strings)
ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]

# [{'Word': 'taak', 'IPA': 'taːk'}, {'Word': 'opdracht', 'IPA': 'ˈɔpdrɑxt'}]
# create 2xN matrix: row0 = words, row1 = scores (initialized 0)
n = len(ipa_list)
IPAScoreList = [[0] * n for _ in range(2)] # dont get this 

# [0] * n makes a list that is has [0] n times, n long with only 0s
# [] for _ in range(2) does this but for 2 times, two seperate arrays

# compute scores
for u, z in enumerate(ipa_list): # going troguh list and saving index // think this is actually wrong lol
    # you can enumrate through an two dimensional array via using u, z
    word = z.get("Word", "") # you can nte Word and what is next to it, understood
    ipa = z.get("IPA", "")
  #  ipa = unicodedata.normalize("NFD", html.unescape(ipa_raw)) # this seems important

    IPAScoreList[0][u] = word
    score = sum(1 for y in compIPA if y in ipa) # creating the score
    IPAScoreList[1][u] = score

    print("the score of", word, "is:", score)

# find best
scores = IPAScoreList[1]
best_i = max(range(len(scores)), key=scores.__getitem__)
print("Our word is", IPAScoreList[0][best_i])
print("highest value is", scores[best_i], "at index", best_i)

# optionally inspect matrix
print(IPAScoreList)
