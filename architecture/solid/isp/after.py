from abc import ABC, abstractmethod

class MediaPlayable(ABC):
    @abstractmethod
    def play_media(self, file: str) -> None:
        pass

    @abstractmethod
    def stop_media(self) -> None:
        pass

class LyricsDisplayable(ABC):
    @abstractmethod
    def display_lyrics(self, file: str) -> None:
        pass

class VideoFilterable(ABC):
    @abstractmethod
    def apply_video_filter(self, filter: str) -> None:
        pass

class MusicPlayer(MediaPlayable, LyricsDisplayable):
    @abstractmethod
    def play_media(self, file: str) -> None:
        print(f"음악 재생 중: {file}");

    def stop_media(self) -> None:
        print("음악 중지 중");

    def display_lyrics(self, file: str) -> None:
        print(f"가사 표시 중: {file}");

class VideoPlayer(MediaPlayable, VideoFilterable):
    def play_media(self, file: str) -> None:
        print(f"동영상 재생 중: {file}");

    def stop_media(self) -> None:
        print("동영상 중지 중")

    def apply_video_filter(self, filter: str) -> None:
        print(f"비디오 필터 적용: {filter}")

class BasicAudioPlayer(MediaPlayable):
    def play_media(self, file: str) -> None:
        print(f"오디오 재생 중: {file}")

    def stop_media(self) -> None:
        print("오디오 중지 중")