import requests

FAKE_API_KEY = "12345"
DATA_ANALYZER_REST_API_IG_DATA = "http://127.0.0.1:5000/igdata/"

def get_all_posts_metrics():
    response = requests.get(DATA_ANALYZER_REST_API_IG_DATA + FAKE_API_KEY)
    data = []
    if (response.status_code == 200):
        for user in response.json()["data"]:
            curr_user = (user["id"], user["username"], user["full_name"], user["posts"], user["average_likes"], user["most_recent_post"], user["last_updated"])
            data.append(curr_user)
    return data