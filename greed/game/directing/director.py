from game.shared.point import Point
from game.casting.artifact import Artifact
from game.shared.color import Color
import random

# Basic values for game data
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.player_score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

        artifact = cast.get_first_actor("artifacts")
        artifact_velocity = self._keyboard_service.get_entity_direction()
        artifact.set_velocity(artifact_velocity)

        boulder = cast.get_first_actor("boulders")  
        boulder_velocity = self._keyboard_service.get_entity_direction()
        boulder.set_velocity(boulder_velocity)    

    def _do_updates(self, cast):
        """Updates the position's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("player")
        artifact = cast.get_first_actor("artifacts")
        boulder = cast.get_first_actor("boulders")

        banner.set_text(f"score: {self.player_score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        artifact.move_next(max_x, max_y)
        if player.get_position().equals(artifact.get_position()):
            message = "You found a gem!"
            banner.set_text(message)
            self.player_score += 1
            artifact.remove_actor("artifacts", artifact)

            #create a new artifact
            text = "*"
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            cast.add_actor("artifacts", artifact)

        boulder.move_next(max_x, max_y)
        if player.get_position().equals(boulder.get_position()):
            message = "Ouch!"
            banner.set_text(message)
            self.player_score -= 1
            boulder.remove_actor("boulders", boulder)

            # create a new boulder
            text = "{}"
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            r = 150
            g = 150
            b = 100
            color = Color(r, g, b)

            boulder = Artifact()
            boulder.set_text(text)
            boulder.set_font_size(FONT_SIZE)
            boulder.set_color(color)
            boulder.set_position(position)
            cast.add_actor("boulders", boulder)

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()