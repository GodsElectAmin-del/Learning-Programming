import html
import unicodedata

# source IPA (HTML-escaped) for component extraction
compIPA = "zɔ.nənˌbʏ.mə"
# compIPA = list(unicodedata.normalize("NFD", html.unescape(source_escaped)))

# GPT output (HTML-escaped IPA strings)
ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
ipa_test = {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}
n = len(ipa_list)
ipa_Scorelist = [[0] * n for _ in range(3)]

def Ipa_score(ipa_list):
    #i have the lenght of the IPA list
    z = ipa_test
    n = len(ipa_list)
    for index,item in enumerate(ipa_list):
        Word = item.get("Word", "")
        IPA = item.get("IPA", "")

        Score = sum( 1 for y in compIPA if y in IPA)
        ipa_Scorelist[2][index] = Score
        ipa_Scorelist[0][index] = Word
        ipa_Scorelist[1][index] = IPA

    return n, Word, IPA, ipa_Scorelist

print(Ipa_score(ipa_list))
'''
    word = z.get("Word", "") # you can nte Word and what is next to it, understood
    ipa = z.get("IPA", "")
'''

#TODO I want a multi dimensional list where in the first is the normal word, 2end is the IPA word and 3rd is the score