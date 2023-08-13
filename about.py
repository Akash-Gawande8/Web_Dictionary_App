import justpy as jp

import layout


class About():
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="""
        ABOUT
        """, classes='text-lg')

        jp.Div(a=div, text="""
        A dictionary is a listing of lexemes from the lexicon of one or more specific languages, 
        often arranged alphabetically (or by consonantal root for Semitic languages or radical and stroke for logographic languages),
        which may include information on definitions, usage, etymologies, pronunciations, translation, 
        etc.It is a lexicographical reference that shows inter-relationships among the data.
        """, classes="text-lg m-2")

        return wp
