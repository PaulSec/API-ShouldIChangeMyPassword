"""
This is the (unofficial) Python API for ShouldIChangeMyPassword Website.

Using this code, you can manage to know if your email has been compromised using ShouldIChangeMyPassword's database.

"""
import requests
import json

URL = "https://shouldichangemypassword.com/check-single"


class SicmpAPI(object):

    """
        SicmpAPI Main Handler
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
            __new__ builtin
        """
        if not cls._instance:
            cls._instance = super(SicmpAPI, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def is_compromised(self, mail):
        payload = {'email': mail}
        try:
            r = requests.post(
                "https://shouldichangemypassword.com/check-single", data=payload, timeout=3)
            data = json.loads(r.content)
            return data['num'] > 0
        except Exception, e:
            print e.message
            pass
