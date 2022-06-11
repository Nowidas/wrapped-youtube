from googleapiclient.discovery import build
from SECRETS import YOUTUBE_API_KEY

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

#'snippet,contentDetails,statistics,topicDetails,localizations''snippet,contentDetails,statistics'
request = youtube.videos().list(part='snippet,contentDetails,topicDetails, statistics, localizations', id='4VxdufqB9zg')

response = request.execute()
print(response)