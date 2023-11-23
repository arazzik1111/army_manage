from flask import Flask, jsonify, render_template
from security_proxy import SecurityProxy

app = Flask(__name__)

class Battalion:
    def __init__(self, name, species, count):
        self.name = name
        self.species = species
        self.count = count

battalions = [
    Battalion("Gnome Battalion", "Gnomes", 500),
    Battalion("Elf Battalion", "Elves", 1000),
    Battalion("Ent Battalion", "Ents", 200),
]

@app.route('/army', methods=['GET'])
def get_army():
    army = {b.name: {'species': b.species, 'count': b.count} for b in battalions}
    return jsonify(army)

@app.route('/army/json', methods=['GET'])
def get_army_json():
    army = {b.name: {'species': b.species, 'count': b.count} for b in battalions}
    return jsonify(army)

@app.route('/army/html', methods=['GET'])
def get_army_html():
    army = {b.name: {'species': b.species, 'count': b.count} for b in battalions}
    return render_template('html_template.html', army=army)

@app.route('/army/json-template', methods=['GET'])
def get_army_json_template():
    army = {b.name: {'species': b.species, 'count': b.count} for b in battalions}
    json_data = jsonify(army).get_json()
    return render_template('json_template.html', json_data=json_data)

@app.route('/army/secure/json', methods=['GET'])
def get_secure_army_json():
    proxy = SecurityProxy(get_army_service)
    return jsonify(proxy.get_army_data("authorized_user"))

if __name__ == '__main__':
    app.run(debug=True)
