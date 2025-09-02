from flask import render_template
import requests
import os

# Define the route for the Financial Health page
@app.route('/financial-health/<user_id>')
def financial_health(user_id):
    """
    Fetch personalized financial insights for the user
    and render them in the financial_health template.
    """
    try:
        # Construct the URL for the insights service
        insights_service_url = os.getenv("INSIGHTS_SERVICE_URL", "http://localhost:8080/api/v1/insights")
        response = requests.get(f"{insights_service_url}/{user_id}")
        response.raise_for_status()
        insights = response.json()
    except requests.RequestException as e:
        # Handle errors gracefully
        insights = {"error": str(e)}

    # Render the template and pass the insights
    return render_template('financial_health.html', insights=insights)
