'train and export the Function Requirement/company desc model to FRClfModel.pkl, watch out to uncomment sections in this file and fileProcess.py'

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from fileProcess import FileProcess

'''+++++++ uncomment this section for functional requirement classifier +++++++'''
MODELFILE = "FRClfModel.pkl"

'''+++++++ uncomment this section for company description classifier +++++++'''
'MODELFILE = "CompanyDescModel.pkl"'

def build_data_frame(path, classification):
    rows = []
    index = []
    fp = FileProcess()
    for file_name, text in fp.read_files(path):
        rows.append({'text': text, 'class': classification})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame

data = DataFrame({'text': [], 'class': []})
for path, classification in FileProcess.SOURCES:
    data = data.append(build_data_frame(path, classification))

print("len(data)")
print(len(data))


pipeline = Pipeline([
    ('count_vectorizer',   CountVectorizer()),
    ('classifier',         MultinomialNB())
])

train_text = []
train_y = []

for index, row in data.iterrows():
    train_text.append(row['text'])
    train_y.append(row['class'])

#pipeline.fit_transform(train_text, train_y)
pipeline.fit(train_text, train_y)

print("++++++++++++ vocabulary from the documents ++++++++++=")
vector = pipeline.named_steps['count_vectorizer']
print(vector.vocabulary_)

text = "this is a sample test that it is not a requirement \n\n dont think it is good for training."
test_text = [text]

joblib.dump({'FRClf': pipeline}, MODELFILE)
clf = joblib.load(MODELFILE)
predictions = clf['FRClf'].predict(test_text)
print(predictions)