import random
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================================================
# PARAMETERS
# =====================================================

C = 100
radius = C / (2 * math.pi)

speed = 1

p_reverse = 0.3

min_distance_before_turn = 20

meeting_threshold = 1

max_steps_per_trial = 1000

num_trials = 20

# =====================================================
# STORAGE
# =====================================================

all_positions1 = []
all_positions2 = []
meeting_steps = []

# =====================================================
# RUN MULTIPLE TRIALS
# =====================================================

for trial in range(num_trials):

    # ---------------------------------------------
    # RANDOM INITIAL CONDITIONS
    # ---------------------------------------------

    pos1 = random.uniform(0, C)
    pos2 = random.uniform(0, C)

    dir1 = random.choice([1, -1])
    dir2 = random.choice([1, -1])

    since_turn1 = 0
    since_turn2 = 0

    positions1 = []
    positions2 = []

    meeting_happened = False

    # ---------------------------------------------
    # SIMULATION LOOP
    # ---------------------------------------------

    for step in range(max_steps_per_trial):

        # Walker 1 reversal logic
        if since_turn1 >= min_distance_before_turn:

            if random.random() < p_reverse:
                dir1 *= -1
                since_turn1 = 0

        # Walker 2 reversal logic
        if since_turn2 >= min_distance_before_turn:

            if random.random() < p_reverse:
                dir2 *= -1
                since_turn2 = 0

        # Move walkers
        pos1 = (pos1 + dir1 * speed) % C
        pos2 = (pos2 + dir2 * speed) % C

        since_turn1 += speed
        since_turn2 += speed

        positions1.append(pos1)
        positions2.append(pos2)

        # Circular distance
        d = abs(pos1 - pos2)
        circular_distance = min(d, C - d)

        # Meeting condition
        if circular_distance < meeting_threshold:

            print(f"Trial {trial+1}: Meeting at step {step}")

            meeting_steps.append(step)

            all_positions1.extend(positions1)
            all_positions2.extend(positions2)

            meeting_happened = True
            break

    if not meeting_happened:
        print(f"Trial {trial+1}: No meeting")

# =====================================================
# GRAPHICAL ANIMATION
# =====================================================

fig, ax = plt.subplots(figsize=(7,7))

ax.set_xlim(-radius - 5, radius + 5)
ax.set_ylim(-radius - 5, radius + 5)

ax.set_aspect('equal')

circle = plt.Circle((0,0), radius, fill=False)
ax.add_artist(circle)

walker1_dot, = ax.plot([], [], 'bo', markersize=8, label='Walker 1')
walker2_dot, = ax.plot([], [], 'ro', markersize=8, label='Walker 2')

title = ax.set_title("")

ax.legend()

# =====================================================
# UPDATE FUNCTION
# =====================================================

def update(frame):

    p1 = all_positions1[frame]
    p2 = all_positions2[frame]

    theta1 = 2 * math.pi * p1 / C
    theta2 = 2 * math.pi * p2 / C

    x1 = radius * math.cos(theta1)
    y1 = radius * math.sin(theta1)

    x2 = radius * math.cos(theta2)
    y2 = radius * math.sin(theta2)

    walker1_dot.set_data([x1], [y1])
    walker2_dot.set_data([x2], [y2])

    title.set_text(f"Frame {frame}")

    return walker1_dot, walker2_dot

# =====================================================
# RUN ANIMATION
# =====================================================

ani = FuncAnimation(
    fig,
    update,
    frames=len(all_positions1),
    interval=40,
    blit=True
)

plt.show()

# =====================================================
# FINAL STATISTICS
# =====================================================

if len(meeting_steps) > 0:

    avg_meeting = sum(meeting_steps) / len(meeting_steps)

    print("\n================================")
    print("SIMULATION STATISTICS")
    print("================================")
    print(f"Trials completed: {len(meeting_steps)}")
    print(f"Average meeting step: {avg_meeting:.2f}")