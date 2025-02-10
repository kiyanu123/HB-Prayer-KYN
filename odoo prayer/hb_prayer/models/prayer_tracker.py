from odoo import models, fields, api


class PrayerTracker(models.Model):
    _name = 'hb_prayer.tracker'
    _description = 'Prayer Tracker'

    name = fields.Char(string="Participant Name", required=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.today)

    fajr = fields.Selection([
        ('0', 'Not Prayed'),
        ('3', 'Prayed Late'),
        ('2', 'Prayed on Time'),
        ('1', 'Prayed in Jamaah'),
    ], string="Fajr", default='0')

    dhuhr = fields.Selection([...], string="Dhuhr", default='0')
    asr = fields.Selection([...], string="Asr", default='0')
    maghrib = fields.Selection([...], string="Maghrib", default='0')
    isha = fields.Selection([...], string="Isha", default='0')

    sunnah = fields.Text(string="Sunnah Prayers")
    fasting = fields.Boolean(string="Fasting Today")
    quran_learning = fields.Text(string="Read & Learn Quran")

    score = fields.Integer(string="Score", compute="_compute_score", store=True)

    @api.depends('fajr', 'dhuhr', 'asr', 'maghrib', 'isha', 'fasting', 'quran_learning')
    def _compute_score(self):
        for record in self:
            score = 0
            prayer_values = {'0': 0, '3': 3, '2': 2, '1': 1}
            score += sum(
                prayer_values[getattr(record, prayer)] for prayer in ['fajr', 'dhuhr', 'asr', 'maghrib', 'isha'])
            if record.fasting:
                score += 5
            if record.quran_learning:
                score += 3
            record.score = score
