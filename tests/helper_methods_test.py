import unittest
from mock import patch
from plugins.food_bot_plugin import Helper
from config import Config
from datetime import datetime


class HelperMethodsTest(unittest.TestCase):

    @patch('plugins.food_bot_plugin.datetime')
    @patch.dict(Config.config_dict, {'WEEK': 'A'})
    def test_config_week_A_returns_right_option_when_week_is_0(self, mock_date):
        mock_date.now.return_value = datetime(2016, 4, 20, 11, 11, 16, 398810)
        week_number = Helper.get_week_number()
        self.assertEqual(week_number, 2)
        self.assertNotEqual(week_number, 1)
        self.assertNotEqual(week_number, 3)

    @patch('plugins.food_bot_plugin.datetime')
    @patch.dict(Config.config_dict, {'WEEK': 'A'})
    def test_config_week_A_returns_right_option_when_week_is_1(self, mock_date):
        mock_date.now.return_value = datetime(2016, 4, 25, 11, 11, 16, 398810)
        week_number = Helper.get_week_number()
        self.assertEqual(week_number, 1)
        self.assertNotEqual(week_number, 2)
        self.assertNotEqual(week_number, 3)

    @patch('plugins.food_bot_plugin.datetime')
    @patch.dict(Config.config_dict, {'WEEK': 'B'})
    def test_config_week_B_returns_right_option_when_week_is_1(self, mock_date):
        mock_date.now.return_value = datetime(2016, 4, 20, 11, 11, 16, 398810)
        week_number = Helper.get_week_number()
        self.assertEqual(week_number, 1)
        self.assertNotEqual(week_number, 2)
        self.assertNotEqual(week_number, 3)

    @patch('plugins.food_bot_plugin.datetime')
    @patch.dict(Config.config_dict, {'WEEK': 'B'})
    def test_config_week_B_returns_right_option_when_week_is_2(self, mock_date):
        mock_date.now.return_value = datetime(2016, 4, 25, 11, 11, 16, 398810)
        week_number = Helper.get_week_number()
        self.assertEqual(week_number, 2)
        self.assertNotEqual(week_number, 1)
        self.assertNotEqual(week_number, 3)

    @patch.dict(Config.config_dict, {'BREAKFAST_TIME': '07:45:00'})
    def test_config_get_meal_time_for_breakfast(self, *args):
        meal_time = Helper.get_meal_time('breakfast')
        self.assertEqual(meal_time, '07:45:00')

    @patch.dict(Config.config_dict, {'LUNCHTIME': '13:30:00'})
    def test_config_get_meal_time_for_lunch(self, *args):
        meal_time = Helper.get_meal_time('lunch')
        self.assertEqual(meal_time, '13:30:00')

    def test_no_confi_for_meal_time(self, *args):
        meal_time = Helper.get_meal_time('lunch')
        self.assertRaises('Check if you have breakfast and lunch times set')

