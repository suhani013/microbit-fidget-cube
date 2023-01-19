number1 = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global number1
    basic.clear_screen()
    number1 = randint(1, 100)
    basic.show_number(number1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        # # # # #
                # . . . #
                # . # . #
                # . . . #
                # # # # #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)
