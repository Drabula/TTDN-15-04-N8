from odoo import models, fields, api

class Dashboard(models.Model):
    _name = 'dashboard'
    _description = 'Dashboard Tổng Quan'

    # Các trường thống kê
    tong_so_khach = fields.Integer("Tổng số khách hàng", compute="_compute_tong_so_khach", store=True)
    tong_doanh_thu = fields.Float("Tổng doanh thu", compute="_compute_tong_doanh_thu", store=True)
    tong_so_lan_ho_tro = fields.Integer("Tổng số lần hỗ trợ", compute="_compute_tong_so_lan_ho_tro", store=True)
    nhan_vien_ho_tro_nhieu_nhat = fields.Many2one('nhan_vien', string="Nhân viên hỗ trợ nhiều nhất", compute="_compute_nhan_vien_ho_tro_nhieu_nhat", store=True)

    # Các trường số lượng khách theo từng miền
    so_luong_khach_bac = fields.Integer("Số lượng khách miền Bắc", compute="_compute_so_luong_khach_bac", store=True)
    so_luong_khach_trung = fields.Integer("Số lượng khách miền Trung", compute="_compute_so_luong_khach_trung", store=True)
    so_luong_khach_nam = fields.Integer("Số lượng khách miền Nam", compute="_compute_so_luong_khach_nam", store=True)

    # Các trường tổng chi tiêu của từng miền
    tong_chi_tieu_bac = fields.Float("Tổng chi tiêu miền Bắc", compute="_compute_tong_chi_tieu_bac", store=True)
    tong_chi_tieu_trung = fields.Float("Tổng chi tiêu miền Trung", compute="_compute_tong_chi_tieu_trung", store=True)
    tong_chi_tieu_nam = fields.Float("Tổng chi tiêu miền Nam", compute="_compute_tong_chi_tieu_nam", store=True)


    # Các phương thức tính toán
    def _compute_tong_so_khach(self):
        for record in self:
            record.tong_so_khach = self.env['phan_tich_khach_hang_theo_mien'].search_count([])

    def _compute_tong_doanh_thu(self):
        for record in self:
            record.tong_doanh_thu = sum(self.env['phan_tich_khach_hang_theo_mien'].search([]).mapped('tong_doanh_thu'))

    def _compute_tong_so_lan_ho_tro(self):
        for record in self:
            record.tong_so_lan_ho_tro = sum(self.env['thong_ke_ho_tro_nhan_vien'].search([]).mapped('so_lan_ho_tro'))

    def _compute_nhan_vien_ho_tro_nhieu_nhat(self):
        for record in self:
            nhan_vien_ho_tro_nhieu_nhat = self.env['thong_ke_ho_tro_nhan_vien'].search([], order='so_lan_ho_tro desc', limit=1)
            record.nhan_vien_ho_tro_nhieu_nhat = nhan_vien_ho_tro_nhieu_nhat.nhan_vien_id

    # Các phương thức tính toán số lượng khách hàng cho từng miền
    def _compute_so_luong_khach_bac(self):
        for record in self:
            phan_tich_bac = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'bac')], limit=1)
            record.so_luong_khach_bac = phan_tich_bac.so_luong_khach if phan_tich_bac else 0

    def _compute_so_luong_khach_trung(self):
        for record in self:
            phan_tich_trung = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'trung')], limit=1)
            record.so_luong_khach_trung = phan_tich_trung.so_luong_khach if phan_tich_trung else 0

    def _compute_so_luong_khach_nam(self):
        for record in self:
            phan_tich_nam = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'nam')], limit=1)
            record.so_luong_khach_nam = phan_tich_nam.so_luong_khach if phan_tich_nam else 0

    # Các phương thức tính tổng chi tiêu cho từng miền
    def _compute_tong_chi_tieu_bac(self):
        for record in self:
            phan_tich_bac = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'bac')], limit=1)
            record.tong_chi_tieu_bac = phan_tich_bac.tong_doanh_thu if phan_tich_bac else 0

    def _compute_tong_chi_tieu_trung(self):
        for record in self:
            phan_tich_trung = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'trung')], limit=1)
            record.tong_chi_tieu_trung = phan_tich_trung.tong_doanh_thu if phan_tich_trung else 0

    def _compute_tong_chi_tieu_nam(self):
        for record in self:
            phan_tich_nam = self.env['phan_tich_khach_hang_theo_mien'].search([('vung_mien', '=', 'nam')], limit=1)
            record.tong_chi_tieu_nam = phan_tich_nam.tong_doanh_thu if phan_tich_nam else 0

    def _compute_xep_hang_khach_hang(self):
        for record in self:
            top_ranked_customer = self.env['bang_xep_hang_khach_hang'].search([], order='xep_hang asc', limit=1)
            record.xep_hang_khach_hang = top_ranked_customer.khach_hang_id



    def cap_nhat_dashboard(self):
        """ Cập nhật dữ liệu Dashboard """
        phan_tich_records = self.env['phan_tich_khach_hang_theo_mien'].search([])

        for record in self:
            # Tính toán tổng số khách hàng và tổng doanh thu từ dữ liệu Phân Tích Khách Hàng
            total_customers = sum(phan_tich.so_luong_khach for phan_tich in phan_tich_records)
            total_revenue = sum(phan_tich.tong_doanh_thu for phan_tich in phan_tich_records)

            # Cập nhật các trường trong Dashboard
            record.tong_so_khach = total_customers
            record.tong_doanh_thu = total_revenue

        # Cập nhật các trường khác
        self._compute_tong_so_lan_ho_tro()
        self._compute_nhan_vien_ho_tro_nhieu_nhat()
        self._compute_so_luong_khach_bac()
        self._compute_so_luong_khach_trung()
        self._compute_so_luong_khach_nam()
        self._compute_tong_chi_tieu_bac()
        self._compute_tong_chi_tieu_trung()
        self._compute_tong_chi_tieu_nam()

