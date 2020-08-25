from flask import Flask, jsonify, request
from Controller.Main import *
from Model.SearchRoute import *

app = Flask(__name__)

api = None

@app.route("/")
def index():
    return jsonify({"message":"Hello Json!"})

@app.route("/api/create",  methods=["POST"])
def create():
    data = request.get_json()
    if isBlank(data['origin']):
        return jsonify({"message":"Origin cannot be null"}), 406
    elif isBlank(data['destiny']):
        return jsonify({"message":"Destiny cannot be null"}), 406

    api.dataFile.writeFile(data['origin'], data['destiny'], data['amount'])

    return jsonify({"message": "New route successfully created"})

@app.route("/api/search",  methods=["POST"])
def search():
    data = request.get_json()
    if isBlank(data['origin']):
        return jsonify({"message":"Origin cannot be null"}), 406
    elif isBlank(data['destiny']):
        return jsonify({"message":"Destiny cannot be null"}), 406

    search = Search()

    dataRoute = search.batter_price_travel(route=data['origin']+"-"+data['destiny'],dataRoutes= api.dataFile.dataInput)

    return jsonify({"route": dataRoute[0], "amount":dataRoute[1]})
    
def isBlank (data):
    if data and data.strip():
        return False
    
    return True

if __name__ == '__main__':
    args = []

    for param in sys.argv:
        args.append(param)
        
    fileInput = args[1]

    api = Main(fileInput)
    api.openningFile()

    app.run(debug=True)