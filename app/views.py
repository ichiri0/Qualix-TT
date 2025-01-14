from django.forms import Form
from django.views.generic import FormView
from django.shortcuts import render

from app.utils.web_client import JsonRpcClient
from .forms import RpcCallForm
from django.conf import settings


class RpcCallView(FormView):
    template_name = "rpc_call.html"
    form_class = RpcCallForm

    def form_valid(self, form: Form):
        method = form.cleaned_data['method']
        params = form.cleaned_data.get('params')
        client = JsonRpcClient(endpoint=settings.JSONRPC_ENDPOINT)
        result = client.call_method(method, params)
        print(result)
        return render(self.request, self.template_name, {
            'form': form,
            'result': result
        })