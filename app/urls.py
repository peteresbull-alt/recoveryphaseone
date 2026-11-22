from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),

    path('industries/', views.industries, name='industries'),
    path('industries/<slug:slug>/', views.industry_detail, name='industry_detail'),

    path('insights/', views.insights, name='insights'),
    path('insights/<slug:slug>/', views.insight_detail, name='insight_detail'),

    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('report-a-fraud/', views.report_fraud, name='report_fraud'),

    path('legal/<slug:slug>/', views.legal_page, name='legal_page'),

    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
]
