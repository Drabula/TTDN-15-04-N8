from odoo import models, fields, api

class ChiTietDonHang(models.Model):
    _name = 'chi_tiet_don_hang'
    _description = 'Chi tiết đơn hàng'
    _rec_name = 'chi_tiet_don_hang'
    

    order_id = fields.Many2one('sale.order', string='Đơn hàng', required=True)
    product_id = fields.Many2one('product.product', string='Sản phẩm', required=True)
    quantity = fields.Float(string='Số lượng', required=True, default=1.0)
    price_unit = fields.Float(string='Đơn giá', required=True)
    subtotal = fields.Float(string='Thành tiền', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.price_unit
