from address import Address
from mailing import Mailing

# Адрес получателя
to_address = Address("101000", "Москва", "Арбат", "12", "45")

# Адрес отправителя
from_address = Address("190000", "Санкт-Петербург", "Невский проспект", "1", "10")

# Создание экземпляра Mailing
mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=750,
    track="AB123456789RU"
)

# Печать информации
print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)