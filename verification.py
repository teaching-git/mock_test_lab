class VerificationService:
    def __init__(self, sms_gateway):
        self.sms_gateway = sms_gateway

    def send_code(self, phone):
        return self.sms_gateway.send(phone, "1234")
