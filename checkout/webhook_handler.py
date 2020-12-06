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
            content=f'Webhook received: {event["type"]}',
            status=200)