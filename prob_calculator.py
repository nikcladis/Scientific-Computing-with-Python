import copy
import random


class Hat:

    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            self.contents += [key] * int(value)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents

        random_ball_list = []
        for i in range(0, num):
            bid = random.randint(0, len(self.contents) - 1)
            random_ball_list.append(self.contents.pop(bid))

        return random_ball_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(0, num_experiments):
        h = copy.deepcopy(hat)
        balls = h.draw(num_balls_drawn)
        dic = {}
        for b in balls:
            x = dic.get(b, 0)
            dic[b] = x + 1

        found = True
        for b, x in expected_balls.items():
            if dic.get(b, 0) < x:
                found = False
                break

        if found:
            count += 1

    return count / num_experiments