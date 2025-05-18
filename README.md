
# 📊 Social Media User Behavior Dashboard

This Streamlit app provides a visual and interactive analysis of social media user behavior based on a CSV file extracted from a ZIP archive. It helps uncover insights related to platform usage, income and age groups, device preferences, and behavioral metrics like addiction levels and productivity loss.

---

## 🚀 Features

- ✅ Upload and analyze a ZIP file containing a CSV dataset
- ✅ Auto-categorization of users into `IncomeGroup` and `AgeGroup`
- ✅ Interactive, tab-based visualizations using Seaborn and Matplotlib
- ✅ Clean and modern dashboard UI with tabs for specific insights

---

## 📁 Data Requirements

The uploaded `.zip` file must contain a single `.csv` file with the following columns:

| Column Name         | Description                                       |
|---------------------|---------------------------------------------------|
| `Platform`          | Social media platform used                        |
| `DeviceType`        | Type of device used (e.g., Mobile, Desktop)       |
| `ConnectionType`    | Type of internet connection (e.g., WiFi, Mobile)  |
| `Location`          | User's geographic location                        |
| `Income`            | User's income level (numeric)                     |
| `Age`               | User's age (numeric)                              |
| `Watch Reason`      | Reason for watching content (e.g., Entertainment) |
| `Addiction Level`   | Numeric scale of user addiction to platforms      |
| `Self Control`      | Self-reported control level (numeric)             |
| `ProductivityLoss`  | Self-reported productivity loss (numeric)         |

---

## 🧮 Automatic Grouping

- **IncomeGroup**:
  - Low: ₹0 - ₹20,000
  - Mid: ₹20,001 - ₹50,000
  - High: ₹50,001 - ₹80,000
  - Very High: ₹80,001 - ₹150,000

- **AgeGroup**:
  - 10s: 10-20
  - 20s: 21-30
  - 30s: 31-40
  - 40s: 41-50
  - 50s: 51-60
  - 60s: 61-70

---

## 📊 Dashboard Tabs

The dashboard includes the following tabs for analysis:

1. **Platform vs Device Type** – Compare social media platform usage across different device types
2. **Connection Type by Location** – Visualize internet connection preferences by region
3. **Platform vs Income Group** – Study how income affects platform preference
4. **Watch Reason by Platform** – Analyze motivations behind content consumption
5. **Addiction by Age Group** – View addiction trends across different age categories
6. **Self Control vs Productivity Loss** – Examine the relationship between discipline and productivity

---

## 🛠 Installation

1. **Clone the repository** (or create your own `app.py` file using the Streamlit code):

```bash
git clone https://github.com/yourusername/socialmedia-dashboard.git
cd socialmedia-dashboard
```

2. **Install dependencies**:

```bash
pip install streamlit pandas matplotlib seaborn
```

3. **Run the Streamlit app**:

```bash
streamlit run app.py
```

4. **Upload your `socialmedia.zip` file** when prompted.

---

## 📦 File Structure

```
.
├── app.py               # Main Streamlit app script
├── README.md            # Documentation
└── socialmedia.zip      # (Uploaded via UI) Contains user behavior CSV
```

---

## 📌 Sample Code Preview

```python
df['IncomeGroup'] = pd.cut(df['Income'], bins=[0, 20000, 50000, 80000, 150000], labels=['Low', 'Mid', 'High', 'Very High'])
df['AgeGroup'] = pd.cut(df['Age'], bins=[10, 20, 30, 40, 50, 60, 70], labels=['10s', '20s', '30s', '40s', '50s', '60s'])
```

---

## 📍 Use Cases

- Social media trend research
- Marketing segmentation and targeting
- Behavioral analysis for academic or business purposes

---

## 🧠 Insights You Can Gain

- How younger or older users behave on different platforms
- Which income groups prefer specific social networks
- Whether people with less self-control suffer greater productivity loss
- How device and internet type affect platform engagement

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Questions?

Feel free to reach out or raise an issue if you need support integrating your data or customizing the dashboard!
