"""
This script generates a random One-Time Password (OTP) and sends it via email to a specified recipient.
The OTP length must be between 4 and 8 digits, and the email address is validated before sending.
"""

import smtplib
import random
from validate_email_address import validate_email

def generate_otp(length=6):
    """
    Generate a random OTP of specified length (default is 6).
    Length must be between 4 and 8 digits.

    Args:
        length (int): The length of the OTP (default is 6).
    
    Returns:
        str: A string containing the randomly generated OTP.
    
    Raises:
        ValueError: If the length is less than 4 or greater than 8.
    """
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8.")
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email(email, otp):
    """
    Send OTP to the specified email address using SMTP.
    
    Args:
        email (str): The recipient's email address.
        otp (str): The OTP to be sent.

    Raises:
        ValueError: If the email is invalid.
        smtplib.SMTPException: If there is an error during email sending.
    """
    # Validate the email address
    if not validate_email(email):
        raise ValueError("Invalid email address.")

    # Properly formatted email message with Subject
    sender_email = "siddharthpandere@gmail.com"  # Your Gmail address
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"
    message = f"Subject: {subject}\n\n{body}"  # Include subject and body

    try:
        # Connect to Gmail's SMTP server securely using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, 'qlun mynq vzxz vheq')  # Replace with your app password
            smtp.sendmail(sender_email, email, message)
            print(f"OTP sent to {email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to generate OTP and send it via email.
    """
    email = input("Enter the recipient's email address: ")
    try:
        otp = generate_otp(length=6)  # Generate a 6-digit OTP
        send_email(email, otp)  # Send the OTP to the email
    except ValueError as ve:
        print(f"Error: {ve}")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
