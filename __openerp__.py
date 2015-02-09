{
    'name' : 'Automan Account Module',
    'version': '1.0',
    'summary': 'Account Transactions for Myanmar',
    'category': 'Accounting and Financial Management',
    'author': 'kothudevil, Myanmar',
    'description':
        """
Accounting Management for Myanmar
=================

A helpful feature for Myanmar Accounting Nature
        """,
    'data': [
        "account_view.xml",
        "advance_payment_sequence.xml",
    ],
    'depends' : ['account','hr',],
   # 'qweb': ['static/src/xml/*.xml'],
    'application': True,
    'Installable': True,
}
