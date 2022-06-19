from django.shortcuts import redirect, render
from watering.pump_driver import PumpDriver

pump_driver = PumpDriver()


def show_watering_status(request):
    context = {"pump_status": pump_driver.state, "pump_pin": pump_driver.channel}
    return render(request, "watering/show_watering_status.html", context)


def switch_pump(request):
    pump_driver.switch()
    return redirect("watering:show_watering_status")
