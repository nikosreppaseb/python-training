# python-training/rock_paper_scissors_test.py
import unittest
from unittest.mock import patch
import io # Used to capture print output

# Import the module from the python-training package
from . import rock_paper_scissors as rps

class TestRockPaperScissors(unittest.TestCase):

    def test_determine_winner_tie(self):
        """Test Scenario 1: Tie scenarios."""
        self.assertEqual(rps.determine_winner("rock", "rock"), "It's a tie!")
        self.assertEqual(rps.determine_winner("paper", "paper"), "It's a tie!")
        self.assertEqual(rps.determine_winner("scissors", "scissors"), "It's a tie!")

    def test_determine_winner_user_wins(self):
        """Test Scenario 2: User win scenarios."""
        self.assertEqual(rps.determine_winner("rock", "scissors"), "🎉🍾🥂🎉 You win!")
        self.assertEqual(rps.determine_winner("scissors", "paper"), "🎉🍾🥂🎉 You win!")
        self.assertEqual(rps.determine_winner("paper", "rock"), "🎉🍾🥂🎉 You win!")

    def test_determine_winner_computer_wins(self):
        """Test Scenario 3: Computer win scenarios."""
        self.assertEqual(rps.determine_winner("scissors", "rock"), "😜😜 You lose!")
        self.assertEqual(rps.determine_winner("paper", "scissors"), "😜😜 You lose!")
        self.assertEqual(rps.determine_winner("rock", "paper"), "😜😜 You lose!")

    @patch('random.choice')
    def test_get_computer_choice(self, mock_choice):
        """Test Scenario 4: Get computer choice."""
        # Configure the mock to return a specific value
        mock_choice.return_value = "paper"
        self.assertEqual(rps.get_computer_choice(), "paper")
        # Check that random.choice was called once with the valid choices
        mock_choice.assert_called_once_with(rps.VALID_CHOICES)

        # Test another choice
        mock_choice.return_value = "rock"
        self.assertEqual(rps.get_computer_choice(), "rock")


    @patch('builtins.input', side_effect=['rock'])
    def test_get_user_choice_valid(self, mock_input):
        """Test Scenario 5: Get valid user choice."""
        self.assertEqual(rps.get_user_choice(), "rock")
        mock_input.assert_called_once() # Check input was called

    @patch('builtins.input', side_effect=['invalid', 'Spock', 'paper'])
    @patch('sys.stdout', new_callable=io.StringIO) # Capture print output
    def test_get_user_choice_invalid_then_valid(self, mock_stdout, mock_input):
        """Test Scenario 6: Get user choice (invalid then valid)."""
        expected_error_message = f"Invalid input. Please enter one of: {', '.join(rps.VALID_CHOICES)}.\n"

        choice = rps.get_user_choice()

        self.assertEqual(choice, "paper")
        self.assertEqual(mock_input.call_count, 3) # Called for 'invalid', 'Spock', 'paper'

        # Check that the error message was printed twice
        output = mock_stdout.getvalue()
        self.assertEqual(output.count(expected_error_message), 2)


    @patch('python_training.rock_paper_scissors.get_user_choice', return_value='rock')
    @patch('python_training.rock_paper_scissors.get_computer_choice', return_value='scissors')
    @patch('python_training.rock_paper_scissors.determine_winner')
    @patch('sys.stdout', new_callable=io.StringIO) # Capture print output
    def test_play_game_flow(self, mock_stdout, mock_determine_winner, mock_comp_choice, mock_user_choice):
        """Test Scenario 7: Main game flow."""
        # Configure the mock for determine_winner
        mock_determine_winner.return_value = "Mocked Win Result"

        rps.play_game()

        # Verify functions were called
        mock_user_choice.assert_called_once()
        mock_comp_choice.assert_called_once()
        mock_determine_winner.assert_called_once_with('rock', 'scissors')

        # Verify output contains expected parts
        output = mock_stdout.getvalue()
        self.assertIn("--- Rock Paper Scissors ---", output)
        self.assertIn("You chose: rock", output)
        self.assertIn("Computer chose: scissors", output)
        self.assertIn("Mocked Win Result", output)
        self.assertIn("-------------------------", output)


if __name__ == '__main__':
    unittest.main()