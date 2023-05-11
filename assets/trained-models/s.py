import warnings
import pickle

# Suppress the warning message
warnings.filterwarnings("ignore", category=UserWarning)
# Load the contents of the .pkl file into a Python object
with open('file.pkl', 'rb') as f:
    model = pickle.load(f)

# Inspect the contents of the loaded object
# print(model.check_feature_names())
print((model.coef_))
