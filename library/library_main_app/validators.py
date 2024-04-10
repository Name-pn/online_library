from rest_framework import serializers


class TitleFieldValidator:
    def __call__(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Поле не может состоять из одних цифр")
        return value
