from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload_playlist', methods=['POST'])
def upload_playlist():
    data = request.json
    playlist_data = get_playlist_data(data['platform'], data['playlist_id'])
    return jsonify(playlist_data)

@app.route('/analyze_playlist', methods=['POST'])
def analyze_playlist():
    data = request.json
    recommendations = analyze_playlist(data)
    return jsonify(recommendations)

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    data = request.json
    platform = data['platform']
    recommendations = data['recommendations']
    if platform == 'youtube':
        create_youtube_playlist("Recommended Playlist", recommendations)
    elif platform == 'spotify':
        create_spotify_playlist("Recommended Playlist", recommendations)
    elif platform == 'lastfm':
        create_lastfm_playlist("Recommended Playlist", recommendations)
    return jsonify({"message": "Playlist created successfully"})

if __name__ == '__main__':
    app.run(debug=True)
