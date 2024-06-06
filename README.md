# MixMatch


Music Stats Generator is an innovative web-based app designed to provide users with comprehensive insights into their music listening habits and preferences. It offers a personalized experience by analyzing users' playlists and giving recommended or collaborated playlists. The app supports playlist integration from Spotify, YouTube, and Last.fm.

## Features

- **Playlist Scraping**: Extracts playlist data from Spotify, YouTube, and Last.fm.
- **Data Analysis**: Uses Gemini AI API to analyze playlists and generate recommendations.
- **Playlist Creation**: Allows users to create new playlists on Spotify, YouTube, or Last.fm.
- **User Interface**: Simple web-based interface with options to choose the platform for creating new playlists.

## Technologies Used

- **Backend**: Python, Flask
- **APIs**: Spotify Web API, YouTube Data API, Last.fm API, Gemini AI API
- **Web Scraping**: BeautifulSoup
- **Authentication**: OAuth

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/music-stats-generator.git
    cd music-stats-generator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API keys**:
    - Spotify API keys
    - YouTube Data API keys
    - Last.fm API keys
    - Gemini AI API key

    Create a `.env` file and add your API keys:
    ```env
    SPOTIPY_CLIENT_ID='your_spotify_client_id'
    SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
    SPOTIPY_REDIRECT_URI='your_spotify_redirect_uri'

    YOUTUBE_API_KEY='your_youtube_api_key'

    LASTFM_API_KEY='your_lastfm_api_key'

    GEMINI_API_KEY='your_gemini_api_key'
    ```

5. **Run the Flask app**:
    ```bash
    flask run
    ```

## Usage

1. **Upload Playlist**:
    - Send a POST request to `/upload_playlist` with the platform and playlist ID.
    - Example: `curl -X POST -H "Content-Type: application/json" -d '{"platform": "spotify", "playlist_id": "your_playlist_id"}' http://127.0.0.1:5000/upload_playlist`

2. **Analyze Playlist**:
    - Send a POST request to `/analyze_playlist` with the playlist data.
    - Example: `curl -X POST -H "Content-Type: application/json" -d '@playlist_data.json' http://127.0.0.1:5000/analyze_playlist`

3. **Create Playlist**:
    - Send a POST request to `/create_playlist` with the platform and recommendations.
    - Example: `curl -X POST -H "Content-Type: application/json" -d '{"platform": "youtube", "recommendations
