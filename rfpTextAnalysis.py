'Utility class for RFP Text Analysis'
'functions: '
'     getKeyPhrasesCounts: count the word counts of key phrases like mobile, eccommerece, to determine the subsequent UC classifier'

from pandas import DataFrame
from pandas import Series
from sklearn.feature_extraction.text import CountVectorizer

class RfpTextAnalysis:
    # returns the key phrases counts
    def getKeyPhrasesCounts(self, docs) :

        vocabulary = ["ecommerce", "mobile", "sap", "order management"]

        #vocabulary = [{"ecommerce","digital commerce"}, "mobile", "sap", "order management"]
        vocabIndex = ["Commerce", "Mobile", "Sap", "OMS"]
        vect = CountVectorizer(ngram_range=(1, 2), vocabulary=vocabulary)
        dtm = vect.fit_transform(docs)
        vocab = vect.get_feature_names()

        #print(DataFrame(dtm.A, columns=vocab).to_string())
        #print(dtm[0, vocab=="ecommerce"])

        # sum the word count per keyword
        dtm = dtm.toarray()
        word_count = []
        j=0
        for j in range(len(vocab)):
            count = 0

            for i in range(len(dtm)):
                occ = dtm[i, j]
                count += occ

            word_count.append(count)

        seq_tech = Series(word_count, index=vocabIndex)
        return seq_tech

