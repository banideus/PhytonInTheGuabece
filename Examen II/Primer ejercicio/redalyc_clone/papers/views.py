from django.shortcuts import render,redirect #puedes importar render_to_response
from papers.forms import subirTrabajo
from papers.models import trabajos

# Create your views here.

def index(request):
	return render(request,"trabajos/index.html")
# querysets para la consulta de los trabajos
def consultacc(request):
	obj=trabajos.objects.filter(categoria="CC")
	for abc in obj:
		obj_titulos=abc.titulo
		obj_autores=abc.autor
		obj_categorias=abc.categoria
		obj_docfiles=abc.docfile
	context= {
		"obj":obj,
		"obj_titulos":obj_titulos,
		"obj_autores":obj_autores,
		"obj_categorias":obj_categorias,
		"obj_docfiles":obj_docfiles
	}
	return render(request,"trabajos/consultacc.html", context)

def consultact(request):
	obj=trabajos.objects.filter(categoria="CT")
	for abc in obj:
		obj_titulos=abc.titulo
		obj_autores=abc.autor
		obj_categorias=abc.categoria
		obj_docfiles=abc.docfile
	context= {
		"obj":obj,
		"obj_titulos":obj_titulos,
		"obj_autores":obj_autores,
		"obj_categorias":obj_categorias,
		"obj_docfiles":obj_docfiles
	}
	return render(request,"trabajos/consultact.html", context)

def consultacn(request):
	obj=trabajos.objects.filter(categoria="CN")
	for abc in obj:
		obj_titulos=abc.titulo
		obj_autores=abc.autor
		obj_categorias=abc.categoria
		obj_docfiles=abc.docfile
	context= {
		"obj":obj,
		"obj_titulos":obj_titulos,
		"obj_autores":obj_autores,
		"obj_categorias":obj_categorias,
		"obj_docfiles":obj_docfiles
	}
	return render(request,"trabajos/consultacn.html", context)

def consultacs(request):
	obj=trabajos.objects.filter(categoria="CS")
	for abc in obj:
		obj_titulos=abc.titulo
		obj_autores=abc.autor
		obj_categorias=abc.categoria
		obj_docfiles=abc.docfile
	context= {
		"obj":obj,
		"obj_titulos":obj_titulos,
		"obj_autores":obj_autores,
		"obj_categorias":obj_categorias,
		"obj_docfiles":obj_docfiles
	}
	return render(request,"trabajos/consultacs.html", context)

def consultacm(request):
	obj=trabajos.objects.filter(categoria="CM")
	for abc in obj:
		obj_titulos=abc.titulo
		obj_autores=abc.autor
		obj_categorias=abc.categoria
		obj_docfiles=abc.docfile
	context= {
		"obj":obj,
		"obj_titulos":obj_titulos,
		"obj_autores":obj_autores,
		"obj_categorias":obj_categorias,
		"obj_docfiles":obj_docfiles
	}
	return render(request,"trabajos/consultacm.html", context)

#funcion para sbir archivos, utilizando el metodo POST 
def upload_file(request):
    if request.method == 'POST':
        form = subirTrabajo(request.POST, request.FILES)
        if form.is_valid():
        	newdoc = trabajos(titulo= request.POST['titulo'],
				autor= request.POST['autor'],
				categoria= request.POST['categoria'],
        		docfile = request.FILES['docfile'])
        	newdoc.save(form)
        	return redirect("index_view")
    else:
        form = subirTrabajo()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form})