import random
import math
import matplotlib.pyplot as plt

# =====================================================
# PARAMETERS
# =====================================================

C = 100
speed = 1

min_distance_before_turn = 20

meeting_threshold = 1

max_steps_per_trial = 2000

num_trials = 200

# Different reversal probabilities to test
p_values = [i / 20 for i in range(1, 20)]

expected_times = []

# =====================================================
# FUNCTION TO RUN ONE SIMULATION
# =====================================================

def run_simulation(p_reverse):

    # Random initial conditions
    pos1 = random.uniform(0, C)
    pos2 = random.uniform(0, C)

    dir1 = random.choice([1, -1])
    dir2 = random.choice([1, -1])

    since_turn1 = 0
    since_turn2 = 0

    for step in range(max_steps_per_trial):

        # -----------------------------------------
        # Reversal rules
        # -----------------------------------------

        if since_turn1 >= min_distance_before_turn:

            if random.random() < p_reverse:
                dir1 *= -1
                since_turn1 = 0

        if since_turn2 >= min_distance_before_turn:

            if random.random() < p_reverse:
                dir2 *= -1
                since_turn2 = 0

        # -----------------------------------------
        # Move walkers
        # -----------------------------------------

        pos1 = (pos1 + dir1 * speed) % C
        pos2 = (pos2 + dir2 * speed) % C

        since_turn1 += speed
        since_turn2 += speed

        # -----------------------------------------
        # Circular distance
        # -----------------------------------------

        d = abs(pos1 - pos2)
        circular_distance = min(d, C - d)

        # -----------------------------------------
        # Meeting condition
        # -----------------------------------------

        if circular_distance < meeting_threshold:
            return step

    return max_steps_per_trial


# =====================================================
# MONTE CARLO EXPERIMENT
# =====================================================

for p in p_values:

    results = []

    for _ in range(num_trials):

        meeting_time = run_simulation(p)

        results.append(meeting_time)

    E_T = sum(results) / len(results)

    expected_times.append(E_T)

    print(f"p = {p:.2f}   E[T] = {E_T:.2f}")

# =====================================================
# PLOT E[T] vs p
# =====================================================

plt.figure(figsize=(8,5))

plt.plot(p_values, expected_times, marker='o')

plt.xlabel("Reversal Probability p")
plt.ylabel("Expected Meeting Time E[T]")

plt.title("Expected Meeting Time vs Reversal Probability")

plt.grid(True)

plt.show()