# Web URL Detection(Malicious/Safe) using Machine Learning
This project is made to help people to detect malicious URL using machine learning.
### Steps for reproducing the project -
* Install all the required packages using the following command - ```pip install -r requirements.txt```.
* Run the Flask App - ```python myapp.py```
* Goto ```localhost:5000/train/``` to train the model
* Goto ```localhost:5000/check/``` to test the model, pass the form data `url` containing url.
* Done!

### Description
This is a chrome extension with an additional website for real-time malicious web content detection. A binary classifier has been trained using Random Forest Classification algorithm to classify websites as malicious or benign. 22 features of the url have been used for the training of the model. The accuracy of the model's prediction is 96%.
