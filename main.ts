let number1 = 0
input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 1; index++) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # . . . #
            # . # . #
            # . . . #
            # # # # #
            `)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    number1 = randint(1, 100)
    basic.showNumber(number1)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Made By Suhani!")
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
