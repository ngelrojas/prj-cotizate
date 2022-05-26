from django.contrib.auth import authenticate
from django.utils.translation import gettext as _

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework.exceptions import APIException

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomLoginUser(JSONWebTokenSerializer):
    def validate(self, attrs):
        try:
            credentials = {
                "email": attrs.get("email"),
                "password": attrs.get("password"),
            }

            if all(credentials.values()):
                user = authenticate(**credentials)

                if user:
                    if not user.is_activate:
                        msg = _("User account is not activated.")
                        raise serializers.ValidationError(msg)
                    payload = jwt_payload_handler(user)

                    return {"token": jwt_encode_handler(payload)}
                else:
                    msg = _("Unable to log in with provided credentials")
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Must include "{email_field}" and "password"')
                msg = msg.format(username_field=self.email_field)
                raise serializers.ValidationError(msg)

        except serializers.ValidationError as ex:
            raise ex
        except Exception as ex:
            raise APIException(
                {
                    "data": "error",
                    "msg": "An unexpected error ocurred",
                    "detail": format(ex),
                }
            )
