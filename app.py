import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced custom CSS
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 500;
    }
    
    /* Content card */
    .content-card {
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
    }
    
    /* Header */
    .hero-header {
        text-align: center;
        padding: 2rem 0;
        background: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #666;
        font-weight: 300;
    }
    
    /* Prediction result box */
    .prediction-result {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        margin: 2rem 0;
    }
    
    .prediction-label {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .prediction-price {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .prediction-subtext {
        font-size: 1rem;
        opacity: 0.8;
        font-weight: 300;
    }
    
    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .feature-item {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        transition: transform 0.3s;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-label {
        font-size: 0.9rem;
        color: #666;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    
    .feature-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2c3e50;
    }
    
    /* Amenities section */
    .amenities-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .amenity-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 500;
        font-size: 0.9rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .amenity-badge-inactive {
        background: #e0e0e0;
        color: #999;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    /* Metrics */
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    /* Info box */
    .info-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #ff6b6b;
        margin: 2rem 0;
    }
    
    .info-text {
        color: #d63031;
        font-weight: 500;
        font-size: 1.1rem;
        margin: 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(245, 87, 108, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Load model with error handling
@st.cache_resource
def load_model():
    try:
        return joblib.load('linear_regression_model.joblib')
    except FileNotFoundError:
        st.error("⚠️ Model file not found! Please ensure 'linear_regression_model.joblib' exists.")
        st.stop()
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        st.stop()

model = load_model()

# Define columns
original_columns = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
                    'basement', 'hotwaterheating', 'airconditioning', 'parking',
                    'prefarea', 'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished']

# Hero Header
st.markdown("""
    <div class="hero-header">
        <div class="hero-title">🏠 House Price Predictor</div>
        <div class="hero-subtitle">Get accurate property valuations powered by machine learning</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.markdown("<h2 style='color: white; text-align: center; margin-bottom: 2rem;'>⚙️ Property Details</h2>", unsafe_allow_html=True)

st.sidebar.markdown("<h3 style='color: #ffd700; margin-top: 1rem;'>📐 Dimensions</h3>", unsafe_allow_html=True)
area = st.sidebar.number_input('Area (sq ft)', min_value=1000, max_value=20000, value=5000, step=100)
bedrooms = st.sidebar.slider('Bedrooms', min_value=1, max_value=10, value=3)
bathrooms = st.sidebar.slider('Bathrooms', min_value=1, max_value=5, value=2)
stories = st.sidebar.slider('Stories', min_value=1, max_value=4, value=2)

st.sidebar.markdown("<h3 style='color: #ffd700; margin-top: 1.5rem;'>✨ Features</h3>", unsafe_allow_html=True)
mainroad = st.sidebar.checkbox('Main Road Access', value=True)
guestroom = st.sidebar.checkbox('Guest Room', value=False)
basement = st.sidebar.checkbox('Basement', value=False)
hotwaterheating = st.sidebar.checkbox('Hot Water Heating', value=False)
airconditioning = st.sidebar.checkbox('Air Conditioning', value=True)
parking = st.sidebar.checkbox('Parking', value=True)
prefarea = st.sidebar.checkbox('Preferred Area', value=False)

st.sidebar.markdown("<h3 style='color: #ffd700; margin-top: 1.5rem;'>🛋️ Furnishing</h3>", unsafe_allow_html=True)
furnishingstatus = st.sidebar.selectbox('Status', ['furnished', 'semi-furnished', 'unfurnished'], index=1)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
predict_button = st.sidebar.button('🔮 PREDICT PRICE', use_container_width=True)

# Main content
st.markdown('<div class="content-card">', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="section-header">📊 Property Overview</div>', unsafe_allow_html=True)
    
    # Feature cards
    st.markdown("""
        <div class="feature-grid">
            <div class="feature-item">
                <div class="feature-icon">📏</div>
                <div class="feature-label">Area</div>
                <div class="feature-value">{:,}</div>
                <div style="font-size: 0.8rem; color: #888;">sq ft</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🛏️</div>
                <div class="feature-label">Bedrooms</div>
                <div class="feature-value">{}</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🚿</div>
                <div class="feature-label">Bathrooms</div>
                <div class="feature-value">{}</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🏢</div>
                <div class="feature-label">Stories</div>
                <div class="feature-value">{}</div>
            </div>
        </div>
    """.format(area, bedrooms, bathrooms, stories), unsafe_allow_html=True)
    
    # Amenities
    st.markdown('<div class="section-header" style="margin-top: 2rem;">🌟 Amenities & Features</div>', unsafe_allow_html=True)
    
    amenities_html = '<div class="amenities-grid">'
    amenities_list = [
        ("🛣️ Main Road", mainroad),
        ("🏠 Guest Room", guestroom),
        ("🔽 Basement", basement),
        ("♨️ Hot Water", hotwaterheating),
        ("❄️ Air Conditioning", airconditioning),
        ("🚗 Parking", parking),
        ("⭐ Preferred Area", prefarea)
    ]
    
    for amenity_name, is_active in amenities_list:
        badge_class = "amenity-badge" if is_active else "amenity-badge-inactive"
        amenities_html += f'<div class="{badge_class}">{amenity_name}</div>'
    
    amenities_html += '</div>'
    st.markdown(amenities_html, unsafe_allow_html=True)
    
    # Furnishing status
    furnish_color = {"furnished": "#2ecc71", "semi-furnished": "#f39c12", "unfurnished": "#95a5a6"}
    st.markdown(f"""
        <div style="margin-top: 1.5rem; padding: 1rem; background: {furnish_color[furnishingstatus]}20; 
                    border-radius: 10px; border-left: 5px solid {furnish_color[furnishingstatus]};">
            <strong style="color: {furnish_color[furnishingstatus]}; font-size: 1.1rem;">
                🛋️ Furnishing: {furnishingstatus.capitalize()}
            </strong>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-header">💰 Price Estimation</div>', unsafe_allow_html=True)
    
    if predict_button:
        # Prepare input data
        input_data = {
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'stories': stories,
            'mainroad': 1 if mainroad else 0,
            'guestroom': 1 if guestroom else 0,
            'basement': 1 if basement else 0,
            'hotwaterheating': 1 if hotwaterheating else 0,
            'airconditioning': 1 if airconditioning else 0,
            'parking': 1 if parking else 0,
            'prefarea': 1 if prefarea else 0,
            'furnishingstatus_semi-furnished': 1 if furnishingstatus == 'semi-furnished' else 0,
            'furnishingstatus_unfurnished': 1 if furnishingstatus == 'unfurnished' else 0
        }
        
        input_df = pd.DataFrame([input_data])[original_columns]
        
        try:
            predicted_price = model.predict(input_df)[0]
            
            # Display prediction
            st.markdown(f"""
                <div class="prediction-result">
                    <div class="prediction-label">Estimated Property Value</div>
                    <div class="prediction-price">₹ {predicted_price:,.0f}</div>
                    <div class="prediction-subtext">Based on current market analysis</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Price per sqft metric
            price_per_sqft = predicted_price / area
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Price per Square Foot</div>
                    <div class="metric-value">₹ {price_per_sqft:,.0f}</div>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Prediction error: {str(e)}")
    else:
        st.markdown("""
            <div class="info-box">
                <p class="info-text">👈 Configure your property details in the sidebar and click "PREDICT PRICE" to get an instant valuation!</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; padding: 2rem; opacity: 0.6;">
                <div style="font-size: 5rem;">📊</div>
                <p style="font-size: 1.2rem; color: #666;">Ready to predict your house price?</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="background: white; border-radius: 20px; padding: 1.5rem; text-align: center; 
                margin-top: 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
        <p style="color: #666; margin: 0; font-size: 0.9rem;">
            🏠 <strong>House Price Predictor</strong> | Powered by Machine Learning & Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)