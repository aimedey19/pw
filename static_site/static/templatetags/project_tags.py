from coltrane import get_config
from coltrane.retriever import get_data

from django import template

from dateparser import parse


register = template.Library()


@register.simple_tag(name="get_projects")
def get_projects() -> list[dict[str, str]]:
    site = get_config(base_dir=Path(".")).get_site(request)
    projects = get_data(site=site)["projects"]
    for project in projects:
        project["last_updated"] = parse(project["last_updated"])

    projects.sort(key=lambda p: p.get("last_updated"), reverse=True)
    projects.sort(key=lambda p: p.get("featured"), reverse=True)
    projects.sort(key=lambda p: p.get("priority", 0), reverse=True)

    return projects
