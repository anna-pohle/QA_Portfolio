class DateUtils:
    #Utilities für Datums-Operationen

    @staticmethod
    def get_date_x_years_ago(years: int) -> str:
        """Gibt Datum vor X Jahren zurück im Format DD-MM-YYYY"""
        from datetime import datetime, timedelta
        date = datetime.now() - timedelta(days=years * 365)
        return date.strftime("%d-%m-%Y")

    @staticmethod
    def get_current_timestamp() -> str:
        #Gibt aktuellen Unix-Timestamp zurück
        import time
        return str(int(time.time()))
