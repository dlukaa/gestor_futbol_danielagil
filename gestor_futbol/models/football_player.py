from odoo import models, fields, api
from datetime import date

class FootballPlayer(models.Model):
    _name = 'football.player'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Football Player'
    
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')

    position = fields.Selection([
        ('zk', 'Portero'),
        ('df', 'Defensa'),
        ('mf', 'Centrocampista'),
        ('fw', 'Delantero')
    ], string='Posición')
    
    number = fields.Integer(string='Dorsal')
    salary = fields.Float(string='Salario')
    birthdate = fields.Date(string='Fecha de Nacimiento')
    
    club_id = fields.Many2one('football.club', string='Club')
    match_ids = fields.Many2many('football.match', string='Partidos')
    
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)
    is_star = fields.Boolean(string='Es Estrella', compute='_compute_is_star', store=True)

    _sql_constraints = [
        ('unique_number_per_club', 'unique(club_id, number)', '¡El dorsal debe ser único por club!')
    ]

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                record.age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
            else:
                record.age = 0

    @api.depends('salary')
    def _compute_is_star(self):
        for record in self:
            record.is_star = record.salary > 1000000

    @api.constrains('salary')
    def _check_salary(self):
        for record in self:
            if record.salary < 0:
                raise models.ValidationError("El salario no puede ser negativo.")
