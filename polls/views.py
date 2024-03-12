from django.views import View
from .models import PollingUnit, Lga
from django.shortcuts import render


class IndexView(View):

    def get(self, request):
        all_polling_unit = PollingUnit.objects.all()

        return render(request, "index.html", {"all_polls": all_polling_unit})


class ResultView(View):


    template_name = "polling_result_page.html"

    def get(self, request, pu_id):
        print(pu_id)
        polling_unit = PollingUnit.objects.get(uniqueid=pu_id)
        return render(request, template_name=self.template_name, context={
            "polling_unit": polling_unit
        })



class LgaPollingView(View):

    template_name = "lga_polling_sum.html"

    def get(self, request):
        all_lga = Lga.objects.all()
        return render(
            request, template_name=self.template_name, context={
                "all_lga": all_lga
            }
        )

    def post(self, request):
        print(request.POST)
        selected_lga = Lga.objects.get(lga_name=request.POST['lga'])
        all_pu = PollingUnit.objects.all().filter(lga_id=selected_lga.uniqueid)
        return render(request, self.template_name, context={
            "selected_lga": selected_lga.lga_name,
            "all_lga": Lga.objects.all(),
            "all_pu": all_pu,
            "len_all_pu": len(all_pu)
        })




