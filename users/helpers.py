import uuid
from django.db.models import TextChoices


class SaveMediaFile(object):
    def home_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'building/home//{uuid.uuid4()}.{image_extension}'

    def travel_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'travelling/travels//{uuid.uuid4()}.{image_extension}'

    def user_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'users/user//{uuid.uuid4()}.{image_extension}'

    def agent_image(self, filename):
        image_extension = filename.split('.')[-1]
        return f'users/user//{uuid.uuid4()}.{image_extension}'

    def testimonial(self, filename):
        image_extension = filename.split('.')[-1]
        return f'users/testmonial//{uuid.uuid4()}.{image_extension}'


class Choices(object):
    class PriceType(TextChoices):
        s = "USD", "$"
        sum = "UZS", "SO'M"