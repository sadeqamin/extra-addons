# -*- coding: utf-8 -*-
# Part of WR Ltd development.

from odoo import api, models



 class Picking(models.Model):
    _inherit = "stock.picking"
    
    @api.multi
    def action_assign(self):
        """ Check availability of picking moves.
        This has the effect of changing the state and reserve quants on available moves, and may
        also impact the state of the picking as it is computed based on move's states.
        @return: True
        """
        self.filtered(lambda picking: picking.state == 'draft').action_confirm()
        moves = self.mapped('move_lines').filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))
        if not moves:
            raise UserError(_('Nothing to check the availability for.'))
        moves.action_assign()
        for order_picking_id in self:
            order_pack_operation_ids = order_picking_id.pack_operation_ids
            for order_pack_operation_id in order_pack_operation_ids:
                order_pack_operation_id.pack_lot_ids.unlink()

        
        return True
