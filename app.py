from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.now(pytz.utc).astimezone(pytz.timezone('UTC+2')).strftime('%A')

    # Get current UTC time within a +/-2 minute window
    current_time = datetime.now(pytz.utc).astimezone(pytz.timezone('UTC+2')).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    # Create JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
