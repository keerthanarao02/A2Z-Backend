from rest_framework import serializers
from .models import *

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'

class AccountTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTypes
        fields = ['account_type_id', 'name', 'create_date']

class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = ['case_id', 'dispatch_entry_id', 'csr_id']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'name', 'phone', 'email', 'address', 'city', 'state', 'pincode',
                  'country', 'create_date', 'company_type', 'status', 'auth_token',
                  'monthly_fee', 'notes']
        
class CompanyFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFeatures
        fields = ['company_id', 'company_features_id', 'feature_id', 'name', 'create_date']
        
class CompanyPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPricing
        fields = ['id', 'rate_item_id', 'default_rate', 'company_id']

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['customer_id', 'name', 'email', 'phone', 'whatsapp_number']
        
class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = ['id', 'customer_id', 'review', 'rating', 'name', 'phone', 'notes']

class DispatchEntryAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchEntryAssets
        fields = '__all__'
        
class DispatchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchStatus
        fields = ['dispatch_status_id', 'name']
        
class DispatchEntryStatusRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchEntryStatusRecords
        fields = '__all__'

class DispatchEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchEntry
        fields = '__all__'
        
class DriverLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLocation
        fields = '__all__'
        
class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['feature_id', 'name', 'create_date']
        
class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'
        
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
        
class RateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateItem
        fields = '__all__'
        
class ReasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reasons
        fields = ['reason_id', 'name', 'create_date', 'service_type']
        
# class ServiceProviderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceProvider
#         fields = '__all__'
        
class ServiceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypes
        fields = ['service_type_id', 'service', 'service_type']
        
class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ['csr_id', 'name', 'create_date', 'role', 'role_id', 'status']
        
class SystemUserStatusRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUserStatusRecords
        fields = ['id', 'dispatch_entry_id', 'previous_csr_id', 'new_csr_id', 'create_date']
        
class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['vehicle_id', 'make_id', 'make', 'model_id', 'model', 'year', 'vehicle_class', 'vehicle_type']