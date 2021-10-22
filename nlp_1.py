from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather"



blob = TextBlob(text)


#print(blob.sentences)
#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(round(blob.sentiment.polarity,3))
#print(round(blob.sentiment.subjectivity,3))

sentences = blob.sentences

#for sentence in sentences:
    #print(sentence)
    #print(round(sentence.sentiment.polarity, 3))



from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())

#print(blob.sentiment)

#for sentence in blob.sentences:
    #print(sentence.sentiment)



spanish = blob.translate(to='es')
chinese = blob.translate(to='zh')

#print(spanish)

#documentation for textblob translate for langauge directory

##print(spanish.translate)

print(chinese.translate)

#pluralization and singularization

from textblob import Word

index = Word('index')
#print(index.pluralize())

cacti = Word('cacti')

#print(cacti.singularize())

#wordlist

animals = TextBlob('dog cat fish bird').words

#print(animals.pluralize())

#spellcheck in correction 

word = Word('theyr')

#print(word.spellcheck())    #this method just gives correct word options
#print(word.correct())   #this method prints the corrected word based off confidence intervals(wont be printed if dont run spellcheck, but it still used them to choose)


word1 = Word("studies")
word2 = Word("varieties")

#print(word1.stem())
#print(word2.stem())

#print(word1.lemmatize())
#print(word2.lemmatize())

happy = Word("Happy")

#print(happy.definitions)

#print(happy.synsets)    #extract texet from list and iterate thru with for loop

for s in happy.synsets:
    for lemma in s.lemmas():
        print(lemma.name())


synonym = happy.synset[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)