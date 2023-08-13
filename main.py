import justpy as jp

# import page
# import inspect

"""
imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)
"""

from Web_Dictionary_App.about import About
from Web_Dictionary_App.dictionary import Dictionary
from Web_Dictionary_App.home import Home

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
