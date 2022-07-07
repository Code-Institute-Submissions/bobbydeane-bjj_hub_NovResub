from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('review/<product_id>', views.SubmitReview.as_view(), name='add_review'),
    path('product/<product_id>', views.product_detail, name='product_detail'),
    #path('<product_id>/review/edit/', views.UpdateReview.as_view(), name='update_review'),
    #path('<product_id>/review/Delete', views.DeleteReview.as_view(), name='delete_review'),
]