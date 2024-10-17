import re
from sympy import isprime

VALID_ROLES = ["Admin", "Member", "External"]

def validate_claims(decoded_token):
    name = decoded_token.get("Name")
    role = decoded_token.get("Role")
    seed = decoded_token.get("Seed")
    
    if not name or not isinstance(name, str) or len(name) > 256 or re.search(r'\d', name):
        raise ValueError("Invalid 'Name' claim")
    
    if role not in VALID_ROLES:
        raise ValueError("Invalid 'Role' claim")
    
    if not isinstance(seed, int) or not isprime(seed):
        raise ValueError("Invalid 'Seed' claim")
