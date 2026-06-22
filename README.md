# House Price Predictor

A Streamlit web app that estimates house prices from property details using a trained **Linear Regression** model. Enter dimensions, amenities, and furnishing status in the sidebar to get an instant price prediction in INR.

**Live app:** [houseprice-predictor-model.streamlit.app](https://houseprice-predictor-model.streamlit.app/)

## Features

- Interactive sidebar for property inputs (area, bedrooms, bathrooms, stories)
- Toggle amenities such as main road access, parking, air conditioning, and more
- Furnishing status selection (furnished, semi-furnished, unfurnished)
- Real-time price estimate with price-per-square-foot metric
- Responsive UI with custom styling

## Tech Stack

- **Python** — core language
- **Streamlit** — web interface
- **scikit-learn** — machine learning model
- **joblib** — model serialization and loading
- **pandas** — input preprocessing

## Project Structure

```
.
├── app.py                              # Streamlit application
├── linear_regression_model.joblib      # Trained model
├── requirements.txt                    # Python dependencies
└── README.md
```

## Input Features

The model uses the following features:

| Feature | Type |
| --- | --- |
| Area (sq ft) | Numeric |
| Bedrooms | Numeric |
| Bathrooms | Numeric |
| Stories | Numeric |
| Main road access | Binary |
| Guest room | Binary |
| Basement | Binary |
| Hot water heating | Binary |
| Air conditioning | Binary |
| Parking | Binary |
| Preferred area | Binary |
| Furnishing status | Categorical (semi-furnished / unfurnished) |

## Local Setup

### Prerequisites

- Python 3.11 or 3.12 recommended
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Prshant-kumar1/-House-Price-Predictor.git
cd -House-Price-Predictor
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install streamlit pandas
```

4. Run the app:

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Usage

1. Open the app in your browser.
2. Enter property details in the **Property Details** sidebar.
3. Click **PREDICT PRICE**.
4. View the estimated property value and price per square foot.

## Deployment (Streamlit Community Cloud)

This app is deployed on [Streamlit Community Cloud](https://share.streamlit.io/).

1. Push the repository to GitHub.
2. Connect the repo on Streamlit Cloud.
3. Set the main file to `app.py`.
4. In **Advanced settings**, select **Python 3.12** (recommended).
5. Deploy.

Streamlit installs `streamlit`, `pandas`, and `numpy` by default. This project adds `joblib` and `scikit-learn` via `requirements.txt`.

## Model

The app loads a pre-trained linear regression model from `linear_regression_model.joblib`. The model was trained on historical housing data and predicts price based on the property features listed above.

## License

This project is open source and available for learning and portfolio use.
