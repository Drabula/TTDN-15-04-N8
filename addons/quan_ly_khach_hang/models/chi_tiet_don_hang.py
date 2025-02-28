from odoo import models, fields, api

class ChiTietDonHang(models.Model):
    _name = 'chi_tiet_don_hang'
    _description = 'Chi tiết đơn hàng'
    
    order_id = fields.Many2one('don_hang_khach_hang', string='Đơn hàng', required=True)
    
    product_id = fields.Many2one('chi_tiet_san_pham', string='Tên sản phẩm', required=True)
    
    price_unit = fields.Float(string='Đơn giá', related='product_id.price_unit', store=True, readonly=True)
    
    quantity = fields.Integer(string='Số lượng', required=True, default=1)
    
    subtotal = fields.Float(string='Thành tiền', compute='_compute_subtotal', store=True)
    
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.price_unit