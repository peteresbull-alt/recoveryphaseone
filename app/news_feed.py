"""
Live "Scam & Fraud Alerts" feed for the Insights hub, sourced from NewsAPI.org.

Kept deliberately separate from app.content's hand-written INSIGHTS: these are
real, external, unvetted news items (not our own case studies), so they're
rendered in their own section with attribution and an outbound link rather
than mixed into the curated grid.

Requires NEWS_API_KEY to be set (see settings.py). If it's missing, or the
request fails for any reason, this returns an empty list rather than breaking
the page — the live section simply doesn't render.
"""

import logging

import requests
from django.conf import settings
from django.core.cache import cache
from django.utils.dateparse import parse_datetime

logger = logging.getLogger(__name__)

NEWS_API_URL = 'https://newsapi.org/v2/everything'
CACHE_KEY = 'fraud_news_alerts'
CACHE_TTL_SECONDS = 60 * 60  # 1 hour — NewsAPI's free tier allows 100 requests/day total
FETCH_SIZE = 20  # over-fetch, then filter down to `limit` — see _looks_relevant()

# A bare phrase like "ponzi scheme" gets used constantly as political rhetoric
# (e.g. commentary calling Social Security "a ponzi scheme"), which has nothing
# to do with actual fraud reporting. Requiring a crime/enforcement-context word
# alongside the fraud phrase filters most of that out.
SEARCH_QUERY = (
    '("investment scam" OR "crypto scam" OR "romance scam" OR "wire fraud" '
    'OR "ponzi scheme" OR "investment fraud" OR "cryptocurrency fraud") '
    'AND (victims OR investors OR charged OR arrested OR indicted OR investigation '
    'OR fraud OR "SEC" OR "FBI" OR scheme OR scammed OR swindled)'
)

# Opinion/commentary sites that showed up matching fraud-adjacent phrases used as
# political metaphor rather than fraud reporting. Starting list on both sides of
# the aisle so this isn't (and doesn't look like) a one-sided filter.
EXCLUDED_DOMAINS = [
    'commondreams.org', 'crooksandliars.com', 'motherjones.com',
    'breitbart.com', 'theblaze.com', 'dailykos.com',
]

# Titles containing these are almost always political commentary that picked up
# a fraud-adjacent phrase, not actual fraud/scam reporting.
OFF_TOPIC_TITLE_MARKERS = [
    'social security', 'senator', 'congress', 'election', 'president',
    'democrat', 'republican', 'gop', 'white house', 'governor',
]


def _looks_relevant(title):
    lowered = title.lower()
    return not any(marker in lowered for marker in OFF_TOPIC_TITLE_MARKERS)


def get_fraud_news_alerts(limit=6):
    """Returns a list of recent fraud-related news items, or [] on any failure."""
    cached = cache.get(CACHE_KEY)
    if cached is not None:
        return cached[:limit]

    if not settings.NEWS_API_KEY:
        return []

    try:
        response = requests.get(
            NEWS_API_URL,
            params={
                'q': SEARCH_QUERY,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': FETCH_SIZE,
                'excludeDomains': ','.join(EXCLUDED_DOMAINS),
                'apiKey': settings.NEWS_API_KEY,
            },
            timeout=5,
        )
        response.raise_for_status()
        payload = response.json()
    except (requests.RequestException, ValueError) as exc:
        logger.warning('NewsAPI fraud-alerts fetch failed: %s', exc)
        return []

    if payload.get('status') != 'ok':
        logger.warning('NewsAPI returned an error payload: %s', payload.get('message'))
        return []

    items = []
    for article in payload.get('articles', []):
        title = article.get('title')
        if not title or not article.get('url') or not _looks_relevant(title):
            continue
        items.append({
            'title': title,
            'url': article['url'],
            'source': (article.get('source') or {}).get('name') or 'Unknown source',
            'published_at': parse_datetime(article.get('publishedAt', '') or ''),
            'description': article.get('description') or '',
        })

    cache.set(CACHE_KEY, items, CACHE_TTL_SECONDS)
    return items[:limit]
