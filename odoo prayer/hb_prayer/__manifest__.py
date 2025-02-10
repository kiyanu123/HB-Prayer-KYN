{
    'name': 'Prayer Tracker',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Track Daily Prayers and Scores',
    'author': 'Shafaf Shahul',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/prayer_tracker_views.xml',
        'views/dashboard_views.xml',
        'data/prayer_data.xml',
        'reports/prayer_leaderboard.xml',
    ],
    'installable': True,
    'application': True,
}