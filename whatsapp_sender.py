# pip install pywhatkit
import pywhatkit as kit

# Specify the phone number (with country code) and the message
phone_number = "+919915044985"
message = '''Dear Deepanshu Yadav ,

I hope this email finds you well. I wanted to take a moment to express my sincere gratitude for your recent purchase of our product.

At [Your Company Name], we are committed to providing high-quality products and excellent customer service, and we are delighted that you chose to trust us with your purchase.

If you have any questions, feedback, or concerns regarding your purchase or our products, please don't hesitate to reach out to us. We are here to assist you in any way we can.

Once again, thank you for choosing [Your Company Name]. We truly appreciate your business and look forward to serving you again in the future.

Best regards,

Ankur Jaswal
Senior Developer
Electroniot
.'''

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)