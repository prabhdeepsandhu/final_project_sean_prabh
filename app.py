from flask import Flask
import numpy as np
import json
from plotly import data
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)


@app.route('/recommender')
def recommended_songs():
    
    return data
if __name__ == "__main__":
    app.run(debug=True)