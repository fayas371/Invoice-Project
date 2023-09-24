from django.urls import reverse_lazy,reverse
from .models import Invoice, InvoiceDetail
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

class InvoiceView(ListView):
    model=Invoice
    template_name='view_invoice.html'
    context_object_name='invoice_list'

class CreateInvoice(CreateView):
    model=Invoice
    template_name='create_invoice.html'
    fields='__all__'
    success_url=reverse_lazy('Home_page')

class EditInvoice(UpdateView):
    model=Invoice
    template_name='update_invoice.html'
    fields='__all__'
    success_url=reverse_lazy('Home_page')


class InvoiceDetailView(DetailView):
    model = InvoiceDetail
    template_name = 'invoice_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice_detail = self.get_object()  # Get the InvoiceDetail object
        invoice = invoice_detail.invoice  # Get the related Invoice object

        context['invoice_detail'] = invoice_detail
        context['invoice'] = invoice

        return context




class UpdateInvoiceDetails(UpdateView):
    model = InvoiceDetail
    template_name='update_invoice_detail.html'
    fields='__all__'
    success_url=reverse_lazy('Home_page')

class DeleteInvoice(DeleteView):
    model=Invoice
    template_name='delete_invoice.html'
    success_url=reverse_lazy('Home_page')
