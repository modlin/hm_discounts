"""Unit tests for hm_discounts.py"""
import unittest
import hm_discounts


class TestAfter13P(unittest.TestCase):
    """Test support for amount after 13% off."""

    def test_after13p_correct(self):
        """After 13% off answer is correctly rounded to two decimal places."""
        self.assertEqual(
            hm_discounts.after13p('29.99'),
            '26.09'
        )
        self.assertEqual(
            hm_discounts.after13p('89.99'),
            '78.29'
        )

        # We can calculate 13% off by: input * (100% - 13%) or input * 87%.
        #
        # Using non-Python calculator for example `bc`, we find:
        #
        # bc <<< 'scale=100;3.074712643678161 * 0.87'
        #
        # 2.67500000000000007
        #
        # We expect that rounding this to two decimal places, it should
        # always be: `2.68`.
        #
        # But in Python:
        #
        # >>> 3.074712643678161 * 0.87
        #
        # 2.675
        #
        # >>> round(3.074712643678161 * 0.87 , 2)
        #
        # 2.67
        #
        # Python's answer for the multiplication (product) is different,
        # being `2.675`, but more importantly for our purposes, when
        # round() to two decimal places, it is an unexpected `2.67`.
        #
        # So if our function outputs 2.68, I would feel assured the
        # function is using the right rounding method, rounding correctly.
        self.assertEqual(
            hm_discounts.after13p('3.074712643678161'),
            '2.68'
        )

    def test_after13p_terse_correct(self):
        """Amount after 13% off terse wrapper returns correct string."""

        # Since after13p_terse_wrapper() uses p13p(), these indirectly
        # test after13p() as well.
        self.assertEqual(
            hm_discounts.after13p_terse_wrapper('2.99'),
            '-13%     : 2.60'
        )
        self.assertEqual(
            hm_discounts.after13p_terse_wrapper('100'),
            '-13%     : 87.00'
        )

    def test_after13p_zero(self):
        """Input 0 returns 0.00."""

        # Input is type `string`, to simulate user input being a string.
        #
        # Output is 0 but in money format 0.00.
        self.assertEqual(
            hm_discounts.after13p('0'),
            '0.00'
        )


class TestAfter5(unittest.TestCase):
    """Test support for amount after $5 off every $30."""

    def test_after5_terse_correct(self):
        """Amount after $5 off terse wrapper returns correct string."""

        # Where x < $30. Reaches $30 zero times, so (0 * 5) = $0 off.
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('1'),
            '-$5 ~$30 : 1.00'
        )
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('29.99'),
            '-$5 ~$30 : 29.99'
        )

        # Where $30 <= x < $60. Reaches $30 once, so (1 * 5) = $5 off.
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('30'),
            '-$5 ~$30 : 25.00'
        )
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('59.99'),
            '-$5 ~$30 : 54.99'
        )

        # Where $60 <= x < $90. Reaches $30 twice, so (2 * 5) = $10 off.
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('60'),
            '-$5 ~$30 : 50.00'
        )
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('89.99'),
            '-$5 ~$30 : 79.99'
        )

        # Where $90 <= x < $120. Reaches $30 three times, so (3 * 5) =
        # $15 off.
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('100'),
            '-$5 ~$30 : 85.00'
        )
        self.assertEqual(
            hm_discounts.after5_terse_wrapper('119.99'),
            '-$5 ~$30 : 104.99'
        )

    def test_after5_zero(self):
        """Input 0 returns 0.00."""
        self.assertEqual(
            hm_discounts.after5('0'),
            '0.00'
        )


class TestTUITexts(unittest.TestCase):
    """Test textual user interface texts."""

    def test_tui_entry_tips_en_correct(self):
        """Initial prompt text correct."""
        self.assertEqual(
            hm_discounts.TUI_ENTRY_TIPS_EN,
            'Amounts are before tax.'
        )

    def test_tui_how_quit_en_correct(self):
        """Initial prompt text correct."""
        self.assertEqual(
            hm_discounts.TUI_HOW_QUIT_EN,
            'Press q to quit.'
        )

    def test_tui_prompt_en_correct(self):
        """Iteration prompt text correct."""
        self.assertEqual(
            hm_discounts.TUI_PROMPT_EN,
            'Purchase amount: '
        )
