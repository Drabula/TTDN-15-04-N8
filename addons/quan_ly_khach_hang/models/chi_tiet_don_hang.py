from odoo import models, fields, api

class ChiTietDonHang(models.Model):
    _name = 'chi_tiet_don_hang'
    _description = 'Chi tiết đơn hàng'
    
    # Liên kết đến model Đơn Hàng Khách Hàng thay vì sale.order
    order_id = fields.Many2one('don_hang_khach_hang', string='Đơn hàng', required=True)
    
    # Thay vì chọn sản phẩm từ product.product, người dùng sẽ nhập tên sản phẩm thủ công
    product_name = fields.Char(string='Tên sản phẩm', required=True)
    
    quantity = fields.Float(string='Số lượng', required=True, default=1.0)
    price_unit = fields.Float(string='Đơn giá', required=True)
    subtotal = fields.Float(string='Thành tiền', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.price_unit
