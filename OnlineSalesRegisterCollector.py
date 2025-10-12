import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}
    
    # Геттер для получения значения name_items. 
    @property
    def name_items(self):
        return self.__name_items
    # Геттер для получения значения number_items.
    @property
    def number_items(self):
        return self.__number_items
    
    # Метод добавляет товары в чек.
    def add_item_to_cheque(self, name):
        if not 0 < len(name) < 40:
            raise ValueError( 'Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    # Метод  убирает товары из чека.
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__name_items -= 1

    # Метод считает общую сумму покупок.
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])

        if self.__number_items >10:
            return sum(total) * 0.9
        else:
            return sum(total)
        
    # Метод рассчитывает НДС товаров, у которых налоговая ставка 20%.
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate == 20:
                twenty_percent_tax.append(self.__name_items[item])
                total.append(self.__item_price[item])

        if self.__number_items > 10:
            return sum(total) * 0.9 * 0.2
        else:
            return sum(total) * 0.2
    
    # Метод рассчитывает НДС товаров, у которых ставка 10%.
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate == 10:
                 ten_percent_tax.append(self.__name_items[item])
                 total.append(self.__item_price[item])
        if self.__number_items > 10:
            return sum(total) * 0.9 * 0.1
        else:
            return sum(total) * 0.1
        
    # Метод возвращает общую сумму НДС по чеку.
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    # Статический методвозвращает номер телефона покупателя.
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            telephone_number = int(telephone_number)
        except ValueError:
            raise ValueError("Необходимо ввести цифры")
        if len(str(telephone_number)) > 10:
            raise ValueError('Недопустимое значение')
        telephone_number = f' +7{telephone_number}'