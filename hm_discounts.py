#!/usr/bin/python3
"""hm_discounts helps calculate certain discounts at H&M.

Copyright (C) 2019  Robert Lin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# `You're under no obligation to choose a license. However,
# without a license, the default copyright laws apply, meaning
# that you retain all rights to your source code and no one
# may reproduce, distribute, or create derivative works from your work.`
# https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#choosing-the-right-license
# Accessed: 2019-12-17.
#
# `The GNU GPLv3 also lets people do almost anything they want
# with your project, except distributing closed source versions.`
# https://choosealicense.com/  Accessed: 2019-12-17.
#
# `The Free Software Foundation recommends taking the additional
# step of adding a boilerplate notice to the top of each
# file. The boilerplate can be found at the end of the license.`
# https://choosealicense.com/licenses/gpl-3.0/  Accessed: 2019-12-17.
#
# The `GNU GENERAL PUBLIC LICENSE`, included in this project as file
# `LICENSE.txt`, comes from: https://www.gnu.org/licenses/gpl-3.0.txt
# Accessed: 2019-12-17.

import decimal
import sys

# `Constants are usually defined on a module level
# and written in all capital letters with underscores
# separating words. Examples include MAX_OVERFLOW and TOTAL.`
# https://www.python.org/dev/peps/pep-0008/#constants  Accessed:
# 2019-12-17.
TUI_ENTRY_TIPS_EN = 'Amounts are before tax.'
TUI_HOW_QUIT_EN = 'Press q to quit.'
TUI_PROMPT_EN = 'Purchase amount: '


def after13p(purchase_amount_str):
    """Calculate amount after 13% off."""

    # `Comments should be complete sentences. The first word should be
    # capitalized, unless it is an identifier that begins with a lower
    # case letter ...` https://www.python.org/dev/peps/pep-0008/#comments
    # Accessed: 2019-12-17.
    #
    # The answer should look like money, with two decimal places such as
    # "1.00".
    #
    # Problem:
    #
    # The default way Python handles numbers having a decimal place,
    # is to treat as `float` type. But multiplying two floats, can
    # result in something gaining more numbers after the decimal
    # place, such as 1.23456...  when all we want is two decimal
    # places. So round() comes to mind to try to make it two decimal
    # places. However, round() applied to float, some answers can
    # be wrong by a cent. You would expect 2.675 rounded to two
    # decimal places to be 2.68, but:  `round(2.675, 2) gives 2.67`
    # https://docs.python.org/3.7/library/functions.html#round  Accessed:
    # 2019-12-10.
    #
    # Solution:
    #
    # Use Decimal data type and its `quantize()`. Their documention
    # mentions use for rounding money.
    #
    # More info:
    #
    # `The decimal module provides support for fast
    # correctly-rounded decimal floating point arithmetic.`
    # https://docs.python.org/3.7/library/decimal.html#module-decimal
    # Accessed: 2019-11-25.
    #
    # See also in this file, the function: decimal_to_currency_str

    # User input which is string data type, convert to Decimal data type.
    purchase_amount_dec = decimal.Decimal(purchase_amount_str)

    # 0.87 used to calculate 13% off. 100% - 13% = 87%, = 0.87.
    #
    # Now that purchase_amount is a Decimal data type, multiply with
    # the decimal 0.87.
    purchase_amount_reduced_dec = purchase_amount_dec * decimal.Decimal('0.87')

    # Send to helper function that completes the rounding to currency,
    # and converts answer to a string data type. See function's comments
    # for more info.
    return decimal_to_currency_str(purchase_amount_reduced_dec)


def after13p_terse_wrapper(purchase_amount_str):
    """after13p() wrapped with additional but minimal adornment.

    Minimal formatting necessary to distinguish it from other responses.
    """
    answer = after13p(purchase_amount_str)

    # Based on `Accessing arguments by position`, with
    # .format()'s argument defined separately for clarity.
    # https://docs.python.org/3.7/library/string.html#format-examples
    # Accessed: 2019-12-17.
    #
    # Hard-coded extra spacing before colon (:) to make results'
    # horizontal positions aligned, so answers can be visually easier
    # and faster to compare.
    tpl_str = '-13%     : {0}'
    return tpl_str.format(answer)


def after5(purchase_amount_str):
    """Calculate amount after $5 off every $30.

    Examples:

    | Purchase Amount | Fits How Many 30s | Calculation         | Result  |
    | ---             | ---               | ---                 | ---     |
    | $ 29.99         | 0                 | $ 29.99 - (0 x $ 5) | $ 29.99 |
    | $ 30.01         | 1                 | $ 30.01 - (1 x $ 5) | $ 25.01 |
    | $ 60.00         | 2                 | $ 60.00 - (2 x $ 5) | $ 50.00 |

    """

    # Input is string. Convert to float, otherwise errors.
    purchase_amount_flo = float(purchase_amount_str)

    # `To do floor division and get an integer result (discarding
    # any fractional result) you can use the // operator`
    # https://docs.python.org/3.7/tutorial/introduction.html#numbers
    # Accessed: 2019-12-17.

    # BEDMAS allows omitting parenthesis in this case, but kept here for
    # clarity. When reviewing code, saves time from having to re-figure
    # out the BEDMAS sequence.

    # Problem:
    #
    # Line longer than allowed by Python PEP style.

    # Solution:
    #
    # Wrap lines.  `The preferred way of wrapping long lines is by
    # using Python's implied line continuation inside parentheses,
    # brackets and braces. Long lines can be broken over multiple
    # lines by wrapping expressions in parentheses. These should be
    # used in preference to using a backslash for line continuation.`
    # https://www.python.org/dev/peps/pep-0008/#maximum-line-length
    # Accessed: 2019-12-17.

    # Use hanging indent, so opening parenthesis `(` and then new
    # lines with indents: `Hanging indentation is a type-setting
    # style where all the lines in a paragraph are indented except
    # the first line. In the context of Python, the term is used to
    # describe a style where the opening parenthesis of a parenthesized
    # statement is the last non-whitespace character of the line, with
    # subsequent lines being indented until the closing parenthesis.`
    # https://www.python.org/dev/peps/pep-0008/#fn-hi  Accessed:
    # 2019-12-15.

    # Where to break when wish to break near operator `-`:
    #
    # `Donald Knuth explains the traditional rule in his
    # Computers and Typesetting series: "Although formulas within a
    # paragraph always break after binary operations and relations,
    # displayed formulas always break before binary operations"`
    # https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator
    # Accessed: 2019-12-17.

    # Where to place the closing `)`:
    #
    # `The closing brace/bracket/parenthesis on multiline constructs
    # may ...`
    #
    # `may be lined up under the first character
    # of the line that starts the multiline construct`
    # https://www.python.org/dev/peps/pep-0008/#indentation  Accessed:
    # 2019-12-17.
    purchase_amount_reduced_flo = (
        purchase_amount_flo
        - ((purchase_amount_flo // 30) * 5)
    )

    # Convert to decimal.
    purchase_amount_reduced_dec = decimal.Decimal(purchase_amount_reduced_flo)

    # Send to helper function that completes the rounding to currency,
    # and converts answer to a string data type. See function's comments
    # for more info.
    return decimal_to_currency_str(purchase_amount_reduced_dec)


def after5_terse_wrapper(purchase_amount_str):
    """after5() wrapped with additional but minimal adornment.

    Minimal formatting necessary to distinguish it from other responses.
    """
    answer = after5(purchase_amount_str)

    # Tilde (~) inspired by `man sed`: `first~step`.
    tpl_str = '-$5 ~$30 : {0}'
    return tpl_str.format(answer)


def calculator_loop():
    """Repeatedly ask purchase amount and calculate answer, unless quit."""
    while True:

        # Use empty print(), to put a blank line at the start of each
        # iteration.
        #
        # Without a blank line or some kind of visual separators, the user
        # of this script will see the output as a continous wall of text.
        #
        # Providing this visible separation between each iteration, not
        # only looks better, but helps make it easier to visually glance
        # over the answers if searching for a previously entered input.
        print()
        user_input = input(TUI_PROMPT_EN)
        if user_input == 'q':

            # Quit.

            # `The most direct way to
            # terminate a script is to use sys.exit().`
            # https://docs.python.org/3.7/tutorial/stdlib.html#error-output-redirection-and-program-termination
            # Accessed: 2019-12-17.
            sys.exit()
        else:
            print(
                after13p_terse_wrapper(user_input)
            )
            print(
                after5_terse_wrapper(user_input)
            )


def calculator_preamble():
    """Display brief info to the user about how to use this script."""
    print(TUI_ENTRY_TIPS_EN)
    print(TUI_HOW_QUIT_EN)


def decimal_to_currency_str(input_dec):
    """Helper to do our custom final formatting for currency."""

    # First, round to two decimal places.
    #
    # Documentation shows different ways to round. I was
    # reminded: `When working with money you usually
    # want to limit precision as late as possible so
    # things like multiplication don't aggregate rounding errors.`
    # https://stackoverflow.com/questions/7560455/decimals-to-2-places-for-money-in-python-3/7560633#7560633
    # Accessed: 2019-12-17.
    #
    # So this helper function is called last in any discount calculation,
    # to make it so that rounding happens last.

    # `The quantize() method rounds a number ... This
    # method is useful for monetary applications that
    # often round results to a fixed number of places ... `
    # https://docs.python.org/3.7/library/decimal.html#quick-start-tutorial
    # Accessed: 2019-11-25.

    # `decimal.ROUND_HALF_UP`
    #
    # `Round to nearest with ties going away from zero.`
    # https://docs.python.org/3.7/library/decimal.html#rounding-modes
    # Accessed: 2019-11-26.
    input_dec = input_dec.quantize(
        decimal.Decimal('.01'),
        decimal.ROUND_HALF_UP
    )

    # Use str() to convert to string.
    #
    # `Doug McIlroy, the inventor of Unix pipes ...`: `Write programs
    # to handle text streams, because that is a universal interface.`
    # http://www.catb.org/~esr/writings/taoup/html/ch01s06.html  Accessed:
    # 2019-12-17.
    #
    # So convert "Decimal" format answer to text string, to be easier
    # for whatever has to receive the output of this function.
    #
    # For example a testing function would benefit. Otherwise, if testing
    # also had to check output format is a Decimal, what happens if there
    # are future changes of the data format to something else other than
    # Decimal? The test would also require updating to that new format
    # to be consistent.

    # Instead, keep things simple, just output text string, and let tests
    # only check text string values instead of having to also maintain
    # and match data formats.
    return str(input_dec)


# `by adding this code at the end of your module:` , `if __name__
# == "__main__":`,  `you can make the file usable as a script as
# well as an importable module, because the code that parses the
# command line only runs if the module is executed as the "main" file`
# https://docs.python.org/3.7/tutorial/modules.html#executing-modules-as-scripts
# Accessed: 2019-12-17.
if __name__ == '__main__':

    # Script detected as being run directly, not imported and run by
    # another script.

    calculator_preamble()
    calculator_loop()
