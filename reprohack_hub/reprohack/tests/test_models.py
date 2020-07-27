#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from reprohack_hub.users.models import User
from reprohack_hub.users.tests.factories import UserFactory

from reprohack_hub.reprohack.models import Event, Paper


pytestmark = pytest.mark.django_db


def test_event_save(user: User) -> None:
    """Test basic Event save."""
    test_title: str = "A Title"
    event: Event = Event(
        host="Test Host",
        title=test_title,
        user=user
    )
    event.save()
    assert str(event) == test_title
    assert event.get_absolute_url() == f'/reprohack/event/{event.id}/'


def test_paper_save(user: User) -> None:
    """Test basic Paper save."""
    test_title: str = "A Title"
    paper: Paper = Paper(
        title=test_title,
        user=user
    )
    paper.save()
    assert str(paper) == test_title
    assert paper.get_absolute_url() == f'/reprohack/paper/{paper.id}/'