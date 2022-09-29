ACCOUNT_TYPE= (
    ('IN', 'In'),
    ('OU', 'Out'),   
) 

TRANSACTION_STATUS =(
    ('PAID', 'paid'),
    ('NOT_PAID', 'not paid'),
    ('PENDING', 'pending'),
)
TRANSACTION_TYPE_CHOICES= (
    ('PA', 'paiement'),
    ('SA', 'salaire '),
    ('CR', 'creance'),
    ('CH', 'charges'),   
    ('AL', 'allouer'),  
)