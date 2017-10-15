from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from .models import Partner

# Create your views here.

def register(request):
	
	if request.method == "GET":
		return render(request, 'partners/register.html')
	else:
		form = request.POST
		validate_form_data = validate_form(form)
		if len(validate_form_data) != 0 :
			return render (request,
                        'partners/register.html',
                        {'falhas': validate_form_data})
		else:
			name = form.get('name')
        	description = form.get('description')
        	address = form.get('address')
        	fone = form.get('fone')
        	partner = Partner()
        	partner.save_patners(name, description, address, fone)
        	return HttpResponseRedirect(reverse('partners:list'))		

def validate_form(form):
    name = form.get('name')
    description = form.get('description')
    address = form.get('address')
    fone = form.get('fone')

    resultCheck = []

    name = check_name(name, 3)
    if len(name) != 0:
		resultCheck.append(name)

    description = check_description(description, 10)
    if len(description) != 0:
    	resultCheck.append(description)

    address = check_address(address, 10)
    if len(address) != 0:	
    	resultCheck.append(address, 10)

    fone = check_fone(fone, 8)
    if len(fone) != 0:
    	resultCheck.append(fone)

    return resultCheck

def check_name(name, tamanho):
    if len(name) >= tamanho:
        return ''
    else:
        return 'Nome deve conter apenas letras e deve ter no minimo de ' + str(tamanho) + ' caracteres'

def check_description(description, tamanho):
    if len(description) >= tamanho:
        return ''
    else:
        return 'Descricao deve ter no minimo de ' + str(tamanho) + ' caracteres'

def check_address(address, tamanho):
    if len(address) >= tamanho:
        return ''
    else:
        return 'Endereco deve ter no minimo de ' + str(tamanho) + ' caracteres'

def check_fone(fone, tamanho):
    if len(fone) >= tamanho and not fone.isalpha():
        return ''
    else:
        return 'fone deve ter no minimo de ' + str(tamanho) + ' caracteres'                      



def list_partners(request):
	
	return render(request, 'partners/partnersList.html')