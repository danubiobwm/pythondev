import flet as ft

def main(page:ft.Page):
    t1 = ft.Text(
        value = "Utilizando Elemento de Texto Utilizando Elemento de TextoUtilizando Elemento de Texto",
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor= "#000000",
        style= ft.TextStyle(
            color ="#FFFFFF",
            font_family="Arial",
            italic=True,
            weight=ft.FontWeight.W_300
        ),
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        text_align=ft.TextAlign.CENTER
    )
    text_one_style = ft.TextStyle(color="#ACACAC",
                                  decoration=ft.TextDecoration.UNDERLINE)

    text_two_style = ft.TextStyle(bgcolor="#BBC584",
                                  color="#000000",
                                  decoration=ft.TextDecoration.OVERLINE,
                                  decoration_color="#2427F7",
                                  decoration_style=ft.TextDecorationStyle.DOUBLE)
    t2 = ft.Text(
        spans= [
            ft.TextSpan(text="Texto de exemplo",
                        url="https://www.google.com",
                        style=text_one_style),
            ft.TextSpan(text="Continuação do texto", style=text_two_style)
        ]
    )
    page.add(t1, t2)
    page.update()

ft.app(target=main)