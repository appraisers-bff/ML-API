import numpy as np
from flask import Flask, abort, jsonify, request
import _pickle as pickle
from pandas.io.json import json_normalize
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

reg = pickle.load(open('reg_model.pkl','rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    lines = request.get_json(force=True)
    address = lines['address']
    city = lines['city']
    state = lines['state']
    zipcode = lines['zipcode']
    bed = lines['bed']
    bath = lines['bath']
    SqFt = lines['SqFt']
    year = lines['year'] 
    
    input = np.array([[bath, bed, SqFt, year, zipcode]])
    prediction = reg.predict(input)
    output = list(prediction[0])[0]
    
    zillow_data = ZillowWrapper(API_KEY_HERE)
    deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
    result = GetDeepSearchResults(deep_search_response)
    output2 = result.zestimate_amount
    op = list([int(output),int(output2)])
    return jsonify(results=op)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)
