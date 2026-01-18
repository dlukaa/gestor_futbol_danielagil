from odoo import models, fields, api, exceptions

class FootballMatch(models.Model):
    _name = 'football.match'
    _description = 'Football Match'

    name = fields.Char(string='Nombre del Partido', compute='_compute_name', store=True)
    date = fields.Datetime(string='Fecha', default=lambda self: fields.Datetime.now())
    
    home_club_id = fields.Many2one('football.club', string='Equipo Local', required=True)
    away_club_id = fields.Many2one('football.club', string='Equipo Visitante', required=True)
    
    home_score = fields.Integer(string='Goles Local', default=0)
    away_score = fields.Integer(string='Goles Visitante', default=0)
    
    competition_id = fields.Many2one('football.competition', string='Competición')
    
    player_ids = fields.Many2many('football.player', string='Jugadores')
    
    total_goals = fields.Integer(string='Goles Totales', compute='_compute_total_goals', store=True)

    @api.depends('home_club_id', 'away_club_id', 'date')
    def _compute_name(self):
        for record in self:
            home = record.home_club_id.name or 'Unknown'
            away = record.away_club_id.name or 'Unknown'
            date_str = record.date.strftime('%Y-%m-%d') if record.date else ''
            record.name = f"{home} vs {away} ({date_str})"

    @api.depends('home_score', 'away_score')
    def _compute_total_goals(self):
        for record in self:
            record.total_goals = record.home_score + record.away_score

    @api.constrains('home_club_id', 'away_club_id')
    def _check_teams(self):
        for record in self:
            if record.home_club_id == record.away_club_id:
                raise exceptions.ValidationError("El equipo local y el visitante no pueden ser el mismo.")
