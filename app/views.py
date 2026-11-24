from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from . import content
from .models import ContactSubmission
from .news_feed import get_fraud_news_alerts


# ============================================
# HOME
# ============================================

def home(request):
    featured_insights = content.INSIGHTS[:4]
    return render(request, 'pages/home.html', {
        'title': 'Vaultreck — Trace. Recover. Restore.',
        'featured_insights': featured_insights,
        'how_it_works': content.HOW_IT_WORKS,
        'stats': content.STATS,
        'services': content.SERVICES,
        'industries': content.INDUSTRIES,
        'latest_insights': content.INSIGHTS[:3],
        'news_alerts': get_fraud_news_alerts(limit=3),
    })


# ============================================
# SERVICES
# ============================================

def services(request):
    return render(request, 'pages/services.html', {
        'title': 'Services · Vaultreck',
        'services': content.SERVICES,
        'breadcrumbs': [{'label': 'Services'}],
    })


def service_detail(request, slug):
    service = content.SERVICES_BY_SLUG.get(slug)
    if not service:
        raise Http404('Service not found')
    related = [s for s in content.SERVICES if s['slug'] != slug][:3]
    return render(request, 'pages/service_detail.html', {
        'title': f"{service['name']} · Vaultreck",
        'service': service,
        'related_services': related,
        'related_insights': content.INSIGHTS[:3],
        'breadcrumbs': [
            {'label': 'Services', 'url': reverse('services')},
            {'label': service['name']},
        ],
    })


# ============================================
# INDUSTRIES
# ============================================

def industries(request):
    return render(request, 'pages/industries.html', {
        'title': 'Industries · Vaultreck',
        'industries': content.INDUSTRIES,
        'breadcrumbs': [{'label': 'Industries'}],
    })


def industry_detail(request, slug):
    industry = content.INDUSTRIES_BY_SLUG.get(slug)
    if not industry:
        raise Http404('Industry not found')
    return render(request, 'pages/industry_detail.html', {
        'title': f"{industry['name']} · Vaultreck",
        'industry': industry,
        'related_services': content.SERVICES[:4],
        'breadcrumbs': [
            {'label': 'Industries', 'url': reverse('industries')},
            {'label': industry['name']},
        ],
    })


# ============================================
# INSIGHTS
# ============================================

def insights(request):
    category = request.GET.get('category', '')
    return render(request, 'pages/insights.html', {
        'title': 'Insights · Vaultreck',
        'insights': content.INSIGHTS,
        'categories': content.INSIGHT_CATEGORIES,
        'selected_category': category,
        'news_alerts': get_fraud_news_alerts(),
        'breadcrumbs': [{'label': 'Insights'}],
    })


def insight_detail(request, slug):
    insight = content.INSIGHTS_BY_SLUG.get(slug)
    if not insight:
        raise Http404('Insight not found')
    related = [i for i in content.INSIGHTS if i['slug'] != slug and i['category'] == insight['category']][:3]
    if len(related) < 3:
        related += [i for i in content.INSIGHTS if i['slug'] != slug and i not in related][:3 - len(related)]
    return render(request, 'pages/insight_detail.html', {
        'title': f"{insight['title']} · Vaultreck",
        'insight': insight,
        'related_insights': related,
        'breadcrumbs': [
            {'label': 'Insights', 'url': reverse('insights')},
            {'label': insight['title']},
        ],
    })


# ============================================
# ABOUT / CAREERS / CONTACT / FAQ
# ============================================

def about(request):
    return render(request, 'pages/about.html', {
        'title': 'About Us · Vaultreck',
        'team': content.LEADERSHIP_TEAM,
        'breadcrumbs': [{'label': 'About'}],
    })


def careers(request):
    return render(request, 'pages/careers.html', {
        'title': 'Careers · Vaultreck',
        'roles': content.OPEN_ROLES,
        'breadcrumbs': [{'label': 'Careers'}],
    })


def contact(request):
    submitted = False
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        consent = bool(request.POST.get('consent'))
        if name and email and subject and message and consent:
            ContactSubmission.objects.create(
                name=name, email=email, subject=subject, message=message, consent=consent,
            )
            submitted = True
    return render(request, 'pages/contact.html', {
        'title': 'Contact Us · Vaultreck',
        'breadcrumbs': [{'label': 'Contact'}],
        'submitted': submitted,
    })


def faq(request):
    return render(request, 'pages/faq.html', {
        'title': 'Frequently Asked Questions · Vaultreck',
        'faqs': content.SITE_FAQS,
        'breadcrumbs': [{'label': 'FAQ'}],
    })


def report_fraud(request):
    return render(request, 'pages/report_fraud.html', {
        'title': 'Report a Fraud · Free Case Review · Vaultreck',
        'breadcrumbs': [{'label': 'Report a Fraud'}],
    })


# ============================================
# LEGAL
# ============================================

def legal_page(request, slug):
    page = content.LEGAL_PAGES_BY_SLUG.get(slug)
    if not page:
        raise Http404('Page not found')
    return render(request, 'pages/legal/legal_detail.html', {
        'title': f"{page['title']} · Vaultreck",
        'page': page,
        'breadcrumbs': [{'label': page['title']}],
    })


# ============================================
# SEO: robots.txt / sitemap.xml
# ============================================

@require_GET
def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        f"Sitemap: {request.scheme}://{request.get_host()}{reverse('sitemap_xml')}",
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


@require_GET
def sitemap_xml(request):
    base = f"{request.scheme}://{request.get_host()}"
    static_paths = [
        reverse('home'), reverse('services'), reverse('industries'),
        reverse('insights'), reverse('about'), reverse('careers'),
        reverse('contact'), reverse('faq'), reverse('report_fraud'),
    ]
    paths = list(static_paths)
    paths += [reverse('service_detail', args=[s['slug']]) for s in content.SERVICES]
    paths += [reverse('industry_detail', args=[i['slug']]) for i in content.INDUSTRIES]
    paths += [reverse('insight_detail', args=[i['slug']]) for i in content.INSIGHTS]
    paths += [reverse('legal_page', args=[p['slug']]) for p in content.LEGAL_PAGES]

    urls = ''.join(f'<url><loc>{base}{p}</loc></url>' for p in paths)
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
    return HttpResponse(xml, content_type='application/xml')


# ============================================
# ERROR HANDLERS
# ============================================

def handler404(request, exception=None):
    return render(request, '404.html', {'title': 'Page Not Found · Vaultreck'}, status=404)
