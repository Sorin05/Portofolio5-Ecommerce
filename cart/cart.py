
class Cart():
    """
    A shopping cart class, with some defalt behaviors that
    can  be inherited or overrided.
    """

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart
