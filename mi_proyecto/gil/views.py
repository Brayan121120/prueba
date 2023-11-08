from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from gil.forms import RegistroForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect

def prede(request):
    return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guarda el formulario
            form.save()

            # Envía el correo electrónico
            subject = 'Gracias por registrarte'
            message = '¡Gracias por registrarte en nuestro sitio!'
            from_email = 'brayangil121120@gmail.com'
            recipient_list = [form.cleaned_data['email']]
            
            # Puedes usar una plantilla HTML para el cuerpo del correo
            html_message = render_to_string('email_template.html', {'message': message})
            plain_message = strip_tags(html_message)  # Convierte el HTML en texto plano

            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            

            return redirect("login")  # Redirige a una página de éxito
        

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def tablas(request):
    return render(request, 'tables.html')
