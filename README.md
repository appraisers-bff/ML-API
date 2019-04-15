# Appraiser's BFF API

Appraiser's BFF is a web app designed to provide local fair market value estimates (FMV) for homes in LA County, California. The data science portion of the app is a separately hosted Flask app that functions as an API that the backend communicates with to generate FMV estimates. 

Inital data exploration, data cleaning, and model training were completed in a Jupyter notebook. The model was then pickled so that it could be deployed with the Flask app. The Flask app reads in JSON data, coverts it to a numpy array, and then feeds it to the model to generate a prediction, which is then returned as JSON. It also makes a request to the Zillow API so that results can be compared.

## Demo video
https://www.youtube.com/watch?v=wup1IUjhlKI
