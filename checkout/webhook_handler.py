from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle webhooks from Stripe
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle unexpected, unknown or generic webhook events
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent_succeeded webhook
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)