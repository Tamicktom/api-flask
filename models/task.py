from collections import namedtuple

TaskType = namedtuple('TaskType', ['id', 'title', 'description', 'completed'])


class Task:
    data: TaskType

    def __init__(self, id: int, title: str, description: str, completed: bool = False) -> None:
        self.data = TaskType(id, title, description, completed)

    def to_dict(self) -> TaskType:
        return self.data
