from django.http import HttpResponse


class StripeWH_Handler:
    '''Handle stripe webhooks'''
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        '''Handle unexpected or unknown webhooks'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
            
    def handle_payment_intent_succeeded(self, event):
        '''Handle successful payments from stripe'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        '''Handle unsuccessful payments from stripe'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)