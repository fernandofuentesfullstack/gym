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