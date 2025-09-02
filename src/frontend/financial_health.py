from flask import Blueprint, render_template
import requests
import os

financial_health_bp = Blueprint('financial_health', __name__, template_folder='templates')

# URL of your insights_service
INSIGHTS_SERVICE_URL = os.getenv("INSIGHTS_SERVICE_URL", "http://localhost:8080/api/v1/insights")

@financial_health_bp.route('/financial-health/<user_id>')
def financial_health(user_id):
    try:
        resp = requests.get(f"{INSIGHTS_SERVICE_URL}/{user_id}")
        resp.raise_for_status()
        insights = resp.json()
    except Exception as e:
        insights = {"error": str(e)}

    return render_template('financial_health.html', insights=insights)
