import json
import uuid

from django.test import TestCase

from .models import TrashCan

JSON = "application/json"


class TrashCanTests(TestCase):
    """Test TrashCan functionality."""

    def test_create_trash_can(self):
        """Create a nonexistent TrashCan, recall it, and destroy it."""
        response = self.client.post("/trashcans/")
        self.assertEqual(response.status_code, 201)
        id = json.loads(response.content)["id"]
        TrashCan.objects.get(id=uuid.UUID(id))

    def test_create_trash_can_with_uuid(self):
        """Create a TrashCan using an existing UUID."""
        # We need to be able to force a UUID because the trash can generates its own
        new_trashcan = {"id": "00000000-0000-0000-0000-000000000000"}
        response = self.client.post("/trashcans/", json.dumps(new_trashcan), content_type=JSON)
        self.assertEqual(response.status_code, 201)
        TrashCan.objects.get(id=uuid.UUID(new_trashcan["id"]))


class TrashStatesTests(TestCase):
    """Test TrashStates."""

    def test_create_trash_state(self):
        """Return a Trash Can to associate with test Trash States."""
        t = TrashCan()
        t.save()
        new_trash_state = {
            "trash_can": "http://testserver/trashcans/{}/".format(t.id),
            "timestamp": "2018-10-26T18:22:00Z",
            "fill_state": 18.12345
        }
        post_response = self.client.post("/trashstates/", json.dumps(new_trash_state), content_type=JSON)
        self.assertEqual(post_response.status_code, 201)
        get_response = self.client.get("/trashstates/")
        success = False
        for state in json.loads(get_response.content):
            if state == new_trash_state:
                success = True
        self.assertTrue(success)

    def test_create_bogus_trash_state(self):
        """Show that Trash States must belong to an existent Trash Can."""
        new_trash_state = {
            "trash_can": "http://testserver/trashcans/f59e4893-5f07-4748-8318-0619d35ddd39/",
            "timestamp": "2018-10-26T18:22:00Z",
            "fill_state": 18.12345
        }
        self.assertEqual(self.client.post("/trashstates/", json.dumps(new_trash_state), content_type=JSON).status_code,
                         400)
