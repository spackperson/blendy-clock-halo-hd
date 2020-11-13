def write_seconds():
    global restore_second
    restore_second = kitronik_halo_hd.read_time_for_zip(TimeParameter.SECONDS) - 1
    if restore_second < 0:
        restore_second = 59
    if restore_second <= kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS) and restore_second <= kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        haloDisplay.set_zip_led_color(restore_second, blended_color)
        haloDisplay.show()
    if restore_second <= kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS) and restore_second > kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        haloDisplay.set_zip_led_color(restore_second, hours_color)
        haloDisplay.show()
    if restore_second > kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS) and restore_second <= kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        haloDisplay.set_zip_led_color(restore_second, minutes_color)
        haloDisplay.show()
    if restore_second > kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS) and restore_second > kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        haloDisplay.set_zip_led_color(restore_second, kitronik_halo_hd.colors(ZipLedColors.BLACK))
        haloDisplay.show()
    haloDisplay.set_zip_led_color(kitronik_halo_hd.read_time_for_zip(TimeParameter.SECONDS),
        seconds_color)
    haloDisplay.show()
def write_hours():
    index = 0
    while index <= kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS):
        haloDisplay.set_zip_led_color(index, hours_color)
        haloDisplay.show()
        index += 1

def on_button_pressed_ab():
    kitronik_halo_hd.set_time(9, 45, 0)
    haloDisplay.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def write_minutes():
    index2 = 0
    while index2 <= kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        if index2 <= kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS):
            haloDisplay.set_zip_led_color(index2, blended_color)
            haloDisplay.show()
        if index2 > kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS):
            haloDisplay.set_zip_led_color(index2, minutes_color)
            haloDisplay.show()
        index2 += 1
blended_color = 0
hours_color = 0
minutes_color = 0
seconds_color = 0
restore_second = 0
haloDisplay: kitronik_halo_hd.ZIPHaloHd = None
haloDisplay = kitronik_halo_hd.create_zip_halo_display(60)
# Good idea to initialize variable before use (negative to force a comparison/update)
last_hours = -1
last_minutes = -1
last_second = -1
restore_second = -1
haloDisplay.clear()
seconds_color = kitronik_halo_hd.colors(ZipLedColors.RED)
minutes_color = kitronik_halo_hd.colors(ZipLedColors.YELLOW)
hours_color = kitronik_halo_hd.colors(ZipLedColors.BLUE)
# This is the overlap/blendy color. Choose what you like. This is your world. You have absolute power.
blended_color = kitronik_halo_hd.rgb(26, 51, 0)

def on_forever():
    basic.show_number(input.temperature())
basic.forever(on_forever)

def on_forever2():
    global last_hours, last_minutes, last_second
    if last_hours != kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS):
        write_hours()
        last_hours = kitronik_halo_hd.read_time_for_zip(TimeParameter.HOURS)
    if last_minutes != kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES):
        write_minutes()
        last_minutes = kitronik_halo_hd.read_time_for_zip(TimeParameter.MINUTES)
    if last_second != kitronik_halo_hd.read_time_for_zip(TimeParameter.SECONDS):
        write_seconds()
        last_second = kitronik_halo_hd.read_time_for_zip(TimeParameter.SECONDS)
basic.forever(on_forever2)
