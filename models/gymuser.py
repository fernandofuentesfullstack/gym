# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gymuser(models.Model):
    _name = 'gym.gymuser'
    
    name = fields.Char('Nombre', size = 60, required = True)
    idcard = fields.Char('ID Tarjeta', size = 9, required = True)
    photo = fields.Binary('Foto')
    
    gymclass_ids = fields.Many2many('gym.gymclass', string = 'Reserva de clases')
    state = fields.Selection([('solicitante','Solicitante'),
                              ('admitido','Admitido'),
                              ('cancelado','Cancelado'),],
                              'Estado',
                              default='solicitante')
    
    @api.one
    def btn_submit_to_admitido(self):
        self.write({'state':'admitido'})

    @api.one
    def btn_submit_to_cancelado(self):
        self.write({'state':'cancelado'})

    @api.onchange('gymclass_ids')
    def onchange_gymclass(self):
        if self.state != 'admitido':
            raise models.ValidationError('El usuario debe estar admitido para apuntarlo a una clase')