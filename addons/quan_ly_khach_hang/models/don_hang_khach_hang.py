from odoo import models, fields, api

class DonHangKhachHang(models.Model):
    _name = 'don_hang_khach_hang'
    _description = 'Đơn Hàng Khách Hàng'
    _rec_name = 'ma_don_hang'

    ma_don_hang = fields.Char("Mã đơn hàng", required=True, copy=False, readonly=True,
                              default=lambda self: self.env['ir.sequence'].next_by_code('don_hang_khach_hang'))
    ngay_dat_hang = fields.Date("Ngày đặt hàng", default=fields.Date.today)

    order_line_ids = fields.One2many('chi_tiet_don_hang', 'order_id', string="Chi tiết đơn hàng")

    tong_tien = fields.Float("Tổng tiền", compute="_compute_tong_tien", store=True, digits=(16, 2))

    trang_thai = fields.Selection([
        ('moi', "Mới"),
        ('dang_xu_ly', "Đang xử lý"),
        ('hoan_thanh', "Hoàn thành"),
        ('huy', "Hủy")
    ], string="Trạng thái", default='moi')

    khach_hang_id = fields.Many2one('thong_tin_khach_hang', string="Khách hàng", required=True)

    @api.depends('order_line_ids.subtotal')
    def _compute_tong_tien(self):
        for record in self:
            record.tong_tien = sum(record.order_line_ids.mapped('subtotal'))
