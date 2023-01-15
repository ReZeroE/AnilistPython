import time
import requests
from .retrieve_data import ExtractInfo

class User:
    def __init__(self, access_info, activated=True):
        self.extractInfo = ExtractInfo(access_info, activated)

    def GetUserActivity(self, page, perpage):
        activity = self.extractInfo.user_activity(page, perpage)
        activity_data = activity["data"]
        if len(activity_data) > 0:
            return activity_data
        else:
            return None