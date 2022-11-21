import os
from dotenv import load_dotenv
import googleapiclient.discovery

load_dotenv()
TOKEN = os.getenv('TEST_DISCORD_TOKEN')
api_key=os.getenv('YOUTUBE_API')
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
search=input()
request=youtube.search().list(q=search,part="snippet",type='video',order="relevance",maxResults=1)
responce=request.execute()
for i in responce['items']:
    print(i['snippet']['title'])