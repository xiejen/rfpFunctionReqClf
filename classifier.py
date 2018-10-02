
'Program to create the Functional Requirement Classifer model and validate it'
from fileProcess import FileProcess
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.feature_extraction.text import TfidfTransformer








def build_data_frame(path, classification):
    rows = []
    index = []
    fp = FileProcess()
    for file_name, text in fp.read_files(path):
        rows.append({'text': text, 'class': classification})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame

'Main'
data = DataFrame({'text': [], 'class': []})
for path, classification in FileProcess.SOURCES:
    data = data.append(build_data_frame(path, classification))

data = data.reindex(numpy.random.permutation(data.index))

pipeline = Pipeline([
    #('count_vectorizer',   CountVectorizer(ngram_range=(1, 2))),
    ('count_vectorizer',   CountVectorizer()),
#    ('tfidf_transformer',  TfidfTransformer()),
    ('classifier',         MultinomialNB())
])

k_fold = KFold(n=len(data), n_folds=10)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indices, test_indices in k_fold:
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values.astype(str)

    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values.astype(str)

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)
    print("******************* predictions*********")
#    print(predictions)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=FileProcess.FRN)
    scores.append(score)

    for i in range(0, len(predictions))  :
        if predictions[i] != test_y[i] :
            print("********text is \n" + test_text[i])
            print("The wrong clf is: " + predictions[i])
            print("*******************")

print('Total files classified:', len(data))
print('Score:', sum(scores)/len(scores))
print('Confusion matrix:')
print(confusion)

print("++++++++++++ vocabulary from the documents ++++++++++=")
vector = pipeline.named_steps['count_vectorizer']
#print(vector.vocabulary_)