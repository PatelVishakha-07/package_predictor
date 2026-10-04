# Placement Package Predictor

A small machine learning web app that predicts a student's placement package (in LPA) from their CGPA. It uses **Linear Regression** from scikit-learn for the model and **Flask** for the web interface.

## Features

- Trains a Linear Regression model on placement data (`cgpa` to `package`)
- Evaluates the model with R2 score and Mean Absolute Error (MAE)
- Saves the trained model with `pickle`, so the app doesn't retrain on every request
- Simple web UI: enter a CGPA with a box or slider and get an instant prediction
- Input validation (CGPA must be between 0 and 10)

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3 |
| ML | scikit-learn, pandas |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript (Jinja2 templates) |

## Project Structure

```
package_predictor/
├── app.py                 # Flask backend: loads the model and serves predictions
├── model.py               # Trains the model, prints metrics, saves model.pkl
├── model.pkl              # Saved trained model (created by model.py)
├── placement.csv          # Dataset with 'cgpa' and 'package' columns
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web page (form + result)
└── README.md
```

## How It Works

1. `model.py` reads `placement.csv`, splits the data into 80% training and 20% testing, and trains a Linear Regression model.
2. The model learns a straight line: `package = m x cgpa + b`.
3. R2 and MAE are calculated on the test data, and the trained model is saved to `model.pkl`.
4. `app.py` loads `model.pkl` when it starts. When a user submits a CGPA in the form, Flask validates it, predicts the package and shows the result on the page.

```
Browser (index.html) --> Flask (app.py) --> model.pkl --> prediction --> Browser
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PatelVishakha-07/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Place `placement.csv` in the project folder. It needs these two columns:

| cgpa | package |
|---|---|
| 8.1 | 6.5 |
| 7.2 | 4.8 |

### 4. Train the model

```bash
python model.py
```

This prints the slope, intercept, R2 score and MAE, and creates `model.pkl`. Run it again whenever the dataset or training code changes.

### 5. Start the web app

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser, enter a CGPA and click **Predict Package**.

> If you retrain the model, restart the app so it loads the new `model.pkl`.

## Model Details

- **Algorithm:** Linear Regression (simple, one feature)
- **Input feature:** `cgpa`
- **Target:** `package` (LPA)
- **Train/test split:** 80% / 20%, with `random_state=42` so results are repeatable
- **Metrics:** R2 score and Mean Absolute Error (MAE)

| Metric | Value |
|---|---|
| R2 score | _add your value_ |
| MAE | _add your value_ |
| Slope (m) | _add your value_ |
| Intercept (b) | _add your value_ |

## Limitations

- The model uses only CGPA, so the same CGPA always gives the same prediction. Real packages also depend on skills, projects, internships and interview performance.
- Predictions are estimates from the training data and should not be treated as guaranteed outcomes.
- Results depend on the quality and size of the dataset.

## Future Improvements

- Add more features (projects, internships, skills score) and use multiple linear regression
- Compare other models such as Random Forest
- Use cross-validation for a more reliable accuracy estimate
- Show the regression line chart in the UI
- Deploy the app online (Render, PythonAnywhere)

## Common Issues

| Problem | Fix |
|---|---|
| `TemplateNotFound: index.html` | Keep `index.html` inside a folder named `templates`, next to `app.py`. |
| `FileNotFoundError: model.pkl` | Run `python model.py` first. |
| Old predictions after retraining | Restart `app.py` so it reloads the model. |

## Author

**Vishakha Pareshkumar Patel**
MCA Student, LJ University, Ahmedabad
[GitHub](https://github.com/PatelVishakha-07) | [LinkedIn](https://www.linkedin.com/in/patelvishakha-tech)
