# Invoice-Project
This are url_patterns check all the use_case for reference of the project 

    path('invoice/', InvoiceView.as_view(), name='Home_page'),
    path('invoice_create/',CreateInvoice.as_view(),name='create_invoice'),
    path('invoice_update/<int:pk>',EditInvoice.as_view(),name='update_invoice'),
    path('invoice_detail_update/<int:pk>',UpdateInvoiceDetails.as_view(),name='update_invoice_detail'),
    path('invoice_detail/<int:pk>',InvoiceDetailView.as_view(),name='invoice_details'),
    path('delete_invoice/<int:pk>',DeleteInvoice.as_view(),name='delete_invoice'),

