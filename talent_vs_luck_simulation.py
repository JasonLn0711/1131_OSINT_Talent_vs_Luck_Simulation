import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
num_agents = 1000
num_events = 500
event_probability = 0.5  # 50% chance of a lucky or unlucky event
initial_capital = 100000
simulation_years = 40
time_steps = simulation_years * 2  # Every 6 months
grid_size = (201, 201)
num_runs = 50 # For multiple runs analysis
# I cut it down to make it time-efficient; initially, the original experiment ran 100 times instead.


# Initialize lists to store results
capitals_multi_run = []  # To store final capitals for each run

# Define a function to initialize the agents
def initialize_agents():
    capitals = np.full(num_agents, initial_capital)  # Set initial capital for all agents
    talents = np.clip(np.random.normal(0.6, 0.1, num_agents), 0, 1)  # Talent follows a clipped normal distribution
    agent_positions = np.random.randint(0, grid_size[0], (num_agents, 2))  # Random initial positions
    return capitals, talents, agent_positions


# Define a function to initialize events
def initialize_events():
    event_positions = np.random.randint(0, grid_size[0], (num_events, 2))
    event_types = np.random.choice(['lucky', 'unlucky'], size=num_events, p=[event_probability, 1 - event_probability])
    return event_positions, event_types


# Define the simulation function for one run
def run_simulation():
    # Initialize agents and events
    capitals, talents, agent_positions = initialize_agents()
    event_positions, event_types = initialize_events()
    
    # Dictionary to track capital evolution for each agent over time
    capital_evolution = {agent: [initial_capital] for agent in range(num_agents)}

    # Simulation loop over time steps
    for step in range(time_steps):
        # Move events randomly within the grid
        moves = np.random.randint(-1, 2, event_positions.shape)
        event_positions = (event_positions + moves) % grid_size[0]

        # Process interactions between agents and events
        for i, (x, y) in enumerate(event_positions):
            # Find agents located at the same grid position as the event
            agent_indices = np.where((agent_positions == [x, y]).all(axis=1))[0]
            for agent_index in agent_indices:
                if event_types[i] == 'lucky' and np.random.rand() < talents[agent_index]:
                    capitals[agent_index] *= 2  # Successful lucky event doubles capital
                elif event_types[i] == 'unlucky':
                    capitals[agent_index] /= 2  # Unlucky event halves capital

        # Record the current capital for each agent
        for agent in range(num_agents):
            capital_evolution[agent].append(capitals[agent])

    return capitals, talents, capital_evolution

def plot_initial_setup(agent_positions, event_positions, event_types):
    plt.figure(figsize=(10, 10))
    # Plot agents
    plt.scatter(agent_positions[:, 0], agent_positions[:, 1], color='blue', s=10, label='Agents')
    # Plot lucky and unlucky events
    lucky_positions = event_positions[event_types == 'lucky']
    unlucky_positions = event_positions[event_types == 'unlucky']
    plt.scatter(lucky_positions[:, 0], lucky_positions[:, 1], color='green', s=50, alpha=0.6, label='Lucky Events')
    plt.scatter(unlucky_positions[:, 0], unlucky_positions[:, 1], color='red', s=50, alpha=0.6, label='Unlucky Events')
    plt.title("Initial Setup: Agents and Events on the Grid")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.show()

# Define a function to run multiple simulations and store results
def run_multiple_simulations():
    global capitals_multi_run
    for _ in range(num_runs):
        capitals, talents, _ = run_simulation()
        capitals_multi_run.append(list(capitals))  # Store the final capital distribution of each run


# Visualization Functions

# 1. Plot Talent Distribution
def plot_talent_distribution(talents):
    plt.figure(figsize=(10, 6))
    plt.hist(talents, bins=30, color='skyblue', edgecolor='black', density=True)
    plt.axvline(np.mean(talents), color='red', linestyle='dashed', linewidth=2, label='Mean Talent')
    plt.axvline(np.mean(talents) + np.std(talents), color='green', linestyle='dotted', linewidth=2, label='Mean ± 1 SD')
    plt.axvline(np.mean(talents) - np.std(talents), color='green', linestyle='dotted', linewidth=2)
    plt.title("Talent Distribution")
    plt.xlabel("Talent")
    plt.ylabel("Density")
    plt.legend()
    plt.show()


# 2. Plot Final Capital Distribution
def plot_final_capital_distribution(capitals):
    plt.figure(figsize=(10, 6))
    plt.hist(capitals, bins=30, color='skyblue', edgecolor='black', log=True)
    plt.title("Distribution of Final Capital")
    plt.xlabel("Final Capital")
    plt.ylabel("Number of Agents (log scale)")
    plt.show()


# 3. Plot Talent vs Final Capital
def plot_talent_vs_capital(talents, capitals):
    plt.figure(figsize=(10, 6))
    plt.scatter(talents, capitals, color='purple', alpha=0.5)
    plt.title("Talent vs Final Capital")
    plt.xlabel("Talent")
    plt.ylabel("Final Capital")
    plt.show()


