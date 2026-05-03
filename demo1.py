from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id":1, "name":"Arthur", "age":22},
    {"id":2, "name":"salut", "age":88}, 
]

@app.route('/')
def home():
    return "Bienvenue dans la gestion des étudiants !"

@app.route('/students', methods=['GET'])
def getStudents():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def addStudents():
    new=request.get_json()
    new['id']=len(students)+1
    students.append(new)
    return jsonify(new), 201

@app.route('/students/<int:id>', methods=['GET'])
def getStudentbyId(id):
    student = next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur":"le student n'existe pas"}), 400

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:   
        return jsonify({"erreur":"le student n'existe pas"}), 400
    data = request.get_json()
    student.update(data)
    return jsonify(student)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:   
        return jsonify({"erreur":"le student n'existe pas"}), 400
    students.remove(student)
    return jsonify({"message":"student supprimé"}), 200

if __name__ == '__main__':
    app.run(debug=True)