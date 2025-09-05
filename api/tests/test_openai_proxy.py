from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


EXPECTED_501 = {
    "error": {
        "message": "This endpoint is not yet implemented.",
        "type": "not_implemented_error",
        "code": None,
    }
}


def test_post_chat_completions_501():
    resp = client.post("/v1/chat/completions", json={})
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501


def test_post_embeddings_501():
    resp = client.post("/v1/embeddings", json={})
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501


def test_get_models_501():
    resp = client.get("/v1/models")
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501


def test_post_images_generations_501():
    resp = client.post("/v1/images/generations", json={})
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501


def test_post_audio_transcriptions_501():
    resp = client.post("/v1/audio/transcriptions", json={})
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501


def test_post_audio_speech_501():
    resp = client.post("/v1/audio/speech", json={})
    assert resp.status_code == 501
    assert resp.json() == EXPECTED_501
