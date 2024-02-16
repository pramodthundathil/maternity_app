from django.urls import path
from .import views

urlpatterns = [
    path("StaffIndex",views.StaffIndex,name="StaffIndex"),
    path("BookingView/<str:pk>",views.BookingView,name="BookingView"),
    path("AddStaff",views.AddStaff,name="AddStaff"),
    path("AddPatientProfile/<str:pk>",views.AddPatientProfile,name="AddPatientProfile"),
    path("UpdateProfile/<str:pk>,<str:sk>",views.UpdateProfile,name="UpdateProfile"),
    path("PatientList",views.PatientList,name="PatientList"),
    path("DeleteProfile,<str:pk>",views.DeleteProfile,name="DeleteProfile"),
    path("DoctorView",views.DoctorView,name="DoctorView"),
    path("BillView",views.BillView,name="BillView"),
    path("AddBill/<str:pk>",views.AddBill,name="AddBill"),
    path("AddProduct",views.AddProduct,name="AddProduct"),
    path("DeleteProduct/<str:pk>",views.DeleteProduct,name="DeleteProduct"),
    path("CartPage",views.CartPage,name="CartPage"),
    path("IncreaseQuantity/<int:pk>",views.IncreaseQuantity,name="IncreaseQuantity"),
    path("DecreaseQuantity/<int:pk>",views.DecreaseQuantity,name="DecreaseQuantity"),
    path("DeleteCartItem/<int:pk>",views.DeleteCartItem,name="DeleteCartItem"),
     path("ProceedCheckout",views.ProceedCheckout,name="ProceedCheckout"),
    path("paymenthandler/",views.paymenthandler,name="paymenthandler"),
    path("Success1",views.Success1,name="Success1"),
    path("AddToCart/<int:pk>",views.AddToCart,name="AddToCart"),
    path("MyOrderes",views.MyOrderes,name="MyOrderes"),
    path("deleteordercus/<int:pk>",views.deleteordercus,name="deleteordercus"),
    path("CustomerOrderes",views.CustomerOrderes,name="CustomerOrderes"),
    path("deleteordermanu/<int:pk>",views.deleteordermanu,name="deleteordermanu"),



    
]
