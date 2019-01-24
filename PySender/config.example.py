# API Settings
base_url = "https://www.thetexting.com/rest/sms/json/Message/Send"
api_key = "XXXXXXX"
api_secret = "XXXXXXX"
fromSender = "test"
http_method = "POST"
attemptsPerEachMessage = 3
responseStatusField = "Status"
apiPayload = f"api_secret={api_secret}&api_key={api_key}&from={fromSender}"
numberField = "to"
messageField = "text"

#UI and language
bulkSendResultMessage = "sms sent on a total of"
sendErrorMessage = "ERROR: unable to send message to"
xlsxFileLabel = "XLSX file path: "
extractNumberLabel = "Extract numbers"
messageLabel = "Message: "
sendMessagesLabel = "Send Messages"
xlsxExtractResultMessage = "numbers found in file"
