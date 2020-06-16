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
    
    _sql_constraints = [('gymuser_idcard_unique','UNIQUE (idcard)','El idcard debe ser único')]
    
    @api.one
    def btn_submit_to_admitido(self):
        self.write({'state':'admitido'})

    @api.one
    def btn_submit_to_cancelado(self):
        self.write({'state':'cancelado'})
        #Ademas hay que borrar todos las clases reservadas
        #para fechas posteriores al momento de la cancelación
        hoy = fields.Date.context_today(self)
        _logger.debug("HOY " + str(hoy))
        _logger.debug("usuario cancelado " + str(self.name))
        
        for clase in self.gymclass_ids:
            _logger.debug("Clase.start " + str(clase.start))
            if clase.start > hoy:
            #Borrar registro
                _logger.debug("Clase a borrar " + str(clase.id))
                self.write({'gymclass_ids': [ (3, clase.id ) ] })

    @api.onchange('gymclass_ids')
    def onchange_gymclass(self):
        if self.state != 'admitido':
            raise models.ValidationError('El usuario debe estar admitido para apuntarlo a una clase')

