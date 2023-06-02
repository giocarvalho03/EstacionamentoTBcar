"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls') ),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('', home, name='url_principal'),
    path('cadastroCliente/', cadastroCliente, name='url_cadastro_cliente'),
    path('listagem_clientes/' , listagem_clientes, name='url_listagem_clientes'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('listagem_rotativos/', listagem_rotativos, name='url_listagem_rotativos'),
    path('altera_rotativo/<int:id>/', altera_rotativo, name='url_altera_rotativo'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('cadastro_tabela/', cadastro_tabela, name='url_cadastro_tabela'),
    path('listagem_tabelas/', listagem_tabelas, name='url_listagem_tabelas'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)