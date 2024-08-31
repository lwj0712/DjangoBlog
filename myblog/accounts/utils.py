# utils.py
import dns.resolver
from django.core.exceptions import ValidationError

def validate_email_domain(email):
    """
    Check if the domain of the email address has a valid MX record.
    """
    domain = email.split('@')[-1]
    try:
        dns.resolver.resolve(domain, 'MX')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        raise ValidationError(f"'{domain}'은(는) 유효하지 않은 이메일 도메인입니다.")
