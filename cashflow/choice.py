ACCOUNT_TYPE= (
    ('IN', 'In'),
    ('OU', 'Out'),   
) 

TRANSACTION_STATUS =(
    ('payed', 'PAYED'),
    ('not payed', 'NOT_PAYED'),
    ('pending', 'PENDING'),
)
TRANSACTION_TYPE_CHOICES= (
    ('PA', 'paiement'),
    ('SA', 'salaire '),
    ('CR', 'creance'),
    ('CH', 'charges'),   
    ('AL', 'allouer'),  
)