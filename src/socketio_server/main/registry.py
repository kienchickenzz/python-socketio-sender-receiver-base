"""
MainEventRegistry - Registry cho Main Server

Kế thừa từ BaseEventRegistry và implement _create_handlers()
để định nghĩa các handlers riêng cho main server.
"""
from src.socketio_server.shared.base.BaseEventRegistry import BaseEventRegistry
from src.socketio_server.shared.interface.IEventHandler import IEventHandler
from src.socketio_server.main.handler.ConnectHandler import ConnectHandler
from src.socketio_server.main.handler.DisconnectHandler import DisconnectHandler


class MainEventRegistry(BaseEventRegistry):
    """
    Registry cho Main Server, quản lý các event handlers.

    Kế thừa từ BaseEventRegistry và implement abstract method _create_handlers().
    """

    def _create_handlers(self) -> list[IEventHandler]:
        """
        Tạo và trả về danh sách các event handlers cho Main Server.

        Returns:
            List of main server event handlers
        """
        return [
            ConnectHandler(),
            DisconnectHandler(),
        ]
    