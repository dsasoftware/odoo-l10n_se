# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015-2016 Vertel (<http://www.vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'BgMax Format Bank Statements Import',
    'version': '8.0.0.1.0',
    'license': 'AGPL-3',
    'author': ' Vertel AB',
    'website': 'http://vertel.se',
    'category': 'Banking addons',
    'depends': ['account_bank_statement_import'],
    'summary': 'BgMax Format Bank Statements Import',
    'description': """
        Reading BgMax formated files from Bankgirocentralen.
        
        
        There are some problems with the oca class AcountBankStatementImport
        from OCA bank-statement-import/account_bank_statement_import/models/account_bank_statement_import.py
        change pop to get:
        
        140,141c140,141
<         currency_code = stmt_vals.pop('currency_code')
<         account_number = stmt_vals.pop('account_number')
---
>         currency_code = stmt_vals.get('currency_code')
>         account_number = stmt_vals.get('account_number')
328c328
<         for line_vals in stmt_vals['transactions']:
---
>         for line_vals in stmt_vals.get('transactions',[]):
380c380
<         for line_vals in stmt_vals['transactions']:
---
>         for line_vals in stmt_vals.get('transactions',[]):

        
        """,
    'installable': 'True',
    'application': 'False',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
