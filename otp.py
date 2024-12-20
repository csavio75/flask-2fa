import pyotp

KEY = 'ITVX2E4V7BXMB5RWG3O3LFZXAAXL76IJ'


def generate_otp(user):
    totp = pyotp.TOTP(KEY)
    auth_str = totp.provisioning_uri(name=user, issuer_name='Secure App')
    return auth_str


def verify_otp(code):
    totp = pyotp.TOTP(KEY)
    current_otp = totp.now()
    if current_otp == code:
        return True
    else:
        return False
