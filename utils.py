import pickle
import numpy as np
import config

def get_apple_quality(Size, Weight, Sweetness,Crunchiness,Juiciness,Ripeness,Acidity):
    model_file_path = config.MODEL_FILE_PATH

    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)

    test_array = np.array([[Size, Weight, Sweetness,Crunchiness,Juiciness,Ripeness,Acidity]])
    apple_quality = model.predict(test_array)[0]

    return apple_quality
