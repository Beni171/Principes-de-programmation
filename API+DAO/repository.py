from flask import Flask, jsonify, request
import repository

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(repository.get_all_students()), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = repository.get_student_by_id(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

@app.route('/students/add/<string:text>', methods=['POST'])
def add_student_from_path(text):
    try:
        name, age = text.split("-", 1)   # split("-", 1) évite de casser si nom contient "-"
        age = int(age)
    except ValueError:
        return jsonify({"error": "Format must be name-age, e.g. John-22"}), 400

    student = repository.add_student(name, age)
    return jsonify(student), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)