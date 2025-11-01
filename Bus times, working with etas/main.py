import time
from tfwm_service import TfwmService as Service

ATCO_CODE = "43000203903" #bus stop code 
REFRESH_MS = 30_000

def main():
    while True:
        service = Service()
        times = service.get_times(ATCO_CODE)
        for t in times:
            live = "LIVE" if not t.is_timetabled else "TIMETABLED" #show ETA times else show timetabled times
            print(f"{t.number:<4}{t.name:<25}{t.scheduled_time:8}{live}")
        time.sleep(REFRESH_MS / 1000)
if __name__ == "__main__":
    main()
