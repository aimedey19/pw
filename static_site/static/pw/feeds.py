from coltrane.feeds import ContentFeed as BaseContentFeed
from coltrane.retriever import ContentItem
from django.utils import feedgenerator


class CustomFeedGenerator(feedgenerator.Atom1Feed):
    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        html = item["content"]
        html = html.replace("{% verbatim %}", "")
        html = html.replace("{% endverbatim %}", "")
        handler.addQuickElement("content", html, attrs={"type": "html"})


class ContentFeed(BaseContentFeed):
    feed_type = CustomFeedGenerator

    def item_extra_kwargs(self, item: ContentItem):
        return {"content": item.html}
