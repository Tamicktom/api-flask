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
    return jsonify({"message": "New task created successfully"}), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(tasks)
    }

    return jsonify(output), 200


if __name__ == '__main__':
    app.run(debug=True)
