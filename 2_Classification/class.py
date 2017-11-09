import pandas, sklearn, csv, codecs,re
from sklearn.naive_bayes import MultinomialNB as mod
from sklearn.ensemble import RandomForestClassifier as mod2
from sklearn.feature_extraction.text import CountVectorizer

def constructcsv():

    csv_out = open('questions.csv', 'w')
    mywriter = csv.writer(csv_out,delimiter=',',lineterminator='\r\n')
    rows = zip(createliste("class"),createliste("question"))
    mywriter.writerows(rows)
    csv_out.close()

def createliste(i):

    questions = codecs.open("questions.txt", "r", 'utf-8')
    questionsread = questions.read()
    questions.close()

    listecl = re.findall("([QLDPT][A-Z]+[NLY]) .*", questionsread)
    listequestion = re.findall(" (.*)", questionsread)

    listeclass = ["Classe"]+listecl
    listques = ["Question"]+listequestion

    if(i=="class"):

        return listeclass

    if(i=="question"):

        return listques

constructcsv()

df_train= pandas.read_csv('questions.csv')
final=pandas.DataFrame(data=df_train)
y=final["Classe"]
x=final["Question"]

classifier=mod2()
targets=y.values

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(x.values)
classifier.fit(counts, targets)

examples = ["When is sarkozy born ?"]
example_counts = count_vectorizer.transform(examples)
print(example_counts)
predictions = classifier.predict(example_counts)
print(predictions) # [1, 0]
# mod.fit(X.values, y.values)
#
# final['predict'] = mod.predict(x.values)