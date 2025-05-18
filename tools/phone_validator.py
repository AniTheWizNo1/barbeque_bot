import re

def validate_phone_number(phone: str) -> bool:
    """Validate that the phone number is exactly 10 digits."""
    return bool(re.fullmatch(r'\d{10}', phone))

def format_phone_number(phone: str) -> str:
    """Format phone number like 9-8-7, 6-5-4, 3-2-1"""
    return '-'.join([phone[i:i+3] for i in range(0, len(phone), 3)])
 
