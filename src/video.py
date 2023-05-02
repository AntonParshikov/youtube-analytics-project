from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id):
        self.video_id = video_id
        youtube = self.get_service()
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=self.video_id
                                           ).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/watch?v=' + self.video_id
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']


class PLVideo(Video):

    def __init__(self, video_id, play_list_id):
        super().__init__(video_id)
        youtube = self.get_service()
        self.play_list_id = youtube.playlistItems().list(playlistId=play_list_id,
                                                         part='contentDetails',
                                                         maxResults=50,
                                                         ).execute()
