

class ModernNotificationService:
    """ 서로 다른 인터페이스를 가진 외부 알림 서비스 """
    def send_notification(self, payload: dict) -> None:
        # 최신 알림 서비스의 실제 구현
        pass

class ModernNotificationAdapter(NotificationPort):
    """ 
        기존 애플리케이션의 알림 인터페이스에 맞게
        최신 알림 서비스를 연결하기 위한 어댑터
    """
    def __init__(self, modern_service: ModernNotificationService):
        self._service = modern_service
    
    def notify_task_completed(self, task: Task) -> None:
        self._service.send_notification({
            "type": "TASK_COMPLETED",
            "taskId": str(task.id)
        })