import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YouTube_API_KEY')

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.subscriberCount = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.viewCount = int(self.channel["items"][0]["statistics"]["viewCount"])

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, file_name):
        dictionary = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriberCount,
            'video_count': self.video_count,
            'viewCount': self.viewCount
        }
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)
