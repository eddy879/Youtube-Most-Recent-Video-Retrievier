from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('api_key') 

channel_search = input('What is the name of the channel?\n')
youtube = build('youtube', 'v3', developerKey=API_KEY)
request = youtube.search().list( 
    part='snippet',
    type= 'channel',
    q=channel_search,
    maxResults=1,
)
response = request.execute()
response = dict(response)
items_list = response.pop('items')
for item in items_list:
    item = dict(item)
    id = item.get('id')
    channel_id = id['channelId']
print('--------')

request = youtube.channels().list(        
    part="snippet",
    id=channel_id
)
response = request.execute()
response = dict(response)
item = list(response.get('items'))
for i in item:
    i = dict(i)
    title_location = dict(i.get('snippet'))
    title = title_location.get('title')
print('--------')

request = youtube.activities().list( 
        part="snippet,contentDetails",
        channelId=channel_id,
        maxResults=1
)
response = dict(request.execute())
items_list = list(response.get('items'))
for item in items_list:
    item = dict(item)
    vid_title_location = item.get('snippet')
    vid_title = vid_title_location['title']
content_details = dict(item.get('contentDetails'))
video_id_location = list(content_details.values())
for value in video_id_location:
    value = dict(value)
    vid_id = value['videoId']
print('--------')

print("That YouTube channel's latest video is "+str(vid_title)+" and this is the link to it: https://www.youtube.com/watch?v="+str(vid_id)+"&ab_channel="+str(title)+"")