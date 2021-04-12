``Link for the App:`` https://bi-ner-streamlit.herokuapp.com/
===============================

Streamlit is an open-source Python framework that allows you to create beautiful interactive websites for Machine Learning and Data Science projects without needing to have any web development skills.

It achieves this by allowing you to create a website by only adding a few Streamlit function calls to an existing python projects
Spacy-Streamlit is a python package that is useful for visualizing spaCy models and building interactive spaCy-powered apps with Streamlit.

It has several functions and utils for visualizing spacy’s essential NLP features like NER(Named Entity Recognition) using visualize_ner()

With Spacy-streamlit making visualization for NLP task is very easy and requires little code. It contains several building blocks for doing some cools stuff.

We will be using the basic streamlit  st.text_area() function for receiving input from the user

NER:In this section of the app  we will visualize any named entity in our text using the space_streamlit.visualize_ner( ) function
With this function you can even omit entity labels you don’t want to recognize which is quite cool considering the numerous ways we can apply this.

We can now run our app from our terminal using


    streamlit run app.py

Our app will automatically be opened on the expected localhost in our browser.


In order to deploy a Streamlit application with Heroku, a platform as a service (PaaS), there was a lot of things you need to know
First, you need to add some files that allow Heroku to install the needed requirements and run the application.

The requirements.txt file contains all the libraries that need to be installed for the project to work. This file can be created manually by going through all files and looking what libraries are used or automatically using something like pipreqs.

setup.sh and Procfile

Using the setup.sh and Procfile files you can tell Heroku the needed commands for starting the application.
In the setup.sh file we will create a streamlit folder with a credentials.toml and a config.toml file.

The Procfile is used to first execute the setup.sh and then call streamlit run to run the application.


Installation
------------


    pip install wikipedia
    pip install wikipedia-api 
    pip install streamlit
    pip install spacy-streamlit
    python -m spacy download en


## NOTE: To run the project offline comment out the 7th and 9th line of code from file wikicopy.py and remove the comment from 8th line of code
(In case you're interested to run the same application using Flask and Spacy checkout the file wiki.py)

To conclude spacy_streamlit makes it quite easier to visualize interesting NLP takes with just simple code.
