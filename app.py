import streamlit as st
import numpy as np
import pickle

# Load the trained model (Ensure you have a saved model file: 'xgboost_model.pkl')
with open("xgboost_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
def main():
    st.title("House Price Prediction App")
    st.write("Enter house details to get an estimated price prediction.")
    
    # Input fields
    area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=100)
    bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
    bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, step=1)
    stories = st.number_input("Number of Stories", min_value=1, max_value=5, step=1)
    parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=5, step=1)
    
    mainroad = st.checkbox("Near Main Road")
    guestroom = st.checkbox("Guest Room Available")
    basement = st.checkbox("Basement Available")
    hotwaterheating = st.checkbox("Hot Water Heating")
    airconditioning = st.checkbox("Air Conditioning")
    prefarea = st.checkbox("Preferred Area")
    
    furnishing = st.selectbox("Furnishing Status", ["Furnished", "Semi-Furnished", "Unfurnished"])
    
    # Convert categorical values to numeric
    mainroad = 1 if mainroad else 0
    guestroom = 1 if guestroom else 0
    basement = 1 if basement else 0
    hotwaterheating = 1 if hotwaterheating else 0
    airconditioning = 1 if airconditioning else 0
    prefarea = 1 if prefarea else 0
    
    furnishing_furnished = 1 if furnishing == "Furnished" else 0
    furnishing_semi = 1 if furnishing == "Semi-Furnished" else 0
    furnishing_unfurnished = 1 if furnishing == "Unfurnished" else 0
    
    # Prediction
    if st.button("Predict Price"):
        input_features = np.array([[
            area, bedrooms, bathrooms, stories, parking,
            mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea,
            furnishing_semi, furnishing_unfurnished
        ]])
        
        predicted_price = model.predict(input_features)[0]
        st.success(f"Estimated House Price: ₹{predicted_price:,.2f}")

if __name__ == "__main__":
    main()
