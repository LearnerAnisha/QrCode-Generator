from django.shortcuts import render
from .forms import QRCodeForm
import qrcode

def generate_qr_code(request):
  if request.method == 'POST':
    form = QRCodeForm(request.POST)
    if form.is_valid():
      restaurant_name = form.cleaned_data['restaurant_name']
      url = form.cleaned_data['url']
      # Generate the QR code
      qr = qrcode.make(url)
      file_name = restaurant_name.replace('','_') + '_menu_qr.png'
      qr.save(file_name)
  else:
    form = QRCodeForm()
    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)