import html
import unicodedata

# source IPA (HTML-escaped) for component extraction
compIPA = "zɔ.nənˌbʏ.mə"
# compIPA = list(unicodedata.normalize("NFD", html.unescape(source_escaped)))

# GPT output (HTML-escaped IPA strings)
ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]

def Ipa_score(ipa_list):
    #i have the lenght of the IPA list
    n = len(ipa_list)

    return n

print(Ipa_score(ipa_list))
'''
    word = z.get("Word", "") # you can nte Word and what is next to it, understood
    ipa = z.get("IPA", "")
'''