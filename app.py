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
        id=str(task_id_control),
        title=data.get("title", "No title"),
        description=data.get("description", "")
    )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New task created successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
