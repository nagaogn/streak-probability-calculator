import numpy as np

def simulate(p=0.35, n=20000, m=10, trials=100000):
    count = 0
    for _ in range(trials):
        results = np.random.choice([0, 1], size=n, p=[1-p, p]) # 0: lose, 1: win
        win_streak = 0
        for result in results:
            if result == 1:
                win_streak += 1
                if win_streak >= m:
                    count += 1
                    break
            else:
                win_streak = 0
    return count / trials

print(f"Probability: {simulate()}")