import unittest
import responses
from twilio.rest import Client


class TestVideoRooms(unittest.TestCase):
    @responses.activate
    def test_create_video_room(self):
        # Configuración de credenciales de prueba
        account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        auth_token = "your_auth_token"
        client = Client(account_sid, auth_token)

        # Simulación de la respuesta del endpoint de creación de salas de video
        responses.add(
            responses.POST,
            "https://video.twilio.com/v1/Rooms",
            json={
                "sid": "RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "unique_name": "TestRoom",
                "status": "in-progress",
            },
            status=201,
            content_type="application/json",
        )

        # Llamada al método para crear la sala
        room = client.video.rooms.create(unique_name="TestRoom", type="group")

        # Verificaciones de la respuesta
        self.assertEqual(room.sid, "RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.assertEqual(room.unique_name, "TestRoom")
        self.assertEqual(room.status, "in-progress")


if __name__ == "__main__":
    unittest.main()
