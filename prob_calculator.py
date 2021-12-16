import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        k = list(kwargs.keys())
        v = list(kwargs.values())
        for i in range(len(k)):
            for j in range(v[i]):
                self.contents.append(k[i])
    def draw(self, qty):
        self.qty = qty
        drawn = []
        for i in range(self.qty):
            l = self.contents
            x = random.randint(0, len(l) - 1)
            drawn.append(l[x])
            l.remove(l[x])
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments
    n = 0
    
    for i in range(N):
        drawn = []
    
        for j in range(num_balls_drawn):
            l = list(hat.contents)
            x = random.randint(0, len(l) - 1)
            drawn.append(l[x])
            
        for k in expected_balls:
            if expected_balls[k] <= drawn.count(k):
                n += 1
        if n > 1:
            M += 1
        n = 0

    return (M / N)
