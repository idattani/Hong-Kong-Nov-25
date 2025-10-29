import pandas as pd

def osha_experiment(data):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.linear_model import LogisticRegression

    # Check for missing values
    if data.isnull().sum().any():
        print("Missing values detected in the dataset.")
    else:
        print("No missing values in the dataset.")

    # Display first few rows to verify
    print(data.head())

    # Select target column (label) and features
    X_Raw = data
    y_true = (data['Degree of Injury'] == 'Fatal').astype(int)

    sensitive_features = X_Raw[['Nature of Injury', 'Part of Body']]
    X = X_Raw.drop(labels=['Nature of Injury', 'Part of Body'], axis=1)

    # One-hot encoding for categorical variables
    X = pd.get_dummies(X)

    # Scale the features
    sc = StandardScaler()
    X_scaled = sc.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    # Encode the target variable
    le = LabelEncoder()
    y_true = le.fit_transform(y_true)

    X_train, X_test, y_train, y_test, sensitive_features_train, sensitive_features_test = \
    train_test_split(X_scaled, y_true, sensitive_features,
                     test_size=0.2, random_state=0, stratify=y_true)

    # Work around indexing bug
    X_train = X_train.reset_index(drop=True)
    sensitive_features_train = sensitive_features_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    sensitive_features_test = sensitive_features_test.reset_index(drop=True)

    # Train the model
    unmitigated_predictor = LogisticRegression(solver='liblinear', fit_intercept=True)
    unmitigated_predictor.fit(X_train, y_train)

    # Make predictions
    y_pred = unmitigated_predictor.predict(X_test)
    sensitive_features_test['y_test'] = y_test
    sensitive_features_test['y_pred'] = y_pred

    return {'sensitive_features': sensitive_features_test,
            'y_test': y_test,
            'y_pred': y_pred}

if __name__ == "__main__":
    data = pd.read_csv('osha_mock.csv')
    osha_experiment(data)
