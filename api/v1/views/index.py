#!/usr/bin/python3
"""Script to create routes for API endpoints"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


# Route to get the status of the API
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON status indicating that the API is running"""
    return jsonify({"status": "OK"})


# Route to get the count of all objects in the database
@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns the count of all objects in the database"""
    # Create a dictionary to store the counts of different objects
    stats_dict = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    # Return the dictionary as a JSON response
    return jsonify(stats_dict)
