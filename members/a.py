from urllib.parse import urlparse, parse_qs

def extract_video_id(youtube_url):
    try:
        parsed_url = urlparse(youtube_url)
        query_parameters = parse_qs(parsed_url.query)
        video_id = query_parameters.get('v', [None])[0]
        if video_id and len(video_id) == 11:
            return video_id
        else:
            return None
    except Exception as e:
        print(f"Error extracting video ID: {e}")
        return None

# Example usage
youtube_url = "https://www.youtube.com/watch?v=2bwE-yqsDlI&list=PLLGohJ-IqnmYZuPOPYWS1RKppc_jLMJoR&index=18"
video_id = extract_video_id(youtube_url)
if video_id:
    print(f"Video ID: {video_id}")
else:
    print("Invalid YouTube URL or video ID not found.")
