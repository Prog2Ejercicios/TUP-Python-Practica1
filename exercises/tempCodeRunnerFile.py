Cliente = {

    "Nombre": "Mario Pedernera",
    "DNI": 56895632,
    "Domicilio": "Los alamos 4509",
    "Compras": ["cafetera", "TV 50 pulgadas", "mouse gamer"]
}
# COMPLETAR - FIN

assert (
    (Cliente["Nombre"] == "Mario Pedernera")
    and (Cliente["DNI"] == 56895632)
    and (Cliente["Domicilio"] == "Los alamos 4509")
    and (Cliente["Compras"] == ["cafetera", "TV 50 pulgadas", "mouse gamer"])
)