# 4. Plot Capital Distribution Across Multiple Runs
def plot_multi_run_capital_distribution():
    plt.figure(figsize=(10, 6))
    for run_capitals in capitals_multi_run[:5]:  # Plot first 5 runs as example
        plt.hist(run_capitals, bins=30, alpha=0.3, color='skyblue', edgecolor='black', log=True)
    plt.title("Distribution of Capital Across Multiple Runs")
    plt.xlabel("Final Capital")
    plt.ylabel("Frequency (log scale)")
    plt.show()


# 5. Plot Capital Evolution Over Time for Sample Agents
def plot_capital_evolution(capital_evolution):
    plt.figure(figsize=(12, 8))
    for agent in range(5):  # Plot for first 5 agents as an example
        plt.plot(capital_evolution[agent], label=f'Agent {agent}')
    plt.xlabel("Time Steps (6 months each)")
    plt.ylabel("Capital")
    plt.title("Capital Evolution Over Time for Sample Agents")
    plt.legend()
    plt.show()

def plot_events_vs_capital(lucky_counts, unlucky_counts, capitals):
    plt.figure(figsize=(12, 5))

    # Plot lucky events vs final capital
    plt.subplot(1, 2, 1)
    plt.scatter(lucky_counts, capitals, color='green', alpha=0.6)
    plt.title("Lucky Events vs Final Capital")
    plt.xlabel("Number of Lucky Events")
    plt.ylabel("Final Capital")

    # Plot unlucky events vs final capital
    plt.subplot(1, 2, 2)
    plt.scatter(unlucky_counts, capitals, color='red', alpha=0.6)
    plt.title("Unlucky Events vs Final Capital")
    plt.xlabel("Number of Unlucky Events")
    plt.ylabel("Final Capital")

    plt.tight_layout()
    plt.show()

# Modify run_simulation to track lucky/unlucky counts
def run_simulation_with_event_count():
    capitals, talents, agent_positions = initialize_agents()
    event_positions, event_types = initialize_events()
    
    # Track lucky/unlucky event counts
    lucky_counts = np.zeros(num_agents)
    unlucky_counts = np.zeros(num_agents)

    for step in range(time_steps):
        moves = np.random.randint(-1, 2, event_positions.shape)
        event_positions = (event_positions + moves) % grid_size[0]

        for i, (x, y) in enumerate(event_positions):
            agent_indices = np.where((agent_positions == [x, y]).all(axis=1))[0]
            for agent_index in agent_indices:
                if event_types[i] == 'lucky':
                    lucky_counts[agent_index] += 1
                    if np.random.rand() < talents[agent_index]:
                        capitals[agent_index] *= 2
                elif event_types[i] == 'unlucky':
                    unlucky_counts[agent_index] += 1
                    capitals[agent_index] /= 2

    return capitals, talents, lucky_counts, unlucky_counts

def plot_top_talent_distribution(talents, capitals, top_percent=0.1):
    top_n = int(num_agents * top_percent)
    top_agents = np.argsort(capitals)[-top_n:]  # Get indices of top agents by capital
    top_talents = talents[top_agents]

    plt.figure(figsize=(8, 6))
    plt.hist(top_talents, bins=20, color='skyblue', edgecolor='black', density=True)
    plt.title(f"Talent Distribution of Top {top_percent*100:.0f}% Most Successful Agents")
    plt.xlabel("Talent")
    plt.ylabel("Density")
    plt.show()

def plot_success_path(capital_evolution, most_successful_idx):
    plt.figure(figsize=(10, 6))
    plt.plot(capital_evolution[most_successful_idx], color='purple')
    plt.title("Capital Evolution of a Highly Successful Individual")
    plt.xlabel("Time Steps (6 months each)")
    plt.ylabel("Capital")
    plt.show()

# Main Execution Section
# Run multiple simulations for final capital analysis
run_multiple_simulations()

# Run a single simulation for visualizations
capitals, talents, capital_evolution = run_simulation()

# Run the initialization to get positions and event types
_, _, agent_positions = initialize_agents()
event_positions, event_types = initialize_events()
plot_initial_setup(agent_positions, event_positions, event_types) # Figure 1

# Generate visualizations
plot_talent_distribution(talents)  # Figure 2 equivalent
plot_final_capital_distribution(capitals)  # Figure 3 equivalent
plot_talent_vs_capital(talents, capitals)  # Figure 4 equivalent
plot_capital_evolution(capital_evolution)  # Figure 6 equivalent
plot_multi_run_capital_distribution()  # Figure 7 equivalent

# Run simulation with event count tracking
capitals, talents, lucky_counts, unlucky_counts = run_simulation_with_event_count()
plot_events_vs_capital(lucky_counts, unlucky_counts, capitals) # Figure 5

# Plot the talent distribution of the top 10% successful agents
plot_top_talent_distribution(talents, capitals, top_percent=0.1) # Figure 8

# Identify the most successful agent and plot their capital evolution
most_successful_idx = np.argmax(capitals)
plot_success_path(capital_evolution, most_successful_idx) # Figure 9

