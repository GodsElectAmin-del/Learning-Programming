import json
'''
gptoutput = {
   [ {"Word": "Aufgabe","IPA" : "ɔpɣaːvə"}, 
    {"Word": "Aufgabe","IPA" : "taːk"}]
}
'''

# example output when using GPT 4.1 nano

gptoutput = '[ {"Word": "taak", "IPA": "taːk"}, {"Word": "opdracht", "IPA": "ˈɔpdrɑxt"}, {"Word": "klus", "IPA": "klʏs"}, {"Word": "opgave", "IPA": "ˈɔpˌɣɑvə"}, {"Word": "taken", "IPA": "ˈtɑkən"}, {"Word": "project", "IPA": "ˈproːʝɛkt"}, {"Word": "missie", "IPA": "mɪsˈsi"}, {"Word": "bezigheid", "IPA": "bəˈzɪɣɦɛit"}, {"Word": "onderneming", "IPA": "ˌɔndərˈneːmɪŋ"}, {"Word": "verantwoordelijkheid", "IPA": "vərˌɑntwɔrdəˌlɛjkɦɛit"}, {"Word": "opdrachtje", "IPA": "ˈɔpdrɑxtjə"}, {"Word": "klusje", "IPA": "ˈklʏsjə"}, {"Word": "puzzel", "IPA": "ˈpʏzəl"}, {"Word": "job", "IPA": "dʒɔb"}, {"Word": "verzoek", "IPA": "vərˈzuːxt"}, {"Word": "projectje", "IPA": "ˈproːʝɛktjə"}, {"Word": "taakje", "IPA": "ˈtaːk.jə"}, {"Word": "uitdaging", "IPA": "œytˈdɑːxɪŋ"}, {"Word": "verantwoordelijkheid", "IPA": "vərˌɑntwɔrdəˌlɛjkɦɛit"}, {"Word": "plan", "IPA": "plɑn"} ]'
pythonList = json.loads(gptoutput)
print(pythonList)