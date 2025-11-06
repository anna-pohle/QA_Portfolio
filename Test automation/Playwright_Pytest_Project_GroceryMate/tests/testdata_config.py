from framework.data_objects import User, Address, PaymentCard
from framework.utils import FileUtils

class AuthData:
    #Testdaten für Registrierung & Login

    # Lade YAML beim Import; gibt dict-format aus
    _yaml_data = FileUtils.read_yaml("testuser_data.yaml")

    # Erstelle Testuser-Datenobjekte; entpackt das dict
    EXISTING_USER = User(**_yaml_data['existing_user'])
    INVALID_USER = User(**_yaml_data['invalid_user'])

    @staticmethod
    def new_user() -> User:
        """Generiert neuen User bei jedem Aufruf"""
        return User.generate_new_user()


class CheckoutData:
    #Testdaten für Checkout

    # Lade YAML beim Import; gibt dict-format aus
    _yaml_data = FileUtils.read_yaml("testcheckout_data.yaml")

    # Erstelle Checkout-Datenobjekte aus YAML; entpackt das dict
    VALID_ADDRESS = Address(**_yaml_data['valid_address'])
    VALID_PAYMENT = PaymentCard(**_yaml_data['valid_payment'])
    INVALID_CARD = PaymentCard(**_yaml_data['invalid_card'])