from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password', 'password_confirmation']
        extra_kwargs={
            'password':{'write_only':True},
            'password_confirmation':{'required': True},
            'email': {'required': True},
        }

    def validate(self, data):
        
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Passwords mismatch')
            
        if User.objects.filter(email= data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        #****************USERNAME VALDATION AUTOMATIC************************
        return data
    
    def create(self,validated_data):      
        account = User(username = validated_data['username'], email=validated_data['email'])
        account.set_password(validated_data['password'])
        account.save()

        return account