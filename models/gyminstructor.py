# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gyminstructor(models.Model):
    _name = 'gym.gyminstructor'
    
    name = fields.Char('Nombre', size = 60, required = True)
    idcard = fields.Char('ID Tarjeta', size = 9, required = True)
    photo = fields.Binary('Foto')
    
    gymclass_ids = fields.One2many('gym.gymclass','gyminstructor_id','Clases')