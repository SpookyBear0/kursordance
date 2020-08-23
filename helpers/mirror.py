import requests
import urllib

class MirrorHelper():
    """Responsible for letting Kursordance connect with a beatmap mirror."""
    def __init__(self, cheesegullapi_url: str = "http://storage.ripple.moe/api/", download_mirror:str="http://storage.ripple.moe/d/"):
        self.API_URL = cheesegullapi_url
        self.DL_MIRROR = download_mirror
    
    def _mirror_request(self, request_url: str, params: dict) -> dict:
        """Sends a request to the beatmap API."""
        a = requests.get(self.API_URL + request_url+"?"+ urllib.parse.urlencode(params))
        if a.status_code != 200:
            return None
        return a.json()

    def get_beatmapsetid_from_name(self, name: str) -> int:
        """Searches a beatmap name and returns a beatmap id."""
        req = self._mirror_request("search", {
            "query" : name,
            "amount" : 1,
            "status" : 1, #unranked is a mess
            "m" : 0
        })
        assert req is not None
        assert req != []

        return req[0]["SetID"]
    
    def download_mapset(self, set_id: int, save_dir="") -> None:
        """Downloads Beatmap Set."""
        req = requests.get(self.DL_MIRROR + str(set_id), allow_redirects=True)
        if req.content == "Set not found":
            raise FileNotFoundError #idk if this is the right one
        with open(save_dir + f"{set_id}.osz", "wb") as f:
            f.write(req.content)
