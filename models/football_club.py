from odoo import models, fields

class FootballClub(models.Model):
    _name = 'football.club'
    _description = 'Football Club'

    name = fields.Char(string='Nombre del Club', required=True)
    foundation_date = fields.Date(string='Fecha de Fundación')
    city = fields.Char(string='Ciudad')
    
    player_ids = fields.One2many('football.player', 'club_id', string='Jugadores')
    home_match_ids = fields.One2many('football.match', 'home_club_id', string='Partidos como Local')
    away_match_ids = fields.One2many('football.match', 'away_club_id', string='Partidos como Visitante')
