This script calculates discounts.  The feature I wanted, explained as a user story:

> *As a* shopper, *I want* to quickly calculate what discount I can get for each of the different coupons I have, *so that* I can choose the coupon that will save the most money.

## Demo

![Animation demonstrating input values and responses.](demo/demo.gif)

As an alternative, here is the text from the terminal animation shown above:

    $ python3 hm_discounts.py
    Amounts are before tax.
    Press q to quit.

    Purchase amount: 1
    -13%     : 0.87
    -$5 ~$30 : 1.00

    Purchase amount: 10
    -13%     : 8.70
    -$5 ~$30 : 10.00

    Purchase amount: 29.99
    -13%     : 26.09
    -$5 ~$30 : 29.99

    Purchase amount: 30
    -13%     : 26.10
    -$5 ~$30 : 25.00

    Purchase amount: 40
    -13%     : 34.80
    -$5 ~$30 : 35.00

    Purchase amount: 59.99
    -13%     : 52.19
    -$5 ~$30 : 54.99

    Purchase amount: 60
    -13%     : 52.20
    -$5 ~$30 : 50.00

    Purchase amount: q
    $

## How to run

Requirements:

* Python 3

### Computer

The general steps are:

1. Download `hm_discounts.py` script.
2. Use Python 3 to run the `hm_discounts.py` script.

Example: On Debian GNU/Linux 9.11, you can enter the following commands on a terminal (Lines beginning with `#` are comment lines for clarity, and can be omitted):

```bash
# Use Wget to download the script.
wget https://raw.githubusercontent.com/modlin/hm_discounts/master/hm_discounts.py

# Use Python 3 to run the script.
python3 hm_discounts.py
```

### Android

If you have an Android smartphone, you can get [Termux](https://wiki.termux.com). Termux runs a terminal-only, small Linux machine on Android. Once in Termux, packages can be installed that help get and run the `hm_discounts.py` script.

Tested versions:

* Android 7.0
* Python 3.7.5
* Termux 0.76
* Wget 1.20.3

Steps:

1. [Install Termux](https://wiki.termux.com/wiki/Installation).
2. Open Termux, and you'll see a terminal.
3. Enter commands:

```bash
# Install full version of Wget so you can download https URLS.
pkg install wget

# Install Python 3, by installing package: python.
pkg install python

# Use Wget to download the script.
wget https://raw.githubusercontent.com/modlin/hm_discounts/master/hm_discounts.py

# Use Python 3 to run the script.
python hm_discounts.py
```

## What problem does this solve?

There are two different coupon types:

* **13% off**
   * Can't use with any other coupon.
* **$5 off $30**
   * Purchase amount is at least $30.
   * If you have more than one of this coupon type, you can use more than one as long as each is used for every $30 that makes up the purchase amount.
   * Example with purchase amount $61:
     * Think of $61 as made of parts: $61 = $30 + $30 + $1.
     * You can use one coupon for the first $30.
     * You can use another coupon for the second $30.
     * No coupon for the $1 part.
       * This is because $1 is less than the "at least $30" requirement.
     * So you can use two of these coupons, each takes $5 off, leading to $10 off.
       * 2 x $5 off = $10 off
     * This means if originally you had to pay $61 before taxes, then by using the *$5 off $30* coupons, you only need to pay $51 before taxes.
       * $61 - $10 = $51.

Which is the best coupon type for saving money? The answer is not always the same, it depends first on the purchase amount. For some purchase amounts, one coupon type saves the most money, but for others, the other coupon type is better, as seen in this table:

| Purchase Amount | 13% off | $5 off $30 | Best Coupon Type |
| --              | --      | --         | --               |
| $1.00           | $0.87   | $1.00      | 13% off          |
| $5.00           | $4.35   | $5.00      | 13% off          |
| $10.00          | $8.70   | $10.00     | 13% off          |
| $15.00          | $13.05  | $15.00     | 13% off          |
| $20.00          | $17.40  | $20.00     | 13% off          |
| $25.00          | $21.75  | $25.00     | 13% off          |
| $29.99          | $26.09  | $29.99     | 13% off          |
| $30.00          | $26.10  | $25.00     | $5 off $30       |
| $35.00          | $30.45  | $30.00     | $5 off $30       |
| $40.00          | $34.80  | $35.00     | 13% off          |
| $45.00          | $39.15  | $40.00     | 13% off          |
| $50.00          | $43.50  | $45.00     | 13% off          |
| $55.00          | $47.85  | $50.00     | 13% off          |
| $59.99          | $52.19  | $54.99     | 13% off          |
| $60.00          | $52.20  | $50.00     | $5 off $30       |
| $65.00          | $56.55  | $55.00     | $5 off $30       |
| $70.00          | $60.90  | $60.00     | $5 off $30       |
| $75.00          | $65.25  | $65.00     | $5 off $30       |
| $80.00          | $69.60  | $70.00     | 13% off          |
| $85.00          | $73.95  | $75.00     | 13% off          |
| $89.99          | $78.29  | $79.99     | 13% off          |
| $90.00          | $78.30  | $75.00     | $5 off $30       |

So when visiting a store, after adding prices of items to get a total purchase amount, I could then start to work out which coupon type is better.

The problem was, while in the store, I didn't want to spend much time pressing buttons on a generic calculator. Also, the more buttons to press, the greater the risk of pressing something wrong so that I would need to redo calculations again. I may also notice new items of interest and want to add more items. It means I would have a new total purchase amount for which I would need to go through the same steps again. Overall I wanted a faster way to figure out the discount effect of each coupon type.

I could have prepared something like the above table with more pre-calculated answers, or used a spreadsheet app. However, I also wanted to learn Python.

My solution was to use Python to create this discounts calculation script, for use on my smartphone when visiting the store.

## Credits

* [Becoming a Data Scientist Podcast: Episode 01 - Will Kurt](https://www.youtube.com/watch?v=Jtdp_1ONy-E). Accessed 2019-12-17.
  * Instead of "grinding" through a book from beginning to end, Kurt has a productive approach to learning. This involves first browsing several books to select one that you feel works well for you. Learn a little from that book, then use that bit of learning to solve problems of interest to you, before going back to the book, and so on.
  * This inspired me to try Kurt's approach, but instead of books, I was inspired to use this approach for any learning media.
* [Python Programming Tutorials](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-), starring Ulka Simone Mohanty. Accessed 2019-12-17.
  * This playlist teaches mostly Python 3 using great supporting visuals and a little science fiction humour.
  * A third of the way through the list, I noticed the Python knowledge could be used to help my discount calculations problem, so I started this project to calculate discounts.
* [How to Learn Python ...](https://www.youtube.com/watch?v=ohr6O78jGzs&t=115). Accessed 2019-12-17.
  * Daniel Moniz has a "3-day project paradigm", an organized plan for doing small coding projects without missing good practices such as refactoring and documentation. I loosely followed this plan to make and upload this small project to GitHub.
* Additional credits in the comments throughout the code, mostly:
  * Style reminders.
  * Solutions to Python issues I found during coding.

---

This little project is not affiliated with H&M.
