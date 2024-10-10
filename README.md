# Talent vs Luck Simulation and Investment Scam Awareness

This project is a Python simulation developed as a student assignment at NYCU, based on the concepts presented in the paper ["Talent vs Luck: The Role of Randomness in Success and Failure"](https://arxiv.org/abs/1802.07068) by A. Pluchino, A. E. Biondo, and A. Rapisarda. It aims to demonstrate how success is influenced by both talent and luck, with implications on why people are often deceived by fake investment scams.

## Project Overview

In this project, you will find:
1. A Python implementation of the "Talent vs Luck" model, simulating how randomness and talent impact success over time.
2. An exploration of why people frequently fall for investment scams, illustrated through the lens of this model.
3. Visualizations that demonstrate how perceived success can often be attributed more to luck than to skill, shedding light on how scammers manipulate these perceptions.

## Contents

- `talent_vs_luck_simulation.py`: The main Python script that runs the simulation, showing how talent and luck interact to produce success.
- `requirements.txt`: Lists the dependencies required to run the Python code.
- `README.md`: This file, providing an overview of the project.
- **Visualizations**: The script produces multiple figures, illustrating the distribution of talent, wealth accumulation, and the impact of luck on success.

## How the Project Relates to Investment Scams

### The Illusion of Meritocracy

The paper demonstrates that success is often incorrectly attributed solely to personal talent and effort, a concept known as the "naive meritocracy." In reality, luck plays a significant role. Scammers take advantage of this misconception by presenting themselves as successful due to skill, hiding the role of luck or even deception in their apparent achievements.

### Why People Are Deceived by Scams

1. **Misattribution of Success**: People often mistake luck for skill. In investment scams, fraudsters exploit this by crafting narratives of guaranteed success, implying that their methods are foolproof.
2. **Narrative Fallacy**: Humans tend to create compelling stories around success, ignoring the role of chance. This makes scam narratives, which promise consistent, high returns, more believable.
3. **The Power of Luck in Financial Success**: By simulating how luck influences success, this project illustrates why following seemingly successful investors can be misleading. Success in these cases may be more about being in the right place at the right time than genuine skill.

## Running the Code

### Prerequisites

Make sure you have Python 3.x installed. You will also need to install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Simulation

To run the simulation and generate the figures, execute:

```bash
python talent_vs_luck_simulation.py
```

This script will:
- Simulate multiple agents over a period of time, exposing them to random lucky and unlucky events.
- Record and visualize the evolution of their wealth.
- Illustrate how luck can often outweigh talent in determining who becomes the wealthiest.

### Output

The script will generate several figures, including:
- The distribution of talent among agents.
- The distribution of final capital (wealth) across agents after the simulation.
- The correlation (or lack thereof) between talent and final wealth.
- Visual representations of how agents are impacted by random events, both lucky and unlucky.

## Key Takeaways

- **Awareness**: By understanding that success is influenced by randomness, you can better recognize the risks of following "guaranteed" investment schemes.
- **Critical Thinking**: Always question narratives of success that omit the role of luck or randomness.
- **Investment Scams**: Be wary of anyone promising certain returns with no mention of risk. Real investment involves uncertainty, and success stories are not always due to skill.

## License

This project is open-source and licensed under the NYCU License. You are free to use, modify, and distribute the code as long as you include attribution to the original paper and this project.

## Acknowledgments

Thanks to A. Pluchino, A. E. Biondo, and A. Rapisarda for their research on the role of randomness in success. This project aims to bring those insights to a wider audience and promote awareness about investment scams.

---
