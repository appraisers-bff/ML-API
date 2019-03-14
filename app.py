import numpy as np
from flask import Flask, abort, jsonify, request
import _pickle as pickle
from pandas.io.json import json_normalize
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

reg = pickle.load(open('reg_model.pkl','rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    lines = request.get_json(force=True) # was 'data'
    # predict_request = [data['address'], data['city'], data['state'],
    # data['zipcode'], data['bed'], data['bath'], data['SqFt'],
    # data['SqFt']]
    # predict_request = [np.array(predict_request)]
    # y_hat = reg.predict(predict_request)
    address = lines['address']
    city = lines['city']
    state = lines['state']
    zipcode = lines['zipcode']
    bed = lines['bed']
    bath = lines['bath']
    SqFt = lines['SqFt']
    year = lines['year'] 
    
    test_case = np.array([[bath, bed, SqFt, year, zipcode]])
    reg.predict(test_case)
    prediction = reg.predict(test_case)
    output = list(prediction[0])[0]
    #return jsonify(results=address)
    
    zillow_data = ZillowWrapper('X1-ZWz1gyajrkda8b_76gmj')
    deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
    result = GetDeepSearchResults(deep_search_response)
    output2 = result.zestimate_amount
    op = list([int(output),int(output2)])
    return jsonify(results=op)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)