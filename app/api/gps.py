from app.api import api_call
from app.utils.logger import get_logger

l = get_logger("api.gps")


def set_position(imei: str, lat: float, lon: float, speed: float | None = None):
    l.info("set position imei=%s lat=%s lon=%s speed=%s", imei, lat, lon, speed)
    api_call("gps", "set_position", post=True, id=imei, lat=lat, lng=lon, speed=speed)
