# model/task.py

class Task:
    def __init__(self, description, reward, times_completed=0):
        self.description = description
        self.reward = reward
        self.times_completed = times_completed
        self.parent = None

    def get_description(self):
        return self.description

    def get_reward(self):
        return self.reward

    def completed(self):
        self.times_completed += 1
        return self.parent.grow(self.reward)

    def register(self,observer):
        self.parent = observer

    @classmethod
    def from_sql_row(cls, row):
        # row = (description, reward, times_completed)
        return cls(
            description=row[0],
            reward=row[1],
            times_completed=row[2]
        )
