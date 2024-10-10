import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
num_agents = 1000
num_events = 500
event_probability = 0.5  # 50% chance of lucky or unlucky event
initial_capital = 10
simulation_years = 40
time_steps = simulation_years * 2  # every 6 months
grid_size = (201, 201)
num_runs = 100  # For multiple runs analysis

# Initialize lists to store results
capitals_multi_run = []  # To store final capitals for each run

# Define simulation function
def run_simulation():
    global capitals, event_positions, agent_positions
    # Initialize agent attributes and positions
    capitals = np.full(num_agents, initial_capital)
    agent_positions = np.random.randint(0, grid_size[0], (num_agents, 2))
    talents = np.clip(np.random.normal(loc=0.6, scale=0.1, size=num_agents), 0, 1)
    time_series_capitals = {agent: [initial_capital] for agent in range(num_agents)}

    # Initialize event positions and types
    event_positions = np.random.randint(0, grid_size[0], (num_events, 2))
    event_types = np.random.choice(['lucky', 'unlucky'], size=num_events, p=[event_probability, 1 - event_probability])

    # Run the simulation over defined time steps
    for step in range(time_steps):
        moves = np.random.randint(-1, 2, event_positions.shape)
        event_positions = (event_positions + moves) % grid_size[0]  # Ensure events stay within grid

        # Check interactions between agents and events
        for i, (x, y) in enumerate(event_positions):
            agent_indices = np.where((agent_positions == [x, y]).all(axis=1))[0]
            for agent_index in agent_indices:
                if event_types[i] == 'lucky' and np.random.rand() < talents[agent_index]:
                    capitals[agent_index] *= 2
                elif event_types[i] == 'unlucky':
                    capitals[agent_index] /= 2

        # Record capital evolution
        for agent in range(num_agents):
            time_series_capitals[agent].append(capitals[agent])

    return capitals, talents, time_series_capitals

# Run and store results for multiple runs
for run in range(num_runs):
    capitals, talents, _ = run_simulation()
    capitals_multi_run.append(list(capitals))

# Visualization Functions

# 1. Talent Distribution (Figure 2)
def plot_talent_distribution(talents):
    plt.figure(figsize=(8, 6))
    plt.hist(talents, bins=30, color='skyblue', edgecolor='black', density=True)
    plt.axvline(np.mean(talents), color='red', linestyle='dashed', linewidth=2, label='Mean')
    plt.title("Normal Distribution of Talent")
    plt.xlabel("Talent")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

# 2. Distribution of Final Capital (Figure 3)
def plot_final_capital_distribution(capitals):
    plt.figure(figsize=(8, 6))
    plt.hist(capitals, bins=30, color='skyblue', edgecolor='black', log=True)
    plt.title("Distribution of Final Capital")
    plt.xlabel("Final Capital")
    plt.ylabel("Number of Agents (log scale)")
    plt.show()

# 3. Talent vs Final Capital (Figure 4)
def plot_talent_vs_capital(talents, capitals):
    plt.figure(figsize=(8, 6))
    plt.scatter(talents, capitals, color='purple', alpha=0.6)
    plt.title("Talent vs Final Capital")
    plt.xlabel("Talent")
    plt.ylabel("Final Capital")
    plt.show()

# 4. Distribution of Capitals Across Multiple Runs (Figure 7)
def plot_multi_run_capital_distribution(capitals_multi_run):
    plt.figure(figsize=(8, 6))
    for run_capitals in capitals_multi_run[:5]:
        plt.hist(run_capitals, bins=30, alpha=0.3, color='skyblue', edgecolor='black', log=True)
    plt.title("Distribution of Capital Across Multiple Runs")
    plt.xlabel("Final Capital")
    plt.ylabel("Frequency (log scale)")
    plt.show()

# 5. Capital Evolution Over Time for Sample Agents (Figure 6)
def plot_capital_evolution(time_series_capitals):
    plt.figure(figsize=(12, 6))
    for agent in range(5):  # Sample first 5 agents
        plt.plot(time_series_capitals[agent], label=f'Agent {agent}')
    plt.xlabel("Time Steps (6 months each)")
    plt.ylabel("Capital")
    plt.title("Capital Evolution Over Time for Sample Agents")
    plt.legend()
    plt.show()

# Run a single simulation for visualization
capitals, talents, time_series_capitals = run_simulation()

# Generate and display plots
plot_talent_distribution(talents)
plot_final_capital_distribution(capitals)
plot_talent_vs_capital(talents, capitals)
plot_multi_run_capital_distribution(capitals_multi_run)
plot_capital_evolution(time_series_capitals)

