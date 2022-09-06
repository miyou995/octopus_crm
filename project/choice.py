PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
)

CONTRACT_TYPE_CHOICES = (
    ('H', 'hosting'),
    ('A', 'annual'),
    ('S', 'semi-annual'),
    ('Q', 'quarterly'),
    ('AD', 'adverisement'),
)

STATUS_TYPE_CHOICES= (
    ('CF', 'Confirm'),
    ('CP', 'Completed'),
    ('PE', 'Pending'),
    ('CA', 'Cancelled'),
) 

# Create your models here.

TRANSACTION_TYPE_CHOICES= (
    ('PA', 'paiement'),
    ('SA', 'salaire '),
    ('CR', 'creance'),
    ('CH', 'charges'),   
    ('AL', 'allouer'),  
) 