from django.shortcuts import render
from datetime import datetime, timedelta, date
import json
from django.contrib.auth.models import User
from django.views import View

import glob
from os.path import dirname, basename, join
handlers_collection = glob.glob(join(dirname(__file__), "handlers", "*.py"))
for f in handlers_collection:
    import_script =\
"""\
from .{0}.{1} import *\
""".format("handlers", basename(f[:-3]).replace('/', '.'))
    # print(import_script)
    exec (import_script)

class Dashboard(View):

    def get(self, request):
        now = datetime.now()
        threshold_timestamp = now - timedelta(hours=8)

        tempHandler = TemperatureHandler()
        tempHandler.setTimezoneShift(timedelta(hours=8))
        tempHandler.setThresholdTimestamp(threshold_timestamp)

        humidHandler = HumidityHandler()
        humidHandler.setTimezoneShift(timedelta(hours=8))
        humidHandler.setThresholdTimestamp(threshold_timestamp)

        planthandler = PlantDataHandler()

        messageHandler = MessageCenterHandler(self.request)
        messageHandler.setNow(now)

        piCpuTempHander = PiCpuTempStatusHander()
        wateringStatusHandler = WateringStatusHander()
        cameraSatausHander = CameraTaskStatusHander()
        warningStatusHandler = WarningStatusHander()

        contextHandler = ContextHandler()
        contextHandler.join(tempHandler)
        contextHandler.join(humidHandler)
        contextHandler.join(planthandler)
        contextHandler.join(messageHandler)
        contextHandler.join(piCpuTempHander)
        contextHandler.join(wateringStatusHandler)
        contextHandler.join(cameraSatausHander)
        contextHandler.join(warningStatusHandler)
        contextHandler.fillInContext()

        return render(self.request, 'template_dashboard/dashboard.html', contextHandler.getContext())
