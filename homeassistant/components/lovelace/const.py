"""Constants for Lovelace."""
import voluptuous as vol

from homeassistant.const import CONF_TYPE, CONF_URL
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv

DOMAIN = "lovelace"
EVENT_LOVELACE_UPDATED = "lovelace_updated"

MODE_YAML = "yaml"
MODE_STORAGE = "storage"

LOVELACE_CONFIG_FILE = "ui-lovelace.yaml"
CONF_RESOURCES = "resources"
CONF_URL_PATH = "url_path"

RESOURCE_FIELDS = {
    CONF_TYPE: vol.In(["js", "css", "module", "html"]),
    CONF_URL: cv.string,
}
RESOURCE_SCHEMA = vol.Schema(RESOURCE_FIELDS)


class ConfigNotFound(HomeAssistantError):
    """When no config available."""
