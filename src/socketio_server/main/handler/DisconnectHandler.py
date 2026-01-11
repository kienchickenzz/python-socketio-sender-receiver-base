"""
DisconnectHandler - Xử lý khi client disconnect khỏi server

Handler cho disconnect event trên server side
"""
from socketio import AsyncServer

from src.socketio_server.shared.interface.IEventHandler import IEventHandler
from src.socketio_server.main.enum.MainEvent import MainEvents
from src.socketio_server.main.enum.MainNamespace import MainNamespaces


class DisconnectHandler(IEventHandler):
    """Handler xử lý disconnect event từ client"""

    event = MainEvents.DISCONNECT
    namespace = MainNamespaces.ROOT

    async def handle(self, sio: AsyncServer, sid: str, data=None):
        """
        Xử lý khi client disconnect khỏi server

        Args:
            sio: SocketIO AsyncServer instance
            sid: Socket ID của client
            data: Optional data

        Returns:
            None (fire-and-forget)
        """
        print(f"[Server] Client {sid} disconnected from {self.namespace.value}")

        # Cleanup nếu cần
        # - Xóa session
        # - Notify other clients
        # - Release resources
