from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LichSu(models.Model):
    _name = 'lich_su'
    _description = 'Lịch sử công tác'

    employee_id = fields.Many2one('nhan_vien', string='Nhân viên', required=True)
    department_id = fields.Many2one('phong_ban', string='Phòng ban', required=True)
    job_title = fields.Many2one('chuc_vu', string='Chức vụ', required=True)
    start_date = fields.Date(string='Ngày bắt đầu', required=True)
    end_date = fields.Date(string='Ngày kết thúc')
    is_current = fields.Boolean(string='Công tác hiện tại')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date and record.end_date < record.start_date:
                raise ValidationError("Ngày kết thúc không thể nhỏ hơn ngày bắt đầu!")