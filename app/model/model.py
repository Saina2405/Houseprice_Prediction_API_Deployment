import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


def model():
    """
    Polynomial regression model to predict property price 
    """

    df = pd.read_csv('data/clean_data.csv')

    # Drop Immoweb ID
    df = df.drop(columns='Immoweb ID')

    # Rename Terrace_Combined and garden_label columns
    df = df.rename(columns={
        "Terrace_Combined": "Terrace",
        "garden_label": "Garden"
    })

    # Drop Post code, Price and Bedrooms columns
    X = df.drop(df.filter(regex='Post code').columns, axis=1)
    X = X.drop(columns=['Price', 'Bedrooms'])

    y = df['Price']

    # Split X and y into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # Polynomial Regression
    degree = 2

    polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    polyreg.fit(X_train, y_train)

    # Create a model pickle file
    pickle.dump(polyreg, open('model.pkl', 'wb'))

    # Create model columns pickle file
    model_columns = list(X_train.columns)
    pickle.dump(model_columns, open('model_columns.pkl', 'wb'))


if __name__ == '__main__':
    model()