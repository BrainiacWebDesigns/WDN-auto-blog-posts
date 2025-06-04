import update_topics
from unittest.mock import patch, Mock


def test_fetch_trending_topics():
    html = "<html><body><h2>Topic One</h2><h2>Topic Two</h2></body></html>"
    mock_response = Mock(text=html)
    with patch('update_topics.requests.get', return_value=mock_response):
        with patch.object(update_topics, 'sources', ['http://a', 'http://b']):
            topics = update_topics.fetch_trending_topics()
    assert set(topics) == {'Topic One', 'Topic Two'}
