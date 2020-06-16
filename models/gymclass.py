# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gymclass(models.Model):
    _name = 'gym.gymclass'
    
    name = fields.Char('Nombre', size=64, required=True)
    start = fields.Datetime('Comienzo',required=True, autodate = True)
    end = fields.Datetime('Fin',required=True, autodate = True)
    capacity =  fields.Integer("Capacidad") 
    activityType = fields.Selection([('dance','Baile'),
                                     ('aerobic','Aerobica'),
                                     ('anaerobic','Anaerobica'),
                                     ('relax','Relax'),],
                                     'Tipo de actividad')
    
    gymuser_ids = fields.Many2many("gym.gymuser",string="Usuarios confirmados")
    gyminstructor_id = fields.Many2one('gym.gyminstructor','Instructor')
    
    @api.one
    @api.constrains('capacity')
    def _check_capacity(self):
        if self.capacity >= 50:
            raise models.ValidationError('La capacidad de la clase debe ser inferior a 50')
        
    @api.onchange('capacity','activityType')
    def onchange_gymclass(self):
        resultado = {}
        if self.capacity > 30 and self.activityType == 'dance':
            resultado = {'value': {'capacity' : 30 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Las clases de baile son para máximo 30 personas'}}
        return resultado
