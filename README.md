# 💰 Expense Tracker 2.0

A powerful, yet simple Personal Expense Tracker built with **Streamlit** and **SQLite**. Track your spending, manage budgets, and visualize your financial health with ease.

---

## 🚀 Features

- **📊 Interactive Dashboard**: Real-time visualization of your spending habits using Plotly.
- **➕ Easy Expense Logging**: Quickly add new transactions with categories, subcategories, and payment methods.
- **📅 Monthly Budgets**: Set and monitor budgets for different categories to stay on track.
- **📂 Data Management**: Upload existing transaction data via CSV.
- **📋 Detailed Reports**: Generate comprehensive reports to analyze your financial history.
- **⚙️ Customization**: Configure categories and settings to match your personal needs.

## 🛠️ Tech Stack

- **Frontend/App Framework**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Visualization**: [Plotly](https://plotly.com/python/)
- **Database**: SQLite
- **Language**: Python 3.x

## 🏁 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Expense-Tracker-2.0.git
   cd Expense-Tracker-2.0
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the Expense Tracker, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📁 Project Structure

```text
Expense-Tracker-2.0/
├── app.py              # Main application entry point
├── database.py         # SQLite database operations
├── requirements.txt    # Project dependencies
├── components/         # UI components for different pages
│   ├── dashboard.py    # Main dashboard view
│   ├── add_expense.py  # Form for adding expenses
│   ├── reports.py      # Detailed analysis reports
│   └── ...
├── data/               # Local database storage (created on first run)
└── utils/              # Helper functions and utilities
```

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---
*Created with ❤️ by Eric Sena*
