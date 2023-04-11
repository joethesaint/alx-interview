#!/usr/bin/python3
import sys
import unittest
import validator


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.sender_name = 'Marketing @ T-Shoes'
        self.sender_addr = 'marketing@tshoes.com'
        self.receiver_name = 'Jane Doe'
        self.receiver_addr = 'janedoe5511@gmail.com'
        self.html = '''
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
        self.replacements = {"<receiver_name>": self.receiver_name,
                             "<sender_name>": self.sender_name,
                             "<receiver_addr>": self.receiver_addr,
                             "<sender_addr>": self.sender_addr}

    def tearDown(self):
        pass

    def test_validate_example(self):
        self.assertTrue(validator.validate_email_payload(self.sender_name, self.sender_addr, self.receiver_name, self.receiver_addr, self.html, self.replacements))

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

    def test_validate_missing_html_body(self):
        sender_name = "Jane"
        sender_addr = "jane@example.com"
        receiver_name = "John"
        receiver_addr = "john@example.com"
        self.assertFalse(validator.validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, ""))

    def test_validate_invalid_email_addresses(self):
        sender_name = "Jane"
        sender_addr = "jane@com"
        receiver_name = "John"
        receiver_addr = "john@examplecom"
        html = "<p>Hi John,</p><p>This is a test email.</p>"
        self.assertFalse(validator.validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html))

    def test_validate_missing_sender_information(self):
        receiver_name = "John"
        receiver_addr = "john@example.com"
        html = "<p>Hi John,</p><p>This is a test email.</p>"
        self.assertFalse(validator.validate_email_payload("", "", receiver_name, receiver_addr, html))

    def test_validate_empty_strings(self):
        self.assertFalse(validator.validate_email_payload("", "", "", "", ""))


if __name__ == '__main__':
    unittest.main()
