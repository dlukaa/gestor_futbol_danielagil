from odoo import models, fields

class FootballCompetition(models.Model):
    _name = 'football.competition'
    _description = 'Football Competition'

    name = fields.Char(string='Nombre de la Competición', required=True)
    prize_money = fields.Float(string='Premio')
    
    match_ids = fields.One2many('football.match', 'competition_id', string='Partidos')
