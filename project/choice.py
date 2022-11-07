PROJECT_TYPE_CHOICES = (
    ('E-COMMERCE', 'e-commerce'),
    ('WEB SITE', 'web site'),
    ('WEB APP', 'web app'),
)

CONTRACT_TYPE_CHOICES = (
    ('HOSTING', 'hosting'),
    ('ANNUAL', 'annual'),
    ('SEMI-ANNUAL', 'semi-annual'),
    ('QUARTERLY', 'quarterly'),
    ('ADVERTISEMENT', 'advertisement'),
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