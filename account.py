from openerp import api,fields,models
from openerp.api import Environment

class account_advance(models.Model):
    _name='account.advance'

    name=fields.Char(string='Advance Sequence',size=124,readonly=True)
    adv_date=fields.Date()
    employee = fields.Many2one('hr.employee',string='Employee',required="True")
    ref = fields.Char(string='Reference',size=124)
    adv_journal = fields.Many2one('account.journal',string='Advance Journal',required="True")
    total = fields.Float(digits=(9,2),string='Total Advance')
    advance_line_ids=fields.One2many('account.advance.line','advance_id',string='Advance Details')
    state = fields.Selection([
        ('draft',"Draft"),
        ('paid',"Paid"),
        ('clear',"Cleared"),
        ],default='draft')

    _defaults={
        'name': lambda obj,cr,uid,context: obj.pool.get('ir.sequence').get(cr,uid,'account.advance'),
    }

    @api.multi
    def make_payment(self):
        tmp={'state':'paid'}
        line_obj=self.pool.get('account.advance.line')
        self.write(tmp)
        self.advance_line_ids.write(tmp)


    @api.multi
    def make_clearance(self):
        tmp={'state':'clear'}
        line_obj=self.pool.get('account.advance.line')
        self.write(tmp)
        self.advance_line_ids.write(tmp)

account_advance()

class account_advance_line(models.Model):
    _name='account.advance.line'

    advance_id=fields.Many2one('account.advance',ondelete='cascade',select=True,string='Advance Reference')
    name=fields.Char('Description',size=124,required=True)
    amount=fields.Float(digits=(9,2),string='Amount')
    clr_amount=fields.Float(digits=(9,2),string='Clearance Amount')
    state = fields.Selection([
        ('draft',"Draft"),
        ('paid',"Paid"),
        ('clear',"Cleared"),
        ],default='draft')
account_advance_line()


class hr_employee(models.Model):
    _name='hr.employee'
    _inherit='hr.employee'

    adv_acc_id=fields.Many2one('account.account','Advance Account')

hr_employee()
