"""misPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


from django.contrib.auth import views as auth_views
from misPerris import views as vistas
from django.conf.urls import url 
from django.urls import reverse_lazy, include, path
from django.contrib import admin

urlpatterns = [
    path('mascotas/', include('mascotas.urls')),
    path('quienessomos/', vistas.quienes,name="quienes_somos"),
    path('contacto/', vistas.contacto,name="contacto"),
    path('', vistas.inicio,name="inicio"),
    path('admin/', admin.site.urls),
 
    path(
        'ingresar/',
        vistas.ingresando
        ,name='ingreso'
    ),
      url(
       'deslogear',
        auth_views.LogoutView.as_view(),
        name='deslogear',
    ),
    url(
    'password/recovery/',
    auth_views.PasswordResetView.as_view(
        template_name='auth/resetear.html',
        html_email_template_name='auth/resetmail.html',
    ),
    name='password_reset',
),
    url(
        'password/recovery/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
     url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('home'),
            post_reset_login=True,
            template_name='auth/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),
    
    path('new/',vistas.registro_usuario, name="registro")
]
