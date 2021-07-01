"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
        return num_videos

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        sorted_videos = sorted(videos, key=lambda x:x.title)
        for video in sorted_videos:
            video_format = f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"
            print(video_format)


    global check_playing
    check_playing = []

    def play_video(self, video_id):
        """Plays the respective video.
        #play video, stop video if currently playing, if doesnt exist display warning

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            print("Playing video: " + str(video.title))
            check_playing.append(video.title)

        if len(check_playing) != 0 and video is not None:
            print("Stopping video: " + str(check_playing[0]))
            check_playing.pop()

    def stop_video(self):
        """Stops the current video."""
        if len(check_playing) != 0:
            print("Stopping video: " + str(check_playing[0]))
            check_playing.pop()
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if len(check_playing) != 0:
            print("Stopping video: " + str(check_playing[0]))
            check_playing.pop()

        videos = self._video_library.get_all_videos()
        random_video = random.choice(videos)
        print("Playing video: " + str(random_video.title))
        check_playing.append(random_video.title)

    global check_pausing
    check_pausing = []

    def pause_video(self):
        """Pauses the current video."""
        if len(check_pausing) != 0 and len(check_playing) != 0:
            print("Video already paused: " + str(check_playing[0]))
        elif len(check_playing) != 0 and len(check_pausing) == 0:
            print("Pausing video: " + str(check_playing[0]))
            check_pausing.append(str(check_playing[0]))
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if len(check_pausing) != 0:
            print("Continuing video: " + str(check_pausing[0]))
            check_pausing.pop()
        elif len(check_playing) != 0 and len(check_pausing) == 0:
            print("Cannot continue video: Video is not paused")

        if len(check_playing) == 0:
            print("Cannot continue: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if len(check_playing) != 0:
            videos = self._video_library.get_all_videos()
            for video in videos:
                if video.title == str(check_playing[0]):
                    video_format = f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"
                    print("Currently playing: " + video_format)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
