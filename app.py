import streamlit as st
import pandas as pd
import joblib

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="InvoiceLens",
    page_icon="📦",
    layout="wide"
)

# =====================================
# Custom Styling
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.big-title {
    font-size: 3.2rem;
    font-weight: 800;
    color: #1e293b;
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin-top: 1rem;
}

.description {
    font-size: 1.15rem;
    color: #475569;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Load Model
# =====================================

model = joblib.load("models/linear_regression.pkl")

# =====================================
# Sidebar
# =====================================

st.sidebar.title("📦 InvoiceLens")

st.sidebar.markdown("---")

st.sidebar.markdown("### Model Selection")

st.sidebar.radio(
    "Choose Prediction Module",
    ["Freight Cost Prediction"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Business Impact")

st.sidebar.markdown("""
- 📉 Improved cost forecasting
- 💰 Better budgeting decisions
- 🚚 Vendor freight optimization
- 📊 Data-driven procurement planning
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### Tech Stack")

st.sidebar.markdown("""
- Python
- SQLite
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP
- Streamlit
""")

# =====================================
# Header
# =====================================

st.markdown(
    '<div class="big-title">InvoiceLens</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">AI-Driven Freight Cost Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
    Predict vendor freight costs using invoice quantity and invoice dollar amount.
    This machine learning solution helps procurement teams estimate shipping expenses
    before invoice processing, improving budgeting and vendor negotiations.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================
# Model Metrics
# =====================================

st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="R² Score",
        value="97.00%"
    )

with col2:
    st.metric(
        label="MAE",
        value="24.46"
    )

with col3:
    st.metric(
        label="RMSE",
        value="124.43"
    )

st.markdown("---")

# =====================================
# Prediction Section
# =====================================

st.markdown(
    '<div class="section-title">🚚 Freight Cost Prediction</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Enter invoice details below to estimate the expected freight cost.
    """
)

col1, col2 = st.columns(2)

with col1:
    quantity = st.number_input(
        "📦 Quantity",
        min_value=1,
        value=500,
        step=1
    )

with col2:
    dollars = st.number_input(
        "💰 Invoice Dollars",
        min_value=0.0,
        value=18500.0,
        step=100.0
    )

predict_btn = st.button(
    "🔮 Predict Freight Cost",
    use_container_width=True
)

# =====================================
# Prediction Logic
# =====================================

if predict_btn:

    input_df = pd.DataFrame({
        "Quantity": [quantity],
        "Dollars": [dollars]
    })

    prediction = model.predict(input_df)[0]

    st.markdown("<br>", unsafe_allow_html=True)

    st.success("Prediction Generated Successfully!")

    st.metric(
        label="Predicted Freight Cost",
        value=f"${prediction:,.2f}"
    )

    st.caption(
        "Estimated freight cost generated using the trained Linear Regression model."
    )

# =====================================
# Footer
# =====================================

st.markdown("---")

st.caption(
    "InvoiceLens • End-to-End Freight Cost Prediction System • Built by Arnesh Bera"
)