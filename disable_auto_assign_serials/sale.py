# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _action_procurement_create(self):
        res = super(SaleOrderLine, self)._action_procurement_create()
        orders = list(set(x.order_id for x in self))
        for order in orders:
            reassign = order.picking_ids.filtered(lambda x: x.state=='confirmed' or ((x.state in ['partially_available', 'waiting']) and not x.printed))
            if reassign:
                reassign.do_unreserve()
                reassign.action_assign()
                # unlink allocated serials
                order_picking_ids = order.picking_ids
                for order_picking_id in order_picking_ids:
                    order_pack_operation_ids = order_picking_id.pack_operation_ids
                    for order_pack_operation_id in order_pack_operation_ids:
                        order_pack_operation_id.pack_lot_ids.unlink()
                
                return res