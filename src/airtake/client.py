import httpx
from nanoid import generate
from typing import Any
from .props import populate_props
from .utils import timestamp
from .types import Props

class Client:
  base_url: str = 'https://ingest.airtake.io'

  def __init__(self, *, token: str, base_url: str | None = None, debug: bool = False):
    self.token = token
    self.debug = debug

    if base_url:
      self.base_url = base_url

  def track(self, event: str, props: Props) -> None:
    actor_id = props.get('$actor_id') or props.get('$device_id')
    if not actor_id:
      raise ValueError('Either $actor_id or $device_id is required')

    self._request({
      'type': 'track',
      'id': generate(size=32),
      'timestamp': timestamp(),
      'actorId': actor_id,
      'name': event,
      'props': {
        **populate_props(),
        **props,
      },
    })

  def identify(self, actor_id: str | int, props: Props) -> None:
    device_id = props.pop('$device_id', None)

    self._request({
      'type': 'identify',
      'id': generate(size=32),
      'timestamp': timestamp(),
      'actorId': actor_id,
      'deviceId': device_id,
      'props': {
        **populate_props(),
        **props,
      },
    })

  @property
  def endpoint(self) -> str:
    return f'{self.base_url}/v1/events'

  def _request(self, body: dict[str, Any]) -> None:
    response = httpx.post(
      self.endpoint,
      headers={
        'X-Airtake-Token': self.token,
      },
      json=body,
    )

    if self.debug:
      response.raise_for_status()
