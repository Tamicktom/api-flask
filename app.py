# Libraries imports
from flask import Flask, request, jsonify
from typing import List

# Local imports
from models.task import Task, TaskType

app = Flask(__name__)

tasks: List[TaskType] = []
task_id_control: int = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control,
        title=data.get("title", "No title"),
        description=data.get("description", "")
    )
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({
        "message": "New task created successfully",
        "id": new_task.data.id
    }), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(tasks)
    }

    return jsonify(output), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id: int):
    task = None

    for t in tasks:
        if t.data.id == task_id:
            task = t
            break

    if task:
        return jsonify({
            "id": task.data.id,
            "title": task.data.title,
            "description": task.data.description
            }), 200

    return jsonify({"message": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id: int):
    task = None

    for t in tasks:
        if t.data.id == task_id:
            task = t
            break

    if task:
        data = request.get_json()
        new_task_data = TaskType(
            id=task_id,
            title=data.get("title", task.data.title),
            description=data.get("description", task.data.description),
            completed=data.get("completed", task.data.completed)
        )
        task.data = new_task_data

        return jsonify({"message": "Task updated successfully"}), 200

    return jsonify({"message": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    global tasks
    task = None

    for t in tasks:
        if t.data.id == task_id:
            task = t
            break

    if task:
        tasks = [t for t in tasks if t.data.id != task_id]
        return jsonify({"message": "Task deleted successfully"}), 200

    return jsonify({"message": "Task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
