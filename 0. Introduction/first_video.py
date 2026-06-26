from manim import *

class FirstMathVideo(Scene):
    def construct(self):
        title = Text("Maths Impressions for Everyone").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        eq1 = MathTex("y = x^2").scale(1.4)
        self.play(Write(eq1))
        self.wait(1)

        eq2 = MathTex("y = (x-2)^2 + 1").scale(1.4)
        self.play(Transform(eq1, eq2))
        self.wait(1)

        axes = Axes(
            x_range=[-4, 6, 1],
            y_range=[-1, 10, 1],
            x_length=9,
            y_length=5,
            tips=False
        ).to_edge(DOWN)

        graph1 = axes.plot(lambda x: x**2, x_range=[-3, 3])
        graph2 = axes.plot(lambda x: (x-2)**2 + 1, x_range=[-2, 6])

        label1 = axes.get_graph_label(graph1, MathTex("y=x^2"))
        label2 = axes.get_graph_label(graph2, MathTex("y=(x-2)^2+1"))

        self.play(Create(axes))
        self.play(Create(graph1), FadeIn(label1))
        self.wait(1)

        self.play(Transform(graph1, graph2), Transform(label1, label2))
        self.wait(2)