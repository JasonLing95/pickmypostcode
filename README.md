# Purpose
Automate looking up daily postcode on PickMyPostcode (https://pickmypostcode.com/#) and send it to a Telegram channel

# API Integration
1. PickMyPostcode - to get the daily postcode
2. Telegram - to send message to Telegram

# Environments Required
1. `API_TOKEN` (Telegram)
2. `CHAT_ID` (Telegram Channel ID)

# Deployment
Deployed on AWS Lambda and triggered by AWS EventBridge daily
