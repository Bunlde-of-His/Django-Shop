from django.urls import path
from shop.views import (
    Registration,
    Login,
    Logout,
    ListOfProducts,
    AdminProductList,
    EditProduct,
    AddProduct,
    ReturnProduct,
    ReturnAgreement,
    ReturnRejection,
    ProductPurchase,
    PurchaseList,
    CreateReturn,
    ProductDelete
)

app_name = 'shop'
urlpatterns = [
    path('', ListOfProducts.as_view(), name="index"),
    path('register/', Registration.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('product-list/', AdminProductList.as_view(), name="product_list"),
    path('change-product/<int:pk>/', EditProduct.as_view(), name="change_product"),
    path('add-product/', AddProduct.as_view(), name="add_product"),
    path('product-confirm-delete/<int:pk>/', ProductDelete.as_view(), name='product_confirm_delete'),
    path('refunds/', ReturnProduct.as_view(), name="refunds"),
    path('refund_agree/<int:pk>/', ReturnAgreement.as_view(), name='refund_agree'),
    path('refund_reject/<int:pk>/', ReturnRejection.as_view(), name='refund_reject'),
    path('purchase/<int:pk>/', ProductPurchase.as_view(), name='purchase_product'),
    path('purchase-list/', PurchaseList.as_view(), name='purchase_list'),
    path('create-refund/<int:purchase_id>/', CreateReturn.as_view(), name='create_refund'),
]