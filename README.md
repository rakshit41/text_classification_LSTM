### text_classification_LSTM ###
The repository contains the training and deploying files for text classification Built using LSTM architecture, along with a .py file which will produce a inverted right angled triangle w.r.t user input number.
The "lstm_word2vec_binary_classification.ipynb" file contains the model training codes, which is trained on google colab
The final model is present in the resources folder

## Steps to deploy movie review classifier app on your local machine
1. Pull the files from the current repository or clone the repository
2. install the requirements by executing "pip install requirements.txt"
3. Run the following gunicorn command to deploy the API "gunicorn -c config_api.py classifier_api:app"
4. The api will be deployed at local server on port = 5010

## Instructions for calling the API
1. Input format = {"movie review":"The Avengers movie is the greatest movie ever produced in the marvels history"}
2. Application output = { "review sentiment": "Positive" }

## Steps to print right angled triangle
1. run the following command "python numbered_right_angled_triangle.py"
2. enter a number in the terminal
3. The output is a inverted right angled tringle 
