from gweather.I_KNOW_THIS_IS_UNSTABLE import gweather

for loc in gweather.location_new_world(False).get_children():
    print loc.get_name()
    for zone in loc.get_timezones():
        if zone.get_name() is not None:
            print "  %s" % zone.get_name()
