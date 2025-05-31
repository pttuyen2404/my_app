# model/character.py

from config.settings import rank_character

class Character:
    def __init__(self, name, progress):
        self.name = name
        self.progress, self.level_index, self.total_rank = self._calculate_level(progress)
        self.name_rank = rank_character[self.level_index][0]
        self.small_rank = self._calculate_sub_rank(self.progress, self.total_rank)

    def _calculate_level(self, progress):
        total = 0
        for i, (_, threshold) in enumerate(rank_character):
            if progress < total + threshold:
                return progress - total, i, threshold
            total += threshold
        # Nếu vượt max cấp độ
        return rank_character[-1][1], len(rank_character) - 1, rank_character[-1][1]

    def _calculate_sub_rank(self, progress, total):
        if progress < total / 3:
            return "Sơ kỳ"
        elif progress > total * 2 / 3:
            return "Hậu kỳ"
        else:
            return "Trung kỳ"

    def get_name(self):
        return self.name

    def get_name_rank(self):
        return self.name_rank

    def get_small_rank(self):
        return self.small_rank

    def get_total(self):
        return self.total_rank

    def get_progress(self):
        return self.progress
