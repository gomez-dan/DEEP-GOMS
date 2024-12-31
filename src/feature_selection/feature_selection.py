import pandas as pd
from sklearn.linear_model import Lasso, Ridge

def select_features(integrated_data_filepath, output_filepath):
    # Load integrated data
    data = pd.read_csv(integrated_data_filepath)
    
    # Feature matrix and target variable
    X = data.drop('target_variable', axis=1)
    y = data['target_variable']
    
    # LASSO feature selection
    lasso = Lasso(alpha=0.001)
    lasso.fit(X, y)
    selected_features_lasso = X.columns[(lasso.coef_ != 0).ravel().tolist()]
    
    # Ridge feature selection
    ridge = Ridge(alpha=1.0)
    ridge.fit(X, y)
    selected_features_ridge = X.columns[(ridge.coef_ != 0).ravel().tolist()]
    
    # Combine selected features from both methods
    selected_features = list(set(selected_features_lasso) | set(selected_features_ridge))
    
    # Save selected features
    pd.Series(selected_features).to_csv(output_filepath, index=False)

if __name__ == "__main__":
    select_features("data/processed/integrated_data.csv", "data/processed/selected_features.csv")
