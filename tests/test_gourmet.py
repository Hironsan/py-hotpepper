# -*- coding: utf-8 -*-
from unittest import TestCase
from hotpepper.gourmet import Gourmet, Shop, Budget, LargeServiceArea,\
    ServiceArea, LargeArea, MiddleArea, SmallArea, Genre, FoodCategory,\
    Food, CreditCard, Special, SpecialCategory


class TestGourmet(TestCase):

    def test_gourmet(self):
        gourmet = Gourmet(api_key='')
        response = gourmet.send(keyword='ラーメン')
        self.assertTrue(isinstance(response, dict))

    def test_shop(self):
        shop = Shop()
        response = shop.send()
        self.assertTrue(isinstance(response, dict))

    def test_budget(self):
        budget = Budget()
        response = budget.send()
        self.assertTrue(isinstance(response, dict))

    def test_large_service_area(self):
        large_service_area = LargeServiceArea()
        response = large_service_area.send()
        self.assertTrue(isinstance(response, dict))

    def test_service_area(self):
        service_area = ServiceArea()
        response = service_area.send()
        self.assertTrue(isinstance(response, dict))

    def test_large_area(self):
        large_area = LargeArea()
        response = large_area.send()
        self.assertTrue(isinstance(response, dict))

    def test_middle_area(self):
        middle_area = MiddleArea()
        response = middle_area.send()
        self.assertTrue(isinstance(response, dict))

    def test_small_area(self):
        small_area = SmallArea()
        response = small_area.send()
        self.assertTrue(isinstance(response, dict))

    def test_genre(self):
        genre = Genre()
        response = genre.send()
        self.assertTrue(isinstance(response, dict))

    def test_food_category(self):
        food_category = FoodCategory()
        response = food_category.send()
        self.assertTrue(isinstance(response, dict))

    def test_food(self):
        food = Food()
        response = food.send()
        self.assertTrue(isinstance(response, dict))

    def test_credit_card(self):
        credit_card = CreditCard()
        response = credit_card.send()
        self.assertTrue(isinstance(response, dict))

    def test_special(self):
        special = Special()
        response = special.send()
        self.assertTrue(isinstance(response, dict))

    def test_special_category(self):
        special_category = SpecialCategory()
        response = special_category.send()
        self.assertTrue(isinstance(response, dict))
