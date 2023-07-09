import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Channel:
    api_key: str = os.getenv('YI-API-KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_channel):
        self.__id_channel = id_channel

    def print_info(self):
        channel = Channel.youtube.channels().list(id=self.__id_channel, part='snippet,statistics').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        print(dict_channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, file):
        channel = self.youtube.channels().list(id=self.__id_channel, part='snippet,statistics').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        with open(file, 'a') as file_in:
            file_in.write(dict_channel)


