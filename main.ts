function write_seconds () {
    restore_second = kitronik_halo_hd.readTimeForZip(TimeParameter.Seconds) - 1
    if (restore_second < 0) {
        restore_second = 59
    }
    if (restore_second <= kitronik_halo_hd.readTimeForZip(TimeParameter.Hours) && restore_second <= kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)) {
        haloDisplay.setZipLedColor(restore_second, blended_color)
        haloDisplay.show()
    }
    if (restore_second <= kitronik_halo_hd.readTimeForZip(TimeParameter.Hours) && restore_second > kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)) {
        haloDisplay.setZipLedColor(restore_second, hours_color)
        haloDisplay.show()
    }
    if (restore_second > kitronik_halo_hd.readTimeForZip(TimeParameter.Hours) && restore_second <= kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)) {
        haloDisplay.setZipLedColor(restore_second, minutes_color)
        haloDisplay.show()
    }
    if (restore_second > kitronik_halo_hd.readTimeForZip(TimeParameter.Hours) && restore_second > kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)) {
        haloDisplay.setZipLedColor(restore_second, kitronik_halo_hd.colors(ZipLedColors.Black))
        haloDisplay.show()
    }
    haloDisplay.setZipLedColor(kitronik_halo_hd.readTimeForZip(TimeParameter.Seconds), seconds_color)
    haloDisplay.show()
}
function write_hours () {
    for (let index = 0; index <= kitronik_halo_hd.readTimeForZip(TimeParameter.Hours); index++) {
        haloDisplay.setZipLedColor(index, hours_color)
        haloDisplay.show()
    }
}
input.onButtonPressed(Button.AB, function () {
    kitronik_halo_hd.setTime(9, 45, 0)
    haloDisplay.clear()
})
function write_minutes () {
    for (let index = 0; index <= kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes); index++) {
        if (index <= kitronik_halo_hd.readTimeForZip(TimeParameter.Hours)) {
            haloDisplay.setZipLedColor(index, blended_color)
            haloDisplay.show()
        }
        if (index > kitronik_halo_hd.readTimeForZip(TimeParameter.Hours)) {
            haloDisplay.setZipLedColor(index, minutes_color)
            haloDisplay.show()
        }
    }
}
let blended_color = 0
let hours_color = 0
let minutes_color = 0
let seconds_color = 0
let restore_second = 0
let haloDisplay: kitronik_halo_hd.ZIPHaloHd = null
haloDisplay = kitronik_halo_hd.createZIPHaloDisplay(60)
// Good idea to initialize variable before use (negative to force a comparison/update)
let last_hours = -1
let last_minutes = -1
let last_second = -1
restore_second = -1
haloDisplay.clear()
seconds_color = kitronik_halo_hd.colors(ZipLedColors.Red)
minutes_color = kitronik_halo_hd.colors(ZipLedColors.Yellow)
hours_color = kitronik_halo_hd.colors(ZipLedColors.Blue)
// This is the overlap/blendy color. Choose what you like. This is your world. You have absolute power.
blended_color = kitronik_halo_hd.rgb(26, 51, 0)
basic.forever(function () {
    basic.showNumber(input.temperature())
})
basic.forever(function () {
    if (last_hours != kitronik_halo_hd.readTimeForZip(TimeParameter.Hours)) {
        write_hours()
        last_hours = kitronik_halo_hd.readTimeForZip(TimeParameter.Hours)
    }
    if (last_minutes != kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)) {
        write_minutes()
        last_minutes = kitronik_halo_hd.readTimeForZip(TimeParameter.Minutes)
    }
    if (last_second != kitronik_halo_hd.readTimeForZip(TimeParameter.Seconds)) {
        write_seconds()
        last_second = kitronik_halo_hd.readTimeForZip(TimeParameter.Seconds)
    }
})
