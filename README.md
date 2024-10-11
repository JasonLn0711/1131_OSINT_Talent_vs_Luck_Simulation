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
- `experiement_talent_vs_luck__v2_1`: A Jupyter Notebook that contains the full simulation code, step-by-step explanations, and visualizations that highlight the impact of luck on success.
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

## Alternative Method for Using the Simulation

### Requirements
To run this simulation, you’ll need the following Python packages:
- `numpy`
- `matplotlib`
- `pandas` (optional, for extended data analysis)

You can install these packages using pip:
```bash
pip install numpy matplotlib pandas
```

### Running the Simulation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/JasonLn0711/Talent_vs_Luck_Simulation.git
   ```
2. Open the Jupyter Notebook file `experiement_talent_vs_luck__v2_1.ipynb`:
   ```bash
   jupyter notebook experiement_talent_vs_luck__v2_1.ipynb
   ```
3. Follow the instructions in the notebook to run each cell, which will guide you through the simulation process and generate visualizations of the results.

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

## Insights on Investment Scams

The simulation provides a powerful illustration of how people might misinterpret random success as skill. Here’s why this is important in the context of investment scams:
- **Misattribution of Success**: The simulation shows that success is often mistakenly attributed to skill alone, even when luck plays a significant role. Scammers take advantage of this by constructing narratives of inevitable success to deceive investors.
- **Narrative Fallacy**: Many people fall for scams because they believe in a simplified story of talent and success, not realizing how much luck affects outcomes. The notebook includes examples of this fallacy, explaining how it leads to scams.
- **Practical Advice**: By understanding the results of this simulation, you’ll be better equipped to recognize the warning signs of fake investment schemes.

## Future Work
- Explore alternative distributions of talent and events to see how they impact success.
- Integrate additional data analysis to identify how specific parameters influence the outcome.

## Contributing
If you’d like to contribute to this project, please fork the repository and make a pull request. All contributions are welcome!

## License

This project is open-source and licensed under the NYCU License. You are free to use, modify, and distribute the code as long as you include attribution to the original paper and this project.

## Acknowledgments

Thanks to A. Pluchino, A. E. Biondo, and A. Rapisarda for their research on the role of randomness in success. This project aims to bring those insights to a wider audience and promote awareness about investment scams.

---


---


# 模擬市民：天賦與運氣模擬 及 投資詐騙

本專案是以 Python 實現的模擬程式，是一項國立陽明交通大學學生的課程作業，本案靈感源自於 A. Pluchino、A. E. Biondo 和 A. Rapisarda 的論文 [*Talent vs Luck: The Role of Randomness in Success and Failure*](https://arxiv.org/abs/1802.07068) 所提出的概念，旨在呈現並推演出成功受天賦與運氣共同影響的情況，並說明為什麼人們常常會被投資詐騙所欺騙。

## 專案概述

在此專案中，您將看到：
1. 天賦與運氣模型的 Python 實作，模擬隨機性與天賦如何在長期內影響成功。
2. 對人們為何容易陷入投資詐騙的探討，透過此模型來演示。
3. 視覺化呈現說明，為何表面上的成功往往與運氣相關，而非純粹技能，並解析詐騙者如何利用這些錯覺。

## 專案內容

- `talent_vs_luck_simulation.py`： Python 主程式，運行模擬並呈現天賦與運氣如何交互影響。
- `requirements.txt`：列出運行 Python 程式所需的懶人包，一些簡單的 library 。
- `README.md`：說明專案簡介。
- `experiement_talent_vs_luck__v2_1.ipynb`：Jupyter Notebook，包含完整的程式碼、步驟解說及顯示運氣影響成功的視覺化圖表。
- **視覺化呈現**：主程式會生成多張圖表，說明天賦分佈、財富累積以及運氣對成功的影響。

## 本專案與投資詐騙可能存在的關聯

### 功利主義的幻覺

論文指出，成功常常被單純歸因於個人的天賦和努力，這種觀點被稱為「天真的（或過於簡化的）功利主義」。事實上，運氣提供了重要影響。詐騙者利用這一錯誤認知，假裝他們的成功來自於專業的理財技能，而隱藏運氣或甚至欺騙在其中扮演的角色。

### 為何人們會被詐騙

1. **錯誤歸因成功**：人們常常將運氣誤認為技能。在投資詐騙中，詐騙集團透過塑造「保證成功」的故事來利用這一點，讓人們誤以為他們的方法毫無懸念且萬無一失。
2. **敘事謬誤**：人們往往會圍繞成功創造出令人信服的故事，忽略了運氣的角色。這使得詐騙話術（通常承諾穩定且高回報）更容易被相信。
3. **運氣對財務成功的影響**：透過模擬運氣對成功的影響，本專案呈現了為何追隨看似成功的投資者可能會被誤導。這樣的成功或許更與身處對的時間與地點有關，而非真正的技能。

## 運行程式

### 先決條件

請確保您已安裝 Python 3.x，並且安裝 `requirements.txt` 中列出的懶人包：

```bash
pip install -r requirements.txt
```

### 運行模擬

運行模擬並生成圖表，請執行：

```bash
python talent_vs_luck_simulation.py
```

## 運行程式的替代方法

### 所需條件

為了運行此模擬，您需要安裝以下 Python 套件：
- `numpy`
- `matplotlib`
- `pandas`（可選，用於更深入的數據分析）

您可以使用 pip 安裝這些套件：

```bash
pip install numpy matplotlib pandas
```

### 運行模擬

1. 將此資料庫複製到您的用戶端：
   ```bash
   git clone https://github.com/JasonLn0711/Talent_vs_Luck_Simulation.git
   ```
2. 打開 Jupyter Notebook 文件 `experiement_talent_vs_luck__v2_1.ipynb`：
   ```bash
   jupyter notebook experiement_talent_vs_luck__v2_1.ipynb
   ```
3. 按照 notebook 中的指示逐步運行每個 code cell，本程式將引導您完成模擬過程並生成視覺化結果。

### 輸出

此程式碼將生成多張圖表，包括：
- 每個人的天賦分佈。
- 模擬後每個人的最終財富（資本）分佈。
- 天賦與最終財富之間的關聯（或缺乏關聯）。
- 顯示每個人如何受到幸運與不幸事件影響的視覺化圖表。

## 主要收穫

- **提高警覺**：了解成功受隨機性影響，您可以更清楚地認識到追隨「保證」投資方案的風險。
- **批判性思考**：時刻質疑成功故事中忽略運氣或隨機性角色的說法。
- **投資詐騙**：警惕那些保證高回報而未提及風險的個人。真正的投資包含不確定性，成功故事不總是由技能驅動。

## 關於投資詐騙的見解

此程式模擬了人們可能將隨機的成功誤認為是專業理財技能的情形。以下是為何這在投資詐騙背景下十分重要：
- **錯誤歸因成功**：模擬顯示，成功常常被錯誤地完全歸因於技能，即使運氣扮演著重大角色。詐騙者利用這一點，藉由構建不可避免成功的故事來欺騙投資者。
- **敘事謬誤**：許多人會陷入詐騙，因為他們相信簡單化的天賦與成功故事，而未認識到運氣對結果的影響。notebook 包含此謬誤的範例，解釋其如何導致詐騙。
- **實用建議**：透過理解此模擬結果，您將更有能力識別假投資詐騙的警示訊號。

## 未來展望

- 探索天賦和事件的替代分佈，以了解它們對成功的影響。
- 整合額外的數據分析，以識別特定參數如何影響結果。

## 貢獻

如果您想為此專案做出貢獻，請在此資料庫下分支並提交 pull request。歡迎各位先進提供更加優化的版本！

## 授權

本專案為開源專案，並以 NYCU License 授權。您可以在對原始論文和本專案的合理引用的前提下，自由使用、修改和分支此程式碼。

## 致謝

感謝 A. Pluchino、A. E. Biondo 和 A. Rapisarda 對於成功隨機性角色的研究。本專案旨在將這些見解帶給更廣大的觀眾，並推廣對投資詐騙的防範意識。

---
