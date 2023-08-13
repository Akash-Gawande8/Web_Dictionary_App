import justpy as jp

import layout


class Home():
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="""
        HOME
        """, classes='text-lg')
        jp.Div(a=div, text="Dictionary.com strives to enable and inspire connection, "
                           "communication, learning, creativity, "
                           "and expression in a world powered by words.", classes="text-lg m-2")

        return wp
