from . import content


def nav_context(request):
    """Makes services/industries available to the header mega-menu and
    footer on every page without every view having to pass them."""
    return {
        'nav_services': content.SERVICES,
        'nav_industries': content.INDUSTRIES,
        'insight_categories': content.INSIGHT_CATEGORIES,
        'offices': content.OFFICES,
        'support_email': content.SUPPORT_EMAIL,
    }
