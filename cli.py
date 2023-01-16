import click
from pizza import Pizza
from decorators import log


@log('🥘 The best pizza of size {} was made in {} seconds!')
def bake(pizza: Pizza) -> None:
    """Making pizza"""
    pass


@log('🛵 The best pizza of size {} was delivered in {} seconds!')
def deliver(pizza: Pizza) -> None:
    """Delivering pizza"""
    pass


@log('🛵 The best pizza of size {} was taken away in {} seconds!')
def pickup(pizza: Pizza) -> None:
    """Pickup pizza"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='By courier')
@click.option('--size', default='L', help='Choose the size of your pizza')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    """Cooking and Delivery"""
    stock = {sub.__name__: sub for sub in Pizza.__subclasses__()}
    if pizza not in stock.keys():
        print('We dont have this pizza. Plz, make your choice from the menu')
    chosen_pizza = stock[pizza]
    chosen_pizza.size = size
    bake(chosen_pizza)
    if delivery:
        deliver(chosen_pizza)
    else:
        pickup(chosen_pizza)


@cli.command()
def menu():
    """Ask for a menu"""
    for sub in Pizza.__subclasses__():
        elems = list(sub().ingredients.keys())
        print(f'- {sub.__name__}{sub().emoji}: {", ".join(elems)}', end='\n')


if __name__ == '__main__':
    cli()
