import sys
import sys
from googleapiclient.discovery import build
import json
import re
# Set up the API key and create a YouTube API service object
api_key = 'AIzaSyDqpyPFBcgYwAR9vJduSDxq25lNfxmZgDU'
youtube = build('youtube', 'v3', developerKey=api_key)

  
# youtube_url= "https://www.youtube.com/watch?v=R-sh3kfdHQ4"


def url_check(video_url=None):
    # global video_id
    pattern = r'v=([A-Za-z0-9_-]+)'
    print(video_url,re.findall(r'https://www.youtube.com/watch\?v=',video_url))
    if video_url==None:
        return 0
    elif len(re.findall(r'https://www.youtube.com/watch\?v=',video_url))!=1:
        print("Empty")
        return 0
    else:
        video_id = re.search(pattern, video_url)
        # video_id=video_id.group(1)
        # fetch_comments(video_id)
        return video_id.group(1)

# Function to fetch comments for a specific video
def fetch_comments(video_id, page_token=None):
    try:
        all_comments = []  # Declare the list inside the function
        while True:
            comments = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                pageToken=page_token
            ).execute()

            for comment in comments['items']:
                snippet = comment['snippet']['topLevelComment']['snippet']
                author = snippet['authorDisplayName']
                text = snippet['textDisplay']
                all_comments.append(f'{text}')

            if 'nextPageToken' in comments:
                page_token = comments['nextPageToken']
            else:
                break  # No more comments to fetch, exit the loop
        return all_comments  # Return the comments from the function
    except:
        return 0

# Function to fetch comments for a specific video
# def fetch_comments(video_id, page_token=None):
#     all_comments=[]
#     comments = youtube.commentThreads().list(
#         part='snippet',
#         videoId=video_id,
#         textFormat='plainText',
#         pageToken=page_token
#     ).execute()

#     for comment in comments['items']:
#         snippet = comment['snippet']['topLevelComment']['snippet']
#         author = snippet['authorDisplayName']
#         text = snippet['textDisplay']
#         all_comments.append(f'{text}')

#     # Check if there are more comments to fetch
#     if 'nextPageToken' in comments:
#         # fetch_comments(video_id, page_token=comments['nextPageToken'])
#         all_comments.extend(fetch_comments(video_id, page_token=comments['nextPageToken']))




def main(youtube_url=None, keyword=None):
    # Start fetching comments
    print("Featching...")
    
    video_id = url_check(video_url=youtube_url)
    print(video_id)
    if video_id==0:
        print("Check Your URL and Try Again...")
        return 0
    all_comments = fetch_comments(video_id=video_id)
    if all_comments==0:
        print("Video Not Found")
        return 404
    

    ##save comments to json file
    data = {"comment": all_comments}
    # print("all_comments = ",all_comments)
    # with open('video_comments.json', 'w') as file:
    #     json.dump(data,file, indent=4)

    # keyword = input("Enter Keyword = ")
    pattern = rf'\b{re.escape(keyword)}\b'
    fetch = [comment for comment in all_comments if re.search(pattern, comment.lower())]
    return fetch
    # print(fetch)



# if __name__=="__main__":
#     # Start fetching comments
#     print("Featching...")
#     video_id = url_check(video_url=youtube_url)
#     if video_id==0:
#         print("Check Your URL and Try Again...")
#         sys.exit()
#     fetch_comments(video_id=video_id)
    
#     ## save comments to json file
#     # data = {"comment": all_comments}
#     # with open('video_comments.json', 'w') as file:
#     #     json.dump(data,file, indent=4)

#     keyword = input("Enter Keyword = ")
#     pattern = rf'\b{re.escape(keyword)}\b'
#     fetch = [comment for comment in all_comments if re.search(pattern, comment.lower())]
#     print(fetch)

