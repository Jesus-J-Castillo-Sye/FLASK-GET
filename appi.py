from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# ===========================
# Primer EndPoint
# ===========================
@app.route('/mat-juridico/archivo/<param>', methods=['GET'])
def endpoint1(param):
    # Check if a second parameter is provided
    if param: 
        # Return JSON with a list of 4 string values
        data = {
            'tipoDocumento': 'Example-value',
            'urlRepositorio': 'www.example.com',
            'descripcion': 'Nombre-archivo-example',
            'tamaño': 123,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(data)     
        
    else:
        return jsonify({'error': 'Second parameter missing'})


# ===========================
# Segundo EndPoint
# ===========================
@app.route('/mat-juridico/estado-procesal/<param>', methods=['GET'])
def endpoint2(param):
    if param: 
        data = {
            'Estado':'Fallido'
        }
        return jsonify(data)
    else:
        return jsonify({'error': 'Second parameter missing'})


# ===========================
# Tercer EndPoint
# ===========================
@app.route('/mat-juridico/relaciones-recuridas/<param>', methods=['GET'])
def endpoint3(param):
    # Check if a second parameter is provided
    if param: 

        data = {
            'relacionDeLasRelaciones': 'Example-value',
            'resolucionReccurrida': 'Example',
            'resolucionImpugnada': 'Example',
            'fechaResolucion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cuantia' : 123,
            'autoridadEmisoraDeLaResolucion': 'Example-value',
            'fechaEmision': datetime.now().strftime('%Y-%m-%d %H:%M:%S')            
        }
        return jsonify(data)  

        # Return JSON with a list of 4 string values  

    else:
        return jsonify({'error': 'Second parameter missing'})


if __name__ == '__main__':
    app.run(debug=True)
