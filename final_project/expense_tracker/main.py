import sys
from PySide6.QtWidgets import QApplication

from controllers.expense_controller import ExpenseController
from views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    controller = ExpenseController()
    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
