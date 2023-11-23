from flask import Flask, request, jsonify
#from datetime import datetime

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Retrieve the 'id' parameter from the request
    id_param = request.args.get('id')

    # Dummy data for demonstration
    data = {
        'id': int(id_param),
        'name': 'Example Name',
        'article': 123,
        'date': '2023-11-22',
        'additional_info': 'Example additional info'
    }

    # Return the data as JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)