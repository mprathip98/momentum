import reflex as rx


class Spline(rx.Component):
    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]
spline = Spline.create
#link for the animation on Spline
scene = "https://prod.spline.design/WgCVJEkCUF1CFaaP/scene.splinecode"