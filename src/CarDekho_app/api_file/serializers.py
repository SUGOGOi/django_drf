from rest_framework import serializers
from ..models import CarList , ShowroomList, Review


#********************************VALIDATOR FOR CARSERIALIZER(NOT WORKING)**********************************
# def alphanumeric(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError('Only alphanumeric character')

#********************************************USING ONLY SERIALIZER******************************************
# class CarSerializer(serializers.Serializer):
#     id  = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#     chassisnumber = serializers.CharField(validators=[alphanumeric]) # validator
#     price = serializers.DecimalField(max_digits=9, decimal_places=2)

#     def create(self, validated_data):
#         return CarList.objects.create(**validated_data) 
#         #The ** operator unpacks the dictionary into keyword arguments for the create method
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
#         instance.price = validated_data.get('price',instance.price)
#         instance.save()
#         return instance

#********************************************USING MODEL SERIALIZER******************************************
class ReviewSerializer(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Review
        exclude=('car',)  #*****NOT SHOW CAR IN REVIEW_DETAIL(GET) + NO NEED TO GIVE CAR'S ID===> IT TAKE FROM URL
        # But i want to show CAR in  REVIEW_DETAIL(GET) , currently not working
        # fields = '__all__' #********************IT INCLUDE ALL THE FIELDS*******************
    def get_car(self,object):
        return object.car


class CarSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField() # custom serializer
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = CarList
        fields ="__all__"
        # fields = ["id","name","description"]
        # exclude = ["name"]
        
    def get_discounted_price(self,object):
        discountprice = object.price - 5000
        return discountprice
    

    # field level validator
    def validate_price(self, value):
        if value < 20000.00:
            raise serializers.ValidationError('Price must be greater than 20k')
        return value
    
    #simple validator / object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    

class ShowroomSerializer(serializers.ModelSerializer):
    #***********************************SHOW DATA OF FOREIGN TABLE*****************************************8
    # cars = CarSerializer(many=True, read_only=True) -------> show all fields
    # cars = serializers.StringRelatedField(many=True, read_only= True) # filed given in __str__ method
    # cars = serializers.PrimaryKeyRelatedField(many=True, read_only= True) 
    cars = serializers.HyperlinkedRelatedField(many=True, read_only= True, view_name='cardetail') 
    class Meta:
        model = ShowroomList
        fields = '__all__'


