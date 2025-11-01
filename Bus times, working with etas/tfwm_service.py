import requests
from bus_time import BusTime

APP_ID = "a265ddae"
APP_KEY = "7529d0b95200d8f98d16f755b80e9065"

class TfwmService:
    def get_times(self, atco_code: str):
        """    Fetch live and timetabled bus departures for a given bus stop."""
        url = f"https://transportapi.com/v3/uk/bus/stop/{atco_code}/live.json"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "group": "no", #dont group by route
            "limit": 8, #next 8 departures
            "nextbuses": "yes" #gives live bus times provided the atco code is able to give them
        }

        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status() 
        data = r.json() #storing json data in data var

        out = []
        for line, buses in data.get("departures", {}).items():
            for b in buses:
                mins = b.get("best_departure_estimate_mins") # if it finds the best_departure_estimate_mins value then gives ETA
                direction = b.get("direction", "") 
                time = f"{mins} mins" if mins is not None else b.get("aimed_departure_time", "N/A") #if mins is None show timetabled time
                is_timetabled = mins is None
                out.append(BusTime(b["line"], direction, time, is_timetabled))
        return out
