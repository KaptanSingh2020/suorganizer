from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from .views import DisableAccount

password_urls = [
    url(r'^change/$',
        auth_views.password_change,
        {'template_name': 'user/password_change_form.html',
        'post_change_redirect': reverse_lazy('dj-auth:pw_change_done')},
        name='pw_change'),
    url(r'^change/done/$',
        auth_views.password_change_done,
        {'template_name': 'user/password_change_done.html'},
        name='pw_change_done'),
    url(r'^reset/$',
        auth_views.password_reset,
        {'template_name': 'user/password_reset_form.html',
        'email_template_name': 'user/password_reset_email.txt',
        'subject_template_name': 'user/password_reset_subject.txt',
        'post_reset_redirect': reverse_lazy('dj-auth:pw_reset_sent')},
        name='pw_reset_start'),
    url(r'^reset/sent/$',
        auth_views.password_reset_done,
        {'template_name': 'user/password_reset_sent.html'},
        name='pw_reset_sent'),
    url(r'^reset/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'user/password_reset_confirm.html',
        'post_reset_redirect': reverse_lazy('dj-auth:pw_reset_complete')},
        name='pw_reset_confirm'
        ),
    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {'template_name': 'user/password_reset_complete.html',
        'extra_context': {'form': AuthenticationForm}},
        name='pw_reset_complete'),
    url(r'^disable/$', DisableAccount.as_view(), name='disable'),

]

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dj-auth:login', permanent=False)),
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, 
        {'template_name': 'user/logged_out.html', 'extra_context': {'form': AuthenticationForm}},
        name='logout'),
    url(r'^password/', include(password_urls)),

]
