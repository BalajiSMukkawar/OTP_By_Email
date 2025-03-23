import smtplib
import random

# Email sender details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "Enter_mail"  # Replace with your Gmail
SENDER_PASSWORD = "API_16 Char App Pass"  # Replace with your 16-char App Password

# Function to generate a 6-digit numeric OTP
def generate_numeric_otp():
    return random.randint(100000, 999999)  # Generates a 6-digit OTP

# Function to send OTP via email
def send_email_otp(receiver_email, otp):
    subject = "Your OTP Code"
    message = f"Subject: {subject}\n\nYour OTP is {otp}. Use this to verify your login."

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login to Gmail
        server.sendmail(SENDER_EMAIL, receiver_email, message)  # Send email
        server.quit()
        print(f"✅ OTP sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Function to verify OTP entered by the user
def verify_otp(user_input, correct_otp):
    if user_input == correct_otp:
        print("✅ OTP Verified Successfully!")
    else:
        print("❌ Incorrect OTP. Please try again!")

# Main Execution
receiver_email = input("Enter recipient email: ")  # Get recipient email
otp = generate_numeric_otp()  # Generate numeric OTP
send_email_otp(receiver_email, otp)  # Send OTP

# Ask user to enter OTP
user_input = input("Enter the OTP received: ")

# Verify OTP
verify_otp(user_input, str(otp))  # Convert to string for comparison
