from manim import *
import numpy as np

class ContinuousTimeSignal(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1], y_range=[-3, 3, 1],
            x_length=10, y_length=6,
            axis_config={"color": GREY},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label="t", y_label="Amplitude")

        # Create initial sine wave
        amplitude = 1
        frequency = 1
        phase = 0
        sine_wave = axes.plot(lambda t: amplitude * np.sin(2 * np.pi * frequency * t + phase),
                              color=BLUE, x_range=[0, 10])

        sine_wave_label = MathTex("y(t) = A \, \sin(2\pi f t + \phi)").to_edge(UP)

        # Add initial elements to the scene
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sine_wave), Write(sine_wave_label))
        self.wait(2)

        # Add sliders for amplitude, frequency, and phase
        amplitude_slider = ValueTracker(amplitude)
        frequency_slider = ValueTracker(frequency)
        phase_slider = ValueTracker(phase)

        # Update sine wave dynamically
        sine_wave.add_updater(
            lambda m: m.become(
                axes.plot(lambda t: amplitude_slider.get_value() * np.sin(
                    2 * np.pi * frequency_slider.get_value() * t + phase_slider.get_value()),
                          color=BLUE, x_range=[0, 10])
            )
        )

        # Show all initial values
        amplitude_text = MathTex(f"A = {amplitude}").to_corner(UP + LEFT)
        phase_text = MathTex(f"\phi = {phase}").next_to(amplitude_text, DOWN)
        frequency_text = MathTex(f"f = {frequency} \, Hz").next_to(phase_text, DOWN)
        self.play(FadeIn(amplitude_text), FadeIn(phase_text), FadeIn(frequency_text))

        # Show amplitude change
        new_amplitude = 2
        self.play(
            amplitude_slider.animate.set_value(new_amplitude),
            Transform(amplitude_text, MathTex(f"A = {new_amplitude}").to_corner(UP + LEFT))
        )
        self.wait(2)

        # Show phase change
        new_phase = np.pi / 2
        self.play(
            phase_slider.animate.set_value(new_phase),
            Transform(phase_text, MathTex(f"\\phi = \\, \\pi/2").next_to(amplitude_text, DOWN))
        )
        self.wait(2)

        # Show frequency change
        new_frequency = 2
        self.play(
            frequency_slider.animate.set_value(new_frequency),
            Transform(frequency_text, MathTex(f"f = {new_frequency} \\, Hz").next_to(phase_text, DOWN))
        )
        self.wait(2)

        # End scene
        self.play(FadeOut(sine_wave), FadeOut(amplitude_text), FadeOut(frequency_text), FadeOut(phase_text), FadeOut(axes), FadeOut(sine_wave_label))
        self.wait()
