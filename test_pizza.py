import pytest
from pizza import Pizza, Pepperoni, Margherita, Hawaiian


def test_can_pizza_create_class_with_right_dict():
    """Class pizza has right dict"""
    expected = {
        'good mood': 1000,
        'tomato sauce': 100,
        'mozzarella': 50
    }
    my_pizza = Pizza()
    my_pizza_consist_from = my_pizza.dict()
    assert my_pizza_consist_from == expected, (
        'test_can_pizza_create_class_with_right_dict() works incorrectly'
    )


def test_can_pizza_create_class_with_right_size():
    """Class pizza has right size"""
    expected = 'XL'
    my_pizza = Pizza('XL')
    assert my_pizza.size == expected, (
        'test_can_pizza_create_class_with_right_size() works incorrectly'
    )


def test_can_pizza_create_class_with_right_basic_size_2():
    """Class pizza has right size"""
    expected = 'L'
    my_pizza = Pizza()
    assert my_pizza.size == expected, (
        'test_can_pizza_create_class_with_right_size_2() works incorrectly'
    )


def test_can_compare_two_pizzas():
    assert Margherita() == Margherita(), (
        'test_can_compare_two_pizzas() works incorrectly'
    )


def test_can_compare_two_pizzas_2():
    assert Pepperoni() != Pepperoni('XL'), (
        'test_can_compare_two_pizzas_2() works incorrectly'
    )


def test_can_compare_two_pizzas_3():
    assert Pepperoni() != Hawaiian(), (
        'test_can_compare_two_pizzas_3() works incorrectly'
    )


def test_can_pizza_create_right_pepperoni():
    """Class pizza has right dict"""
    expected = {
        'good mood': 3000,
        'tomato sauce': 300,
        'mozzarella': 150,
        'pepperoni': 126
    }
    my_pizza = Pepperoni('XL')
    my_pizza_consist_from = my_pizza.dict()
    assert my_pizza_consist_from == expected, (
        'test_can_pizza_create_right_pepperoni() works incorrectly'
    )


def test_can_pizza_create_right_hawaiian():
    """Class pizza has right dict"""
    expected = {
        'good mood': 1000,
        'tomato sauce': 100,
        'mozzarella': 50,
        'chicken': 111,
        'pineapples': 500}
    my_pizza = Hawaiian()
    my_pizza_consist_from = my_pizza.dict()
    assert my_pizza_consist_from == expected, (
        'test_can_pizza_create_right_hawaiian() works incorrectly'
    )


def test_can_pizza_create_right_margherita():
    """Class pizza has right dict"""
    expected = {
        'good mood': 1000,
        'tomato sauce': 100,
        'mozzarella': 50,
        'tomatoes': 20
    }
    my_pizza = Margherita()
    my_pizza_consist_from = my_pizza.dict()
    assert my_pizza_consist_from == expected, (
        'test_can_pizza_create_right_margherita() works incorrectly'
    )
