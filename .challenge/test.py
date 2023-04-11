#!/usr/bin/python3
import sys
import unittest
import validator


class ValidatorTest(unittest.TestCase):
    def test_validate_example(self):
        sender_name = 'Marketing @ T-Shoes'
        sender_addr = 'marketing@tshoes.com'
        receiver_name = 'Jane Doe'
        receiver_addr = 'janedoe5511@gmail.com'
        html = '''
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>TShoes Discounts comes AGAIN!</title>
            </head>
            <body>
            <p>Hi {first_name},</p>
            <p>Marketing message...</p>
            </body>
            </html>
        '''
        replacements = {"<receiver_name>": receiver_name,
                        "<sender_name>": sender_name,
                        "<receiver_addr>": receiver_addr,
                        "<sender_addr>": sender_addr}
        self.assertTrue(validator.validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements))

    def test_validate_another_example(self):
        sender_name = 'Jenny Wong'
        sender_addr = 'jennyw@tshoes.com'
        receiver_name = 'Harry White'
        receiver_addr = 'harrywhite@outlook.com'
        html = '''
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>Personal email!</title>
            </head>
            <body>
            <p>How are you Harry?...</p>
            </body>
            </html>
        '''
        replacements = {"<receiver_name>": receiver_name,
                        "<sender_name>": sender_name,
                        "<receiver_addr>": receiver_addr,
                        "<sender_addr>": sender_addr}
        self.assertTrue(validator.validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements))


if __name__ == '__main__':
    unittest.main()
