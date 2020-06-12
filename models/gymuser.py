# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gymuser(models.Model):
    _name = 'gym.gymuser'
    
    name = fields.Char('Nombre', size = 60, required = True)
    idcard = fields.Char('ID Tarjeta', size = 9, required = True)
    photo = fields.Binary('Foto')