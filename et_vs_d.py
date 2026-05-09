import random
import math
import matplotlib.pyplot as plt

# =====================================================
# FIXED PARAMETERS
# =====================================================

C = 100
speed = 1

# Fixed reversal probability
p_reverse = 0.3

meeting_threshold = 1

max_steps_per_trial = 2000

num_trials = 200

# Different minimum turning distances D
D_values = list(range(1, 101, 5))

expected_times = []

# =====================================================
# FUNCTION TO RUN ONE SIMULATION
# =====================================================

def run_simulation(min_distance_before_turn):

    # Random initial conditions
    pos1 = random.uniform(0, C)
    pos2 = random.uniform(0, C)

    dir1 = random.choice([1, -1])
    dir2 = random.choice([1, -1])

    since_turn1 = 0
    since_turn2 = 0

    for step in range(max_steps_per_trial):

        # -----------------------------------------
        # Direction reversal logic
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

for D in D_values:

    results = []

    for _ in range(num_trials):

        meeting_time = run_simulation(D)

        results.append(meeting_time)

    E_T = sum(results) / len(results)

    expected_times.append(E_T)

    print(f"D = {D:3d}   E[T] = {E_T:.2f}")

# =====================================================
# PLOT E[T] vs D
# =====================================================

plt.figure(figsize=(8,5))

plt.plot(D_values, expected_times, marker='o')

plt.xlabel("Minimum Distance Before Turning (D)")
plt.ylabel("Expected Meeting Time E[T]")

plt.title("Expected Meeting Time vs Minimum Turning Distance")

plt.grid(True)

plt.show()