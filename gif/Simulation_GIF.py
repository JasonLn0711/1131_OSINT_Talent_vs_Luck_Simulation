import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# Simulation parameters
grid_size = (201, 201)
num_agents = 1000
num_events = 500
event_probability = 0.5
initial_capital = 100000
simulation_years = 40
time_steps = simulation_years * 2  # every 6 months

# Initialize agents
np.random.seed(0)
talents = np.random.normal(loc=0.6, scale=0.1, size=num_agents)
talents = np.clip(talents, 0, 1)
capitals = np.full(num_agents, initial_capital)

# Initialize agent positions and events
agent_positions = np.random.randint(0, grid_size[0], (num_agents, 2))
event_positions = np.random.randint(0, grid_size[0], (num_events, 2))
event_types = np.random.choice(['lucky', 'unlucky'], size=num_events, p=[event_probability, 1 - event_probability])

# Separate lucky and unlucky events
lucky_events = event_positions[event_types == 'lucky']
unlucky_events = event_positions[event_types == 'unlucky']

# Create a list to store frames for the GIF
frames = []

# Simulation function
def simulate():
    for _ in range(time_steps):
        # Move agents randomly
        movements = np.random.randint(-1, 2, agent_positions.shape)
        agent_positions[:] = (agent_positions + movements) % grid_size[0]
        
        # Detect encounters with events
        for i, pos in enumerate(agent_positions):
            distances = np.linalg.norm(event_positions - pos, axis=1)
            close_event_idx = np.where(distances < 2)
            for idx in close_event_idx[0]:
                if event_types[idx] == 'lucky':
                    capitals[i] *= 1.1
                elif event_types[idx] == 'unlucky':
                    capitals[i] *= 0.9

        # Plot the current state
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, grid_size[0])
        ax.set_ylim(0, grid_size[1])
        ax.scatter(agent_positions[:, 0], agent_positions[:, 1], color='blue', s=10, label='Agents')
        ax.scatter(lucky_events[:, 0], lucky_events[:, 1], color='green', s=50, alpha=0.6, label='Lucky Events')
        ax.scatter(unlucky_events[:, 0], unlucky_events[:, 1], color='red', s=50, alpha=0.6, label='Unlucky Events')
        plt.title('Agent Movement and Event Interactions Over Time')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(False)

        # Save the frame to the frames list
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(image)
        
        plt.close(fig)

# Run the simulation and gather frames
simulate()

from google.colab import drive
drive.mount('/content/drive')

# Save as GIF
imageio.mimsave('/content/drive/MyDrive/Talent_vs_Luck_Simulation.gif', frames, fps=10)

# The GIF file will be saved as 'simulation.gif'
