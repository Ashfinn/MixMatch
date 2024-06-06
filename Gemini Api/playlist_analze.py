import requests

def analyze_playlist(playlist_data):
    url = "https://api.gemini.ai/analyze"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=playlist_data)
    recommendations = response.json()
    return recommendations

recommendations = analyze_playlist(playlist_data)
print(recommendations)
