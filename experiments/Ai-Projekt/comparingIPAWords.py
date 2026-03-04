#declaring an variable so i can use it in the loop for the word and also to have something to comapre
import html
import json

compIPA = "ʊ̯fɡaːbə"
ipa_list = [{'Word': 'taak', 'IPA': 'taːk'}, {'Word': 'opdracht', 'IPA': 'ˈɔpdrɑxt'}, {'Word': 'klus', 'IPA': 'klʏs'}, {'Word': 'opgave', 'IPA': 'ˈɔpˌɣɑvə'}, {'Word': 'taken', 'IPA': 'ˈtɑkən'}, {'Word': 'project', 'IPA': 'ˈproːʝɛkt'}, {'Word': 'missie', 'IPA': 'mɪsˈsi'}, {'Word': 'bezigheid', 'IPA': 'bəˈzɪɣɦɛit'}, {'Word': 'onderneming', 'IPA': 'ˌɔndərˈneːmɪŋ'}, {'Word': 'verantwoordelijkheid', 'IPA': 'vərˌɑntwɔrdəˌlɛjkɦɛit'}, {'Word': 'opdrachtje', 'IPA': 'ˈɔpdrɑxtjə'}, {'Word': 'klusje', 'IPA': 'ˈklʏsjə'}, {'Word': 'puzzel', 'IPA': 'ˈpʏzəl'}, {'Word': 'job', 'IPA': 'dʒɔb'}, {'Word': 'verzoek', 'IPA': 'vərˈzuːxt'}, {'Word': 'projectje', 'IPA': 'ˈproːʝɛktjə'}, {'Word': 'taakje', 'IPA': 'ˈtaːk.jə'}, {'Word': 'uitdaging', 'IPA': 'œytˈdɑːxɪŋ'}, {'Word': 'verantwoordelijkheid', 'IPA': 'vərˌɑntwɔrdəˌlɛjkɦɛit'}, {'Word': 'plan', 'IPA': 'plɑn'}]



sum(1 for y in compIPA if y in ipa_list)



# TODO THE IPAWord is not one but is an Array of Words and we need step by step compare each // done
# TODO We need to add a ranking after each itteration / done
# TODO Each word need to get there own scpre // done
score = 0
'''
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
'''

# the gpt list
ipa_list = [{'Word': 'taak', 'IPA': 'taːk'}, {'Word': 'opdracht', 'IPA': 'ˈɔpdrɑxt'}, {'Word': 'klus', 'IPA': 'klʏs'}, {'Word': 'opgave', 'IPA': 'ˈɔpˌɣɑvə'}, {'Word': 'taken', 'IPA': 'ˈtɑkən'}, {'Word': 'project', 'IPA': 'ˈproːʝɛkt'}, {'Word': 'missie', 'IPA': 'mɪsˈsi'}, {'Word': 'bezigheid', 'IPA': 'bəˈzɪɣɦɛit'}, {'Word': 'onderneming', 'IPA': 'ˌɔndərˈneːmɪŋ'}, {'Word': 'verantwoordelijkheid', 'IPA': 'vərˌɑntwɔrdəˌlɛjkɦɛit'}, {'Word': 'opdrachtje', 'IPA': 'ˈɔpdrɑxtjə'}, {'Word': 'klusje', 'IPA': 'ˈklʏsjə'}, {'Word': 'puzzel', 'IPA': 'ˈpʏzəl'}, {'Word': 'job', 'IPA': 'dʒɔb'}, {'Word': 'verzoek', 'IPA': 'vərˈzuːxt'}, {'Word': 'projectje', 'IPA': 'ˈproːʝɛktjə'}, {'Word': 'taakje', 'IPA': 'ˈtaːk.jə'}, {'Word': 'uitdaging', 'IPA': 'œytˈdɑːxɪŋ'}, {'Word': 'verantwoordelijkheid', 'IPA': 'vərˌɑntwɔrdəˌlɛjkɦɛit'}, {'Word': 'plan', 'IPA': 'plɑn'}]


# The logic works with thes list but the score is always 0

#the IPASCoreList
n = len(ipa_list)
m,n = 2,n 
IPAScoreList = []
for i in range (m):
 row = []
 for j in range(n):
   row.append(0)
 IPAScoreList.append(row)
print(IPAScoreList)



# TODO figure out how i can change the IPA word in an usealble loop / done
#we need to store an score for each word

# IPAword = "ɔpɣaːvə"
u = 0
for z in ipa_list:
  #z 
  IPAScoreList[0][u] = z
 # u += 1
  for y in compIPA:
    if y in z:
     print("this word is in the IPA word " + y)
     score += 1
  print("the score of ",z, "is: ",score) 
  IPAScoreList[1][u] = score
  score = 0
  u += 1

print(IPAScoreList)
scores = IPAScoreList[1]
max_value = max(scores)
highestIPA = scores.index(max_value)

print("Our word is ", IPAScoreList[0][highestIPA])

print("hihest value is ", max_value, "at index ", highestIPA)


  

# TODO We need to filter out the word with the highest score
# we need to assign each word in that array and number: is that an multi dimensional array // done

# TODO Creating a multidimensional Zero Matrix // done

# IPAScoreList = []

'''
m, n = 4, 5
mat = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)

print(mat)

I dont understand
'''
#TODO insert an GPT output of an promt generating IPA words in an array
# it seems like we want gpt to give us JSON outputs because you can convert JSON string to python list

#TODO have a JSON format in which we want gpt give us our to be used Info

# TODO generate a usable GPT prompt

# TODO have acces to an chatbot API the gnerates a Word and than have code inserting it inside the code

# Video to using chatgpt inside of python: https://www.youtube.com/watch?v=q5HiD5PNuck

#TODO u beed to unescape IPA because of some HTML stuff
#TODO 