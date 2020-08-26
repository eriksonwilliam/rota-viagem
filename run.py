from flask import Flask, jsonify, request
from Controllers.Main import *
from Models.SearchRoute import *

app = Flask(__name__)

api = None

@app.route("/api/create",  methods=["POST"])
def create():
    data = request.get_json()
    if isBlank(data['origin']):
        return jsonify({"message":"Origin cannot be null"}), 406
    elif isBlank(data['destiny']):
        return jsonify({"message":"Destiny cannot be null"}), 406
    elif data['amount'] <= 0:
        return jsonify({"message":"Amount cannot be less than or equal to 0"}), 406

    api.dataFile.writeFile(data['origin'], data['destiny'], data['amount'])

    return jsonify({"message": "New route successfully created"})

@app.route("/api/search",  methods=["POST"])
def search():
    data = request.get_json()
    if isBlank(data['origin']):
        return jsonify({"message":"Origin cannot be null or empty"}), 406
    elif isBlank(data['destiny']):
        return jsonify({"message":"Destiny cannot be null or empty"}), 406
    
    search = Search()
    api.dataFile.readFile()
    better_route = search.better_price_travel(route=data['origin']+"-"+data['destiny'],dataRoutes= api.dataFile.dataInput)

    if better_route is not None:
        return jsonify({"route": better_route[0], "amount":better_route[1]})
    
    return jsonify({"message":"Route not found"}), 400
    
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