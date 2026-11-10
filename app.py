
from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ravi", "rollNo": "101", "email": "ravi@gmail.com"}
]

# GET: Display all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET: Display one student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# POST: Add a student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify(data), 201

# PATCH: Update a student
@app.route('/students/<int:id>', methods=['PATCH'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student["id"] == id:
            student.update(data)
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# DELETE: Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})
    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
