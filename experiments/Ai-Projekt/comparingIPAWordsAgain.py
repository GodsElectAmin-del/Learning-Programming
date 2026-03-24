import html
import unicodedata

# source IPA (HTML-escaped) for component extraction
source_escape_compIPA = "zɔ.nənˌbʏ.mə"
compIPA = html.unescape(source_escape_compIPA)
# compIPA = list(unicodedata.normalize("NFD", html.unescape(source_escaped)))

## TODO Unsecaping the HTML Stuff
source_escape_ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
ipa_list = html.unescape(source_escape_ipa_list)
#ipa_list = html.escape(temp_ipa_list)

# GPT output (HTML-escaped IPA strings)
#ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
ipa_test = {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}
n = len(ipa_list)
ipa_Scorelist = [[0] * n for _ in range(3)]
highest_score = 0

def Ipa_score(ipa_list):
    #i have the lenght of the IPA list
    z = ipa_test
    n = len(ipa_list)
    for index,item in enumerate(ipa_list):
        Word = item.get("Word", "")
        IPA = item.get("IPA", "")

        Score = sum( (1* len(compIPA) / len(Word)) for y in compIPA if y in IPA)
        ipa_Scorelist[2][index] = Score
        ipa_Scorelist[0][index] = Word
        ipa_Scorelist[1][index] = IPA

    # TODO now i need the highest score
    finalScore = ipa_Scorelist[2]
    highest_score = 0
    for i, ThisFinalScore in enumerate(finalScore): # Dont now why that works
        ThisFinalScore = finalScore[i] 
        if ThisFinalScore > highest_score:
            highest_score = ThisFinalScore
            thisIndex = i
    TheBestWord = ipa_Scorelist[0][thisIndex]
    return Word, IPA, ipa_Scorelist, highest_score, thisIndex, TheBestWord

print(Ipa_score(ipa_list))
'''
    word = z.get("Word", "") # you can nte Word and what is next to it, understood
    ipa = z.get("IPA", "")
'''

'''
1 * lamda
lamda = len(compIPA) / len/(Word)
'''
#TODO I want a multi dimensional list where in the first is the normal word, 2end is the IPA word and 3rd is the score
#TODO the score is broken, because the code compares html stuff and not actually IPA elements