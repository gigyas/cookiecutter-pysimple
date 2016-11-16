import pbr.version


__version__ = pbr.version.VersionInfo(
    '{{cookiecutter.project_slug}}').version_string()