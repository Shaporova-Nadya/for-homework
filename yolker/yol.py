import random
from collections import deque

class Yolker:
    def __init__(self, events):
       
        if not events:
            raise ValueError("Список событий не может быть пустым.")
            
        self.event = [item[0] for item in events]
        probabilities = [item[1] for item in events]
        self.n = len(self.event)
        
        if any(p < 0 for p in probabilities):
            raise ValueError("Вероятности не могут быть отрицательными.")
            
        prob_sum = sum(probabilities)
        if not (0.999999 <= prob_sum <= 1.000001):
            raise ValueError(f"Сумма вероятностей должна быть равна 1")
            
        self._setup_tables(probabilities)

    def _setup_tables(self, probabilities):
        
        prob_scaled = [p * self.n for p in probabilities]
        self.prob = [0.0] * self.n
        self.a = [0] * self.n

        small = deque()
        large = deque()
        for i, p in enumerate(prob_scaled):
            if p < 1.0:
                small.append(i)
            else:
                large.append(i)

        while small and large:
            s_idx = small.popleft()
            l_idx = large.popleft()

            self.prob[s_idx] = prob_scaled[s_idx]
            self.a[s_idx] = l_idx

            prob_scaled[l_idx] = prob_scaled[l_idx] + prob_scaled[s_idx] - 1.0
            
            if prob_scaled[l_idx] < 1.0:
                small.append(l_idx)
            else:
                large.append(l_idx)

        while small:
            self.prob[small.popleft()] = 1.0
        while large:
            self.prob[large.popleft()] = 1.0

    def get_random(self):
        
        column_index = random.randrange(self.n)
        coin_toss = random.random()

        if coin_toss < self.prob[column_index]:
            return self.event[column_index]
        else:
            return self.event[self.a[column_index]]

