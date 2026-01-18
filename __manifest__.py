{
    'name': 'Gestor de Fútbol',
    'version': '1.0',
    'summary': 'Módulo para gestionar clubes de fútbol, jugadores y competiciones',
    'description': """
        Módulo de Gestión de Fútbol
        ===========================
        Gestiona Clubes, Jugadores, Partidos y Competiciones.
    """,
    'category': 'Deportes',
    'author': 'Student',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/football_menus.xml',
        'views/football_club_views.xml',
        'views/football_player_views.xml',
        'views/football_match_views.xml',
        'views/football_coach_views.xml',
        'views/football_competition_views.xml',
    ],
    'installable': True,
    'application': True,
}
