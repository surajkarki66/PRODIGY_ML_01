import numpy as np
import pickle

# Load the pre-trained linear regression model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_price():
    try:
        # Get input values from the entry widgets
        bedrooms = int(input("Enter the number of bedrooms above the ground: "))
        lot_area = float(input("Enter the lot size in square feet: "))
        bsmt_full_bath = int(input("Enter the no. of full bathrooms in basement: "))
        bsmt_half_bath = int(input("Enter the no. of half bathrooms in basement: "))
        full_bath = int(input("Enter the no. of full bathrooms above grade: "))
        half_bath = int(input("Enter the no. of half bathrooms above grade: "))

        # Make predictions using the model
        input_data = np.array([bedrooms, lot_area, bsmt_full_bath, bsmt_half_bath, full_bath, half_bath])
        predicted_price = model.predict(input_data.reshape(1, -1))[0]
        print(f"Predicted Sale Price: ${predicted_price:,.2f}")
    
    except ValueError:
        print("Error: Please enter valid numerical values for all input fields.")


if __name__ == "__main__":
    print("----------------------- House Price Prediction --------------------------------")
    predict_price()