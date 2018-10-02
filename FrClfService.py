'service wraaper using flask framework to provide REST api'


from flask import Flask, request, jsonify
from sklearn.externals import joblib
from rfpTextAnalysis import RfpTextAnalysis

clf = joblib.load('FRClfModel.pkl')
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     docs = request.form.getlist("text[]")
     if len(docs) == 0:
          return jsonify({"FunctionalReq":["error: input is empty"]})

    # predict if FunctionalReq or FunctionalReqNOT
     test_text = docs
     prediction = clf['FRClf'].predict(test_text)

     # The key phrases counts
     kc = RfpTextAnalysis()
     seq_tech = kc.getKeyPhrasesCounts(docs)

     #print(seq_tech)

     return jsonify({"FunctionalReq":prediction.tolist(), "WordCounts":seq_tech.to_json()})

if __name__ == '__main__':
     app.run(port=8010)
