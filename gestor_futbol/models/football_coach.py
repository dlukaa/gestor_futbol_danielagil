from odoo import models, fields

class FootballCoach(models.Model):
    _name = 'football.coach'
    _description = 'Football Coach'

    name = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(default=True)
    
    club_id = fields.Many2one('football.club', string='Club')
    
    salary = fields.Float(string='Salario')
    experience_years = fields.Integer(string='Experiencia (Años)')
    
    licenses = fields.Selection([
        ('c', 'Licencia C'),
        ('b', 'Licencia B'),
        ('a', 'Licencia A'),
        ('pro', 'Licencia Pro')
    ], string='Licencia de Entrenador')
