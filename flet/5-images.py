import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    # Adicionando a imagem
    img = ft.Image(
        src="https://media.istockphoto.com/id/1334436084/pt/foto/top-down-view-of-colorful-illuminated-gaming-accessories-laying-on-table.jpg?s=612x612&w=0&k=20&c=RADkpRxqLuKNRojQHMbRqcyiuqjt3BJ2Nj8DPgvrTAs=",
        border_radius=ft.border_radius.all(40),
        width=1000,
        height=1000,
        tooltip="Imagem Teste"
    )

    page.add(img)
    page.update()

ft.app(target=main)