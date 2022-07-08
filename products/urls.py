from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('review/<int:product_id>/', views.SubmitReview.as_view(), name='add_review'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product_admin, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
     path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),

    #path('<product_id>/review/edit/', views.UpdateReview.as_view(), name='edit_review'),
    #path('<product_id>/review/Delete', views.DeleteReview.as_view(), name='delete_review'),
]