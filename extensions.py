import re
import subprocess
import unicodedata
from datetime import date
from packaging import version

from jinja2 import Environment
from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default


def slugify(value, separator="-"):
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


def get_lowest_version(versions: str) -> str:
    versions_list = [version.parse(v) for v in versions.split(" ")]
    return str(min(versions_list))


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify


class CurrentYearExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year


class LowestVersionExtension(Extension):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        environment.filters["lowest_version"] = get_lowest_version
