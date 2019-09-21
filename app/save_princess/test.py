from unittest import TestCase

from app.save_princess.validator import Validator
from app.save_princess.save_princess import save_princess


class ValidationTest(TestCase):

    def test_multiple_mario(self):
        n = 3
        # 2 marios are not allowed
        grid = 'mm-,-x-,-p-'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_multiple_princess(self):
        n = 3
        # 2 princess are not allowed
        grid = '-m-,-x-,-pp'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_other_symbols_in_the_grid(self):
        n = 3
        # symbols other than m,p,-,x are not allowed
        grid = '-m-,-x-,-r-'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_mario_not_found(self):
        n = 3
        # one mario is mandatory - who else will save the princess?
        grid = '---,-x-,-p-'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_princess_not_found(self):
        n = 3
        # one princess is mandatory - who will save the princess?
        grid = '-m-,-x-,---'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_grid_and_grid_size(self):
        n = 3
        # one princess is mandatory - who will save the princess?
        grid = '-m-,-x-'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertFalse(is_valid_data, validate.message)

    def test_valid_input(self):
        n = 3
        # valid grid
        grid = '-m-,-x-,-p-'
        validate = Validator(n, grid)
        is_valid_data = validate.validate()
        self.assertTrue(is_valid_data, validate.message)


class SavePrincessTest(TestCase):

    def test_valid_game(self):
        n = 3
        # valid grid
        grid = '--m,-x-,-p-'
        error_code, path = save_princess(n, grid)
        self.assertFalse(error_code)
        self.assertEqual(path, ['DOWN', 'DOWN', 'LEFT'])

    def test_invalid_game(self):
        n = 3
        # invalid grid
        grid = '-mm,-x-,-p-'
        error_code, path = save_princess(n, grid)
        self.assertTrue(error_code)
        self.assertEqual(path, [])

    def test_possible_path(self):
        n = 3
        # valid grid
        grid = '-m-,-x-,-p-'
        error_code, path = save_princess(n, grid)
        self.assertFalse(error_code)
        self.assertEqual(path, ['LEFT', 'DOWN', 'DOWN', 'RIGHT'])

    def test_no_possible_path(self):
        n = 3
        # valid grid
        grid = '-m-,xxx,-p-'
        error_code, path = save_princess(n, grid)
        self.assertFalse(error_code)
        self.assertEqual(path, [])
