var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe('pk_test_51HssThEa2dUbR51THmTD2geGbetSyi0Bt36vlNdLz7E9klfKmVBARcIToLR9aI0v43agTNCPMITeQOWrhRYcA4Dd00NKY0iumN');
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Montserrat", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '1rem',
        '::placeholder': {
            color: '#495057'
        },
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');