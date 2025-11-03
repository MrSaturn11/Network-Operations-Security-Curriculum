from tfwm_service import TfwmService 

ATCO_CODE = "43000203903" #unique bus stop code identifier  

def main():
    while True:
        service = TfwmService()
        times = service.get_times(ATCO_CODE)
        for t in times:
            live = "LIVE" if not t.is_timetabled else "TIMETABLED" #show ETA times else show timetabled times
            print(f"{t.number:<4}{t.name:<25}{t.scheduled_time:8}{live}")
        
        break #could loop every 30 seconds or so but dont want to reach my free limit too quickly
if __name__ == "__main__":
    main()
