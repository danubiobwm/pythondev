import flet as ft

def create_icon_container(icon_name, on_favorite, is_favorite=False):
    def toggle_favorite(e):
        on_favorite(icon_name)
        e.control.icon = (
            ft.Icons.STAR if icon_name in on_favorite.__self__.favorites else ft.Icons.STAR_OUTLINE
        )
        e.control.update()

    return ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    name=icon_name,
                    size=30,
                ),
                ft.IconButton(
                    icon=ft.Icons.STAR if is_favorite else ft.Icons.STAR_OUTLINE,
                    on_click=toggle_favorite,
                ),
                ft.Text(icon_name, size=10, selectable=True)
            ]
        ),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border=ft.border.all(1, ft.Colors.OUTLINE),  # <-- Corrigido aqui
        border_radius=5,
        padding=10,
    )
