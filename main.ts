let granularity = [20, 100, 500]
let x = 0
let y = 0
let tx = 0
let ty = 0

function position(reading: number) {
    // position, calculate the position on the display
    let res = 0
    let modification = 1
    if (reading < 0) {
        reading = Math.abs(reading)
        modification = -1
    }
    for (let pos = 0; pos < granularity.length; pos++) {
        res = 2 + (pos * modification)
        if (Math.min(granularity[pos], reading) == reading) {
            break
        }
    }
    return res
}
function draw(x: number, y: number) {
    // draw, draw cross pointer
    basic.clearScreen()
    led.plot(x, y)
    led.plot(x, y - 1)
    led.plot(x - 1, y)
    led.plot(x, y + 1)
    led.plot(x + 1, y)
}
basic.forever(function () {
    x = position(input.acceleration(Dimension.X))
    y = position(input.acceleration(Dimension.Y))
    if (x != tx || y != ty) {
        draw(x, y)
        tx = x
        ty = y
    }
})
