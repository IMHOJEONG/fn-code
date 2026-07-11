from abc import ABC, abstractmethod

class MultimediaPlayer(ABC):
    @abstractmethod
    def play_media(self, file: str) -> None:
        pass

    @abstractmethod
    def stop_media(self) -> None:
        pass

    @abstractmethod
    def display_lyrics(self, file: str) -> None:
        pass

    @abstractmethod
    def apply_video_filter(self, filter: str) -> None:
        pass

class MusicPlayer(MultimediaPlayer):
    def play_media(self, file: str) -> None:
        print(f"음악 재생 중: {file}")

    def stop_media(self) -> None:
        print(f"음악 중지 중")

    def display_lyrics(self, file):
        print(f"{file}의 가사 표시 중")

    def apply_video_filter(self, filter: str) -> None:
        raise NotImplementedError(
            "MusicPlayer가 지원하지 않는 비디오 필터"
        )

class VideoPlayer(MultimediaPlayer):
    # ....