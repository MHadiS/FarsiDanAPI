import pytest
from django.core.exceptions import ValidationError

from question.models import Difficulty

@pytest.mark.django_db
class TestDifficulty:
    def test_creating_and_deleting(self):
        record = Difficulty.objects.create(
            level_name="-" * 20
        )
        record.save()
        record.delete()