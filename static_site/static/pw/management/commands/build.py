from coltrane.renderer import StaticRequest

from pw.feeds import ContentFeed

from coltrane.management.commands.build import Command as BuildCommand


class Command(BuildCommand):
    def _generate_rss(self) -> None:
        assert self.output_directory
        content_feed = ContentFeed()
        feed = content_feed.get_feed(None, request=StaticRequest(path="/"))
        rss_xml = feed.writeString("utf-8")

        (self.output_directory / "rss.xml").write_text(rss_xml)
