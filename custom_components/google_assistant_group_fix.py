DOMAIN = 'group'

MAPPED_DOMAIN = 'homeassistant'
MAPPED_SERVICE_ON = 'turn_on'
MAPPED_SERVICE_OFF = 'turn_off'

ENTITY_ID_ATTR = 'entity_id'

def setup(hass, config):

    def safe_map_call(call, mapped_service):
        entity_id = call.data.get(ENTITY_ID_ATTR, None)
        if entity_id is not None:
            data = { ENTITY_ID_ATTR: entity_id }
            hass.services.call(MAPPED_DOMAIN, mapped_service, data)

    def handle_turn_on(call):
        safe_map_call(call, MAPPED_SERVICE_ON)

    def handle_turn_off(call):
        safe_map_call(call, MAPPED_SERVICE_OFF)

    hass.services.register(DOMAIN, MAPPED_SERVICE_ON, handle_turn_on)
    hass.services.register(DOMAIN, MAPPED_SERVICE_OFF, handle_turn_off)

    return True