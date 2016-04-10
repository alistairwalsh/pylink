from psychopy import visual, core, event, monitors
import unittest

class NewWindowTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.win = visual.Window(color='black')
        self.rect = visual.Rect(win, width=.5, height=.3, fillColor='red')

    def tearDown(self):  #3
        self.win.close()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.rect.draw() 
        self.win.flip()  # don't forget to flip when done with drawing all stimuli so that the stimuli become visible
        self.event.waitKeys()

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  #5
        self.fail('Finish the test!')  #6

        # She is invited to enter a to-do item straight away
        

if __name__ == '__main__':  #7
    unittest.main()  #8
