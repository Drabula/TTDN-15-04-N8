from odoo import models, fields, api

class PhanTichKhachHang(models.Model):
    _name = 'phan_tich_khach_hang_theo_mien'
    _description = 'Phân Tích Khách Hàng Theo Miền'

    vung_mien = fields.Selection(
        [('bac', 'Miền Bắc'), ('trung', 'Miền Trung'), ('nam', 'Miền Nam')],
        string="Vùng miền",
        required=True
    )
    so_luong_khach = fields.Integer("Số lượng khách hàng", compute="_compute_so_luong_khach", store=True)
    tong_doanh_thu = fields.Float("Tổng doanh thu", compute="_compute_tong_doanh_thu", store=True)

    @api.depends('vung_mien')
    def _compute_tong_doanh_thu(self):
        for record in self:
            record.tong_doanh_thu = sum(
                self.env['thong_tin_khach_hang'].search([('vung_mien', '=', record.vung_mien)]).mapped('tong_tien_chi_tieu')
            )

    @api.depends('vung_mien')
    def _compute_so_luong_khach(self):
        for record in self:
            record.so_luong_khach = self.env['thong_tin_khach_hang'].search_count([('vung_mien', '=', record.vung_mien)])

    def cap_nhat_du_lieu_phan_tich(self):
        """ Cập nhật dữ liệu khi khách hàng thay đổi """
        for vung in ['bac', 'trung', 'nam']:
            phan_tich = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', vung)])
            if not phan_tich:
                phan_tich = self.create({'vung_mien': vung})
            phan_tich._compute_so_luong_khach()
            phan_tich._compute_tong_doanh_thu()

