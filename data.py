from datetime import datetime, timedelta


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

day_after_tomorrow = (
    datetime.now() + timedelta(days=2)
).strftime("%d.%m.%Y")


ORDER_DATA = [
    (
        "top",
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, улица Ленина, 10",
            "metro": "Пражская",
            "phone": "+79991234567",
            "date": tomorrow,
            "period": "трое суток",
            "color": "black",
            "comment": "Позвонить перед доставкой"
        }
    ),
    (
        "bottom",
        {
            "name": "Анна",
            "surname": "Петрова",
            "address": "Москва, улица Мира, 15",
            "metro": "Сокольники",
            "phone": "+79997654321",
            "date": day_after_tomorrow,
            "period": "двое суток",
            "color": "grey",
            "comment": "Доставить после 18:00"
        }
    )
]