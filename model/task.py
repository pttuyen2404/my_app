# model/task.py

class Task:
    def __init__(self, description, reward, times_completed=0):
        self.description = description
        self.reward = reward
        self.times_completed = times_completed

    def get_description(self):
        return self.description

    def get_reward(self):
        return self.reward

    def completed(self):
        self.times_completed += 1

    def to_dict(self):
        return {
            "description": self.description,
            "reward": self.reward,
            "times_completed": self.times_completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data['description'],
            reward=data['reward'],
            times_completed=data.get('times_completed', 0)
        )

    @classmethod
    def from_sql_row(cls, row):
        # row = (description, reward, times_completed)
        return cls(
            description=row[0],
            reward=row[1],
            times_completed=row[2]
        )
