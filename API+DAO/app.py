from flask import Flask, jsonify, request
import repository

app = Flask(__name__)

@app.route('/')
def home():
    return "Rest OK"

@app.route('/students', methods=['GET'])
def get_students():
    students = repository.get_all_students()
    return jsonify(students), 200


@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    return jsonify(repository.get_student_by_id(id))

@app.route('/students/add/', methods=['POST'])
def add_student():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    if not name or not age:
        return jsonify({"error": "Name and age are required"}), 400

    new_student = repository.add_student(name, age)

    return jsonify(new_student), 201

@app.route('/students/add/<string:text>', methods=['POST'])
def add_student_text(text):
    try:
        name, age = text.split("-")
        age = int(age)
    except ValueError:
        return jsonify({"error": "Format must be name-age"}), 400

    new_student = repository.add_student(name, age)
    return jsonify(new_student), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)