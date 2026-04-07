import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df=pd.read_csv('amazon.csv')




def train_model(df):
    X = df[['discounted_price', 'actual_price', 'discount_percentage', 'rating_count']]
    y = df['rating']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred=model.predict(X_test)
    print("\nModel Performance:")
    print("R2 Score:",r2_score(y_test,y_pred))

    print("\nSample Prediction:")
    for i in range(5):
        print(f"Actual:{y_test.iloc[i]:.2f} | Predicted:{y_pred[i]:.2f}")



    return model


model = train_model(df)
print("\n--- Predict Rating ---")
dp = float(input("Discounted Price: "))
ap = float(input("Actual Price: "))
disc = float(input("Discount %: "))
rc = float(input("Rating Count: "))

prediction = model.predict([[dp, ap, disc, rc]])

print(f"\nPredicted Rating: {prediction[0]:.2f}")