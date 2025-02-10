import requests
from odoo import http
from odoo.http import request


class PrayerAPI(http.Controller):

    @http.route('/hb_prayer/times', type='json', auth="public")
    def get_prayer_times(self, city="Makkah", country="SA"):
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("data", {}).get("timings", {})
        return {"error": "Unable to fetch prayer times"}
