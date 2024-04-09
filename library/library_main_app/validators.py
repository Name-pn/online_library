from rest_framework import serializers

class TitleFieldValidator:
    def __call__(self, value):
        if value.isdigit() == True:
            raise serializers.ValidationError('Поле не может состоять из одних цифр')
        return value

# Пример кода для валидации form-data по параметрам, которые имеются в модели
class UnknownFieldsValidator:
    requires_context = True
    def __call__(self, data, serializer=None):
        if serializer:
            allowed_fields = set(serializer.fields.keys())
        else:
            allowed_fields = {' * '}
        for key in data:
            if key not in allowed_fields:
                raise serializers.ValidationError({
                    key: "Это поле не определено в модели."
                })