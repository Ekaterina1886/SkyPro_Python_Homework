import pytest
import requests


class TestProjectsAPI:

    # ---------- POST /api-v2/projects ----------

    def test_create_project_positive(self, api):
        """Создание проекта с валидным именем"""
        response = api.create_project("My_new_project")
        assert response.status_code == 201
        body = response.json()
        assert "id" in body
        assert body["name"] == "My_new_project"

    def test_create_project_negative(self, api):
        """Ошибка при создании проекта без имени"""
        response = api.create_project("")
        assert response.status_code == 400 or response.status_code == 401

    # ---------- PUT /api-v2/projects/{id} ----------

    def test_update_project_positive(self, api, new_project):
        """Обновление имени существующего проекта"""
        project_id = new_project["id"]
        response = api.update_project(project_id, "Updated name")
        assert response.status_code == 200
        updated = response.json()
        assert "id" in updated

    def test_update_project_negative(self, api):
        """Попытка обновить несуществующий проект"""
        fake_id = "999999999999"
        response = api.update_project(fake_id, "Some name")
        assert response.status_code in (404, 400, 401)

    # ---------- GET /api-v2/projects/{id} ----------

    def test_get_project_positive(self, api, new_project):
        """Получение информации о существующем проекте"""
        response = api.get_project(new_project["id"])
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == new_project["id"]

    def test_get_project_negative(self, api):
        """Запрос несуществующего проекта"""
        response = api.get_project("999999999999")
        assert response.status_code in (404, 401, 400)
