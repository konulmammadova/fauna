from fauna_app.models import Basket


def create_bucket_middleware(get_response):
    """
        Create open basket for anonymous users or users not yet logged in
    """

    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        def create_basket(user=None):
            print('Create new basket')
            if request.user.is_authenticated():
                basket_obj = Basket.objects.create(user=request.user)
            else:
                basket_obj = Basket.objects.create(user=user)
            return basket_obj

        basket_id = request.session.get('basket_id', None)
        qs = Basket.objects.filter(id=basket_id)
        if qs.count() == 1:
            basket_obj = qs.first()
            if request.user.is_authenticated():
                basket_obj = Basket.objects.get(id=basket_id)
                basket_obj.user= request.user
                basket_obj.save()
            print('Basket id exists')
        else:
            basket_obj = create_basket()
            request.session['basket_id'] = basket_obj.id

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
