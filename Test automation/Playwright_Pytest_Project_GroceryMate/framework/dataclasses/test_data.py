from framework.dataclasses.data_object_user import User
from framework.dataclasses.data_objects_address import Address
from framework.dataclasses.data_object_paymentdata import PaymentCard

class TestUsers:
    """Vordefinierte User für Tests"""
    EXISTING = User.from_config('existing_user')
    INVALID = User.from_config('invalid_user')


class TestCheckout:
    """Vordefinierte Checkout-Daten für Tests"""
    VALID_ADDRESS = Address.from_config('valid_address')
    VALID_PAYMENT = PaymentCard.from_config('valid_payment')
    INVALID_CARD = PaymentCard.from_config('invalid_card')