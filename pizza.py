class Pizza:
    """Base class for pizza"""
    sizes = {
        'L': 1,
        'XL': 3
    }

    def __init__(self, size: str = 'L'):
        self.size = size
        self.ingredients = {
            'good mood': 1000,
            'tomato sauce': 100,
            'mozzarella': 50
        }
        self.emoji = None

    def dict(self) -> dict:
        """Return pizza recipe in dictionary format"""
        result = {}
        for key, value in self.ingredients.items():
            result[key] = Pizza.sizes[self.size] * value
        return result

    def __hash__(self):
        return hash((self.ingredients, self.size))

    def __eq__(self, other):
        if isinstance(other, Pizza):
            return (self.ingredients == other.ingredients) and\
                (self.size == other.size)
        raise TypeError('You have to compare pizza with another pizza')


class Margherita(Pizza):
    """Class for Margherita pizza"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.emoji = ' 🧀'
        self.ingredients['tomatoes'] = 20


class Pepperoni(Pizza):
    """Class for Pepperoni pizza"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.emoji = ' 🍕'
        self.ingredients['pepperoni'] = 42


class Hawaiian(Pizza):
    """Class for Hawaiian pizza"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.emoji = ' 🍍'
        self.ingredients['chicken'] = 111
        self.ingredients['pineapples'] = 500
