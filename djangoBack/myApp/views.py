from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from joblib import load  # Assuming you're using joblib to save/load your AI model
import json
from xgboost import XGBRegressor
# Create your views here.
from django.http import JsonResponse
from joblib import load
from xgboost import XGBRegressor
import numpy as np

@csrf_exempt
def rating_predict(request):
    if request.method == 'POST':
        model = XGBRegressor()
        model.load_model('../xgboost_model_old_version.XGBoostRegressor')
        # model = load('../XGBoostRegressor.joblib')



        # Assuming the input data is sent as a JSON object
        try:
            input_data = json.loads(request.body)
            print(input_data)
            # Process the input data and make predictions
            # predictions = model.predict(input_data)

            # Convert the input data to a 2D array-like object
            input_array = np.array([[input_data[key] for key in input_data]])

            # Make predictions
            predictions = model.predict(input_array)
            # print(predictions)
            # Format the predictions as a JSON response
            response = {'rating': str(round(predictions[0], 2))}
            print(response)
            # return JsonResponse(response,safe=False)
            return JsonResponse(response,safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})

    return JsonResponse({'error': 'Invalid request'})

    #     # Assuming the input data is sent as a JSON object
    #     # input_data = request.POST.get('input_data', None)
    #     # if input_data:
    #     #     print(input_data)
    #         # Convert the input data to the appropriate format for prediction
    #     input_data = json.loads(request.body)
    #
    #     # Process the input data and make predictions
    #     # Use your specific method for predicting with the loaded model_data
    #     predictions = model.predict(input_data, input_data)
    #
    #     # Format the predictions as a JSON response
    #     response = {'predictions': predictions}
    #     return JsonResponse(response)
    #
    # return JsonResponse({'error': 'Invalid request'})