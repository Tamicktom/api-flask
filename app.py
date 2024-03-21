# Libraries imports
from flask import Flask, request
from typing import List

# Local imports
from models.task import Task, TaskType

app = Flask(__name__)

tasks: List[TaskType] = []


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return "Task created"


if __name__ == '__main__':
    app.run(debug=True)
