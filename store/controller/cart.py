from django.shortcuts import render,redirect
from django.contrib import messages


def addtocart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.get(id = prod_id)
        if(product_check):
            if(Cart.objects.filter(user = request.user , product_id=prod_id)):
                return JsonResponse({'status',"product already in cart"})
            else:
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user , product_id = prod_id , product_qty = prod_qty)
                    return JsonResponse({"status","product added to cart"})

                else:
                    return JsonResponse({"status","only"+str(product_check.quantity+"quantot avaiable")})
                  
                



        else:
            return JsonResponse({'status',"no such product avaiable"})




    else:
        return JsonResponse({'status',"no such product avaiable"})