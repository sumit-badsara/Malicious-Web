# Malicious Web Content Detection using Machine Learning

### Steps for reproducing the project -
* Install all the required packages using the following command - ```pip install -r requirements.txt```.
* Run the Flask App - ```python myapp.py```
* Goto ```localhost:5000/train/``` to train the model
* Goto ```localhost:5000/check/``` to test the model, pass the form data `url` containing url.
* Done!

### Research paper - http://ieeexplore.ieee.org/document/8256834/

#### Abstract -
* Naive users using a browser have no idea about the back-end of the page. The users might be tricked into giving away their credentials or downloading malicious data.
* Our aim is to create an extension for Chrome which will act as middleware between the users and the malicious websites, and mitigate the risk of users succumbing to such websites.
* Further, all harmful content cannot be exhaustively collected as even that is bound to continuous development. To counter this we are using machine learning - to train the tool and categorize the new content it sees every time into the particular categories so that corresponding action can be taken.
