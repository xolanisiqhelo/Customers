from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *

admin.site.register(CodeReference)


# Register your models here.


class CustomerResource(resources.ModelResource):
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        print(dataset)
        # def create_table(custCode, name, surname, address,des):

        _list = []
        for x in dataset:
            _list.append(x)
        s = _list
        print(s)

    #     print(";".join(s))
    def before_import_row(self, row, **kwargs):
        print(row)

    class Meta:
        model = Customer
        skip_unchanged = False
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('customerCode',)
        fields = ['customerCode']
        print('this is inside the model', fields, model)


class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    # print('this is the data that we are seding 2', ImportExportModelAdmin)
    # pass


admin.site.register(Customer, CustomerAdmin)
