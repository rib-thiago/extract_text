from controller import ShowContentController
from textual.app import App
from view import ShowContentView

if __name__ == '__main__':
    controller = ShowContentController()
    view = ShowContentView(controller)
    view.run()
