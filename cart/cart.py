
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


    def add(self, product):
        """
        adding and updating cart session
        """
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